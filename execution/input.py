from captions import captions, follow_text

quote = "I suppose I love this life, in spite of my clenched fist" 
outputName = "output.mp4"

input_dict = {
  "quote": quote,
  "author": "Andrea Gibson",
  "outputName": outputName,
  "font": "fonts/font.ttf",
  "audio": "audios/10.mp3",
  "imagesPath": "./images/images2",
  "random": True,
  "bg_img_opacity": 0.2,
  "bg_img_duration": 0.25,

  "caption": f"""{quote}\n{follow_text}\n\n{captions["Andrea Gibson"]}""",
  "file_path": outputName
}