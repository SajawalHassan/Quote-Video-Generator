import os
from moviepy import AudioFileClip
from moviepy.video.VideoClip import ImageClip, TextClip
from moviepy.video.compositing import CompositeVideoClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import textwrap

class VideoGenerator:
    def __init__(self, quote, authorName, outputName):
        self.quote = quote
        self.outputName = outputName
        self.authorName = authorName
        self.height = 1920
        self.width = 1080
        self.duration = 7 # Seconds
        self.folder_path = "./images"

    def crop_image(self, img_path):
        clip = ImageClip(img_path)
        orig_w, orig_h = clip.size

        target_ratio = self.width / self.height
        orig_ratio = orig_w / orig_h

        if orig_ratio > target_ratio:
            new_w = int(round(orig_h * target_ratio))
            x1 = int((orig_w - new_w) // 2)
            y1 = 0
            cropped = clip.cropped(x1=x1, y1=y1, width=new_w, height=orig_h)
        else:
            new_h = int(round(orig_w / target_ratio))
            x1 = 0
            y1 = int((orig_h - new_h) // 2)
            cropped = clip.cropped(x1=x1, y1=y1, width=orig_w, height=new_h)

        final = cropped.resized(new_size=(self.width, self.height))
        return final

    def get_images(self):
        images = []
        for f in sorted(os.listdir(self.folder_path)):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                img_path = os.path.join(self.folder_path, f)

                cropped_img = self.crop_image(img_path)
                frame = cropped_img.get_frame(0)

                frame = (frame * 0.3).astype("uint8") 
                images.append(frame)
        
        return images

    def generate_bg(self):
        _images = self.get_images()
        
        repeated_images = (lambda lst, n: [item for _ in range(n) for item in lst])(_images, 10)
        durations = (lambda arr: [0.2] * len(arr))(repeated_images)

        clip = ImageSequenceClip(repeated_images, durations=durations)
        
        return clip.with_duration(self.duration)

    def generate_text(self):
        # Manually wrapping text cuz I don't trust moviepy
        wrapper = textwrap.TextWrapper(width=35)
        wrapped_text = "\n".join(wrapper.wrap(text=self.quote))

        txt = TextClip(
            text=wrapped_text,
            font="fonts/font.ttf",
            font_size=55,
            color="white",
            method="caption",
            size=(980, None),
            text_align="center",
            margin=(100, 150)
        ).with_position(("center", "center")).with_duration(self.duration)

        txt_author = TextClip(
            text=self.authorName,
            font="fonts/font.ttf",
            font_size=45,
            color='white',
            method='caption',
            margin=(100, 150),
            size=((1080 - 100), None),
            text_align="center"
        ).with_position(("center", 0.52), relative=True).with_duration(self.duration)

        return txt, txt_author

    def generate(self):
        bg_clip = self.generate_bg()
        text_clip, author_text_clip = self.generate_text()
        audio_clip = AudioFileClip("audio.mp3")

        final_clip = CompositeVideoClip.CompositeVideoClip([bg_clip, text_clip, author_text_clip])
        final_clip = final_clip.with_audio(audio_clip)
        final_clip.write_videofile(self.outputName, codec="libx264")