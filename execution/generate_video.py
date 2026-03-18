from vid_generator import VideoGenerator
from input import input_dict

if __name__ == "__main__":
    vidGen = VideoGenerator(input_dict["quote"], input_dict["author"], input_dict["outputName"],
                            input_dict["imagesPath"], input_dict["font"], input_dict["audio"], input_dict["random"],
                            input_dict["bg_img_opacity"], input_dict["bg_img_duration"])

    vidGen.generate()