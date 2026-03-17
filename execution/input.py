from captions import captions, follow_text

quote = "My being was never so low as to seek praise from some mere humans."
outputName = "output.mp4"

input_dict = {
  "quote": quote,
  "author": "Fyodor Dostoevsky",
  "outputName": outputName,
  "font": "fonts/font.ttf",
  "audio": "audios/3.mp3",
  "imagesPath": "./images/images1",
  "random": False,

  "caption": f"""{quote}\n{follow_text}\n\n{captions["Fyodor Dostoevsky"]}""",
  "file_path": outputName
}