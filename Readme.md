# 🎬 Quote Video Generator

A simple and customizable **quote video generator** that creates MP4 videos from configurable quote data.

<p align="center">
  <img src="example.gif" alt="Demo" width="300" />
</p>
(The background looks cursed because of being converted into a GIF, the produced video will not have this problem)

---

## Overview

This project generates a video as shown in the above GIF of 9:16 aspect ratio and automatically publishes it to Instagram using Github as a data storage. In `execution/input.py` you can edit all parameters of the video, they are:

Video generation:

- `quote`: The actual quote
- `author`: Author of the quote
- `outputName`: The name of the generated video
- `font`: The font to be used. Existing fonts present in `fonts/`
- `audio`: The background audio to be used. Existing audios present in `audios/`
- `imagesPath`: Path to the image folder to be used. Will use all files in that folders sequentially unless `random=True`
- `random`: Whether to choose the images at random from `images/`. Will search all subfolders inside `images/`

Video publishment:

- `caption`: Contains quote, a text asking for a follow, and a description about the author. The follow text and description can be edited in the `captions.py` folder
- `file_path`: The file path to be published to Instagram

## Usage

### Video Generation

All libraries used and required are present in the `requirements.txt` file. Run the following commands to setup your environment:

```Py
python -m venv venv
source venv/source/activate # Or venv\Scripts\activate for windows
pip install -r requirements.txt
```

Once the environment is setup, configure the parameters in `execution/input.py` and run the `execution/generate_video.py` file to generate the video.

### Video Publishing

To publish the video, you'll have to get the following things and put them in your `.env`. An example .env file is present: `.env.example`. The parameters required are:

- `ACCESS_TOKEN`: The facebook GraphAPI access token
- `BUSINESS_ACC_ID`: The business instagram account id
- `GITHUB_PAT`: Github Personal Access Token
- `GITHUB_REPO_PATH`: The github api link to the repository where the videos are stored.

To get the access token and business account id, follow this Youtube video: https://www.youtube.com/watch?v=BuF9g9_QC04. I doubt anyone can actually get it from just the documentation, it's rubbish.

Github is used because the Facebook GraphAPI, as far as I can tell from whatever the hell their documentation is, doesn't allow direct uploads from the API. So you need to store it elsewhere and give them the link. Github I found to be a free option, but its sketchy at times. If you're willing to pay a little, Uploadcare is better.

## Contributing

The actual code is to be found in the `execution/` folder. Its folder structure is as follows:

- `vid_generator.py`: The `VideoGenerator` class
- `vid_publisher.py`: The `VideoPublisher` class
- `generate_video.py`: Uses the class `VideoGenerator` with the input from `input.py` to generate the video.
- `publish_video.py`: Uses the class `VideoPublisher` with the input from `input.py` to publish the video.
- `captions.py`: Captions that can be used in publishing
- `input.py`: Contains a dict `input_dict` containing all parameters mentioned above.

As a developer, you'll mainly be working in the `vid_generator.py` and `vid_publisher.py` files. I got exams and am too lazy to implement tests, so just run edge cases yourself.

### Future changes

Here are some features you can contribute on implementing:

- [ ] Hook up the quotes to some API
- [ ] Use some AI to choose which audios, images, and fonts would be best for a quote
- [ ] Add more images. They can be of any size since the `VideoGenerator` class does resize them, but it sometimes bugs out.
- [ ] On that topic, actually fixing the `crop_image` function inside the `VideoGenerator` would be great lmao.
- [ ] Add different formats. Currently its just image shuffling. Other quotes formats involving fading transitions, pictures for posts, or other variations.

## License

This project has the MIT License. See `LICENSE` for more info.

## Author

I made this because I drank coffee at 2am and didn't want to study Physics xD.

Check out my website: https://sajawalhassan.vercel.app
