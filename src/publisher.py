from dotenv import load_dotenv 
import base64, os, requests, uuid, json, time
from util import generate_caption

load_dotenv()

class Publisher():
    def __init__(self, caption, file_path):
        self.file_path = file_path
        self.caption = caption

    def convert_to_base64(self, file_path):
        try:
            with open(file_path, "rb") as file:
                file_content_bytes = file.read()
                
                encoded_bytes = base64.b64encode(file_content_bytes)
                encoded_string = encoded_bytes.decode('utf-8')
                
                return encoded_string

        except IOError as e:
            print(f"Error opening or reading file: {e}")
            return None

    def upload_to_github(self, file_path):
        encoded_video = self.convert_to_base64(file_path)
        
        data = {
            "message": "Uploading video via Python API",
            "content": encoded_video
        }

        headers = {
            "Authorization": f"Bearer {os.getenv("GITHUB_PAT")}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }

        file_id = uuid.uuid4()
        url = f"{os.getenv("GITHUB_REPO_PATH")}/{file_id}.mp4"

        response = requests.put(url, json=data, headers=headers)

        response_content_decoded = json.loads(response.content.decode("utf-8")) # Decode byte to dict
        return response_content_decoded["content"]["download_url"]

    def create_container(self, video_url=None, image_url=None):
        url = f"https://graph.facebook.com/v20.0/{os.getenv("BUSINESS_ACC_ID")}/media"

        if video_url:
            data = {
                "video_url": video_url,
                "caption": self.caption,
                "access_token": os.getenv("ACCESS_TOKEN"),
                "media_type": "REELS",
                "share_to_feed": True
            }
        elif image_url:
            data = {
                "image_url": image_url,
                "caption": self.caption,
                "access_token": os.getenv("ACCESS_TOKEN"),
                "media_type": "IMAGE",
            }

        response = requests.post(url, json=data)

        decoded_response = json.loads(response.content.decode("utf-8")) # Decode byte to dict

        return decoded_response["id"]

    def publish_container(self, container_id):
        url = f"https://graph.facebook.com/v20.0/{os.getenv("BUSINESS_ACC_ID")}/media_publish?creation_id={container_id}&access_token={os.getenv("ACCESS_TOKEN")}"
        response = requests.post(url)
        return response.status_code

    def check_container_status(self, container_id):
        url = f"https://graph.facebook.com/v20.0/{container_id}?fields=status_code,status&access_token={os.getenv("ACCESS_TOKEN")}"
        
        response = requests.get(url)

        response_content_decoded = json.loads(response.content.decode("utf-8")) # Decode byte to dict

        return response_content_decoded["status_code"], response_content_decoded

    def publish(self, publish_type):
        print("Uploading video to Github...")
        download_url = self.upload_to_github(self.file_path)
        print("Video uploaded!\n")
        
        print("Creating container...")
        if publish_type == "video": container_id = self.create_container(video_url=download_url)
        elif publish_type == "image": container_id = self.create_container(image_url=download_url)
        print(f"Container created with id: {container_id}\n")

        # Poll every five seconds for status
        while True:
            status, r = self.check_container_status(container_id)

            if (status == "FINISHED"):
                print("Container created!")
                break
            elif (status == "ERROR"):
                print("ERROR OCCURED")
                print(r)
                raise Exception("Error occured")
            else:
                print("Container creating...")

            time.sleep(5)

        # Publish container
        print("\nPublishing container...")
        published_status_code = self.publish_container(container_id)
        print("\n---------- Video uploaded to Instagram! ----------")
        return published_status_code

if __name__ == "__main__":
    from publisher import Publisher
    from input import input_dict
    from util import generate_caption

    caption = generate_caption(input_dict["quote"], input_dict["author"])
    vidPublisher = Publisher(caption, input_dict["file_path"])

    if input_dict["file_path"].split(".")[1] == "png":
        vidPublisher.publish(publish_type="image")
    elif input_dict["file_path"].split(".")[1] == "mp4":
        vidPublisher.publish(publish_type="video")