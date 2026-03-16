from vid_publisher import VideoPublisher
from input import input_dict

vidPublisher = VideoPublisher(input_dict["caption"], input_dict["file_path"])

if __name__ == "__main__":
    vidPublisher.publish_video()