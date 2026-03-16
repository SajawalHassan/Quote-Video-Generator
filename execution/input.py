from captions import captions, follow_text

quote = "Man is sometimes extraordinarily, passionately, in love with suffering."

input_dict = {
  "quote": quote,
  "author": "Fyodor Dostoevsky",
  "outputName": "output.mp4",
  "font": "fonts/font.ttf",
  "audio": "audios/3.mp3",
  "imagesPath": "./images/images1",
  "random": True,

  "caption": f"""{quote}\n{follow_text}\n\n{captions["Fyodor Dostoevsky"]}""",
  "file_path": "./output.mp4"
}