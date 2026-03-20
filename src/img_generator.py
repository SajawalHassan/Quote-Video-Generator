from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from io import BytesIO
import textwrap, requests, os
from dotenv import load_dotenv 

load_dotenv()

class ImageGenerator():
    def __init__(self, quote, author):
        self.quote = quote
        self.author = author
        self.img_size = 1080 
        self.font_path = "fonts/font.ttf"
        self.watermark_text = "@quill_of_humanity"

    def get_image(self, author_name):
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{author_name}"
        
        headers = {
            "User-Agent": f"MyQuoteBot/1.0 (https://example.com/bot; {os.getenv("WIKI_HEADER_EMAIL")})",
            "Accept": "image/*, application/json"
        }

        with requests.Session() as session:
            session.headers.update(headers)
            
            r = session.get(url)
            is_err = r.status_code != 200
            if is_err: raise Exception(f"API Error: {r.status_code}")

            data = r.json()
            
            img_url = data.get("thumbnail", {}).get("source")
            img_url_doesnt_exist = not img_url
            if img_url_doesnt_exist: raise Exception("No image found for this page.")

            img_response = session.get(img_url)

            if img_response.status_code == 403: raise Exception("403 Forbidden: Wikipedia blocked the image download.")
            elif img_response.status_code != 200: raise Exception(f"Image Download Error: {img_response.status_code}")

            return Image.open(BytesIO(img_response.content)).convert("RGB")

    # Crops image from get_image and applies opacity
    def format_image(self, img, target_size):
        width, height = img.size
        new_dimension = min(width, height)

        left = (width - new_dimension) / 2
        top = (height - new_dimension) / 2
        right = (width + new_dimension) / 2
        bottom = (height + new_dimension) / 2

        img = img.crop((int(left), int(top), int(right), int(bottom)))
        img = img.resize((target_size, target_size), Image.Resampling.LANCZOS)

        brightness = ImageEnhance.Brightness(img)
        opacity_factor = 0.3
        img = brightness.enhance(opacity_factor)

        return img

    def draw_quote_and_author_text(self, img, text, author):
        draw = ImageDraw.Draw(img)
        
        text_width = 28
        wrapper = textwrap.TextWrapper(width=text_width)
        wrapped_quote = wrapper.fill(text=text)
        
        try:
            quote_font = ImageFont.truetype(self.font_path, 60)
            author_font = ImageFont.truetype(self.font_path, 40)
        except OSError:
            quote_font = ImageFont.load_default()
            author_font = ImageFont.load_default()

        center_x = self.img_size / 2
        center_y = self.img_size / 2
        
        draw.multiline_text(
            (center_x, center_y), 
            text=wrapped_quote, 
            fill="white", 
            font=quote_font, 
            anchor="mm",
            align="center"
        )
        
        quote_bbox = draw.multiline_textbbox((0, 0), wrapped_quote, font=quote_font, align="center")
        quote_height = quote_bbox[3] - quote_bbox[1]

        spacing_factor = 120 # Y-Distance from quote
        author_y = center_y + (quote_height / 2) + spacing_factor
        
        draw.text((center_x, author_y), author, fill="white", font=author_font, anchor="mm")
        
        return img

    def draw_watermark_text(self, img, text):
        draw = ImageDraw.Draw(img)

        try:
            # font = ImageFont.truetype(self.font_path, 30)
            font = ImageFont.load_default(30)
        except:
            font = ImageFont.load_default(30)
        
        width = font.getlength(self.watermark_text)
        height = 40
        padding_factor = 50
        padding_x = width + padding_factor
        padding_y = height + padding_factor
        draw.text((self.img_size - padding_x, self.img_size - padding_y), text, fill="white", font=font, align="rb")

        return img

    def generate(self):
        author_name = self.author.replace(" ", "_")
        
        image = self.get_image(author_name)
        image = self.format_image(image, self.img_size)
        image = self.draw_quote_and_author_text(image, self.quote, self.author)
        image = self.draw_watermark_text(image, self.watermark_text).save("output.png")


if __name__ == "__main__":
    from input import input_dict
    
    imgGen = ImageGenerator(input_dict["quote"], input_dict["author"])
    imgGen.generate()