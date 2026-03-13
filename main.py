from vid_generator import VideoGenerator
from input import input_dict

vidGen = VideoGenerator(input_dict["quote"], input_dict["author"], input_dict["outputName"])

def main():
    vidGen.generate()

if __name__ == "__main__":
    main()