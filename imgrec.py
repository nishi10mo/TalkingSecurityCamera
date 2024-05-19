
import io
import os
from google.cloud import vision

# 画像認識
client = vision.ImageAnnotatorClient()
file_name = os.path.abspath('pic.jpg')
with io.open(file_name, 'rb') as image_file:
  content = image_file.read()

image = vision.Image(content=content)

response = client.label_detection(image=image)
labels = response.label_annotation

for label in labels:
  print(label.description)
  if "People" in label.description or "Human" in label.description:
    os.system("./aquestalkpi/AquesTalkPi '防犯カメラが作動しています' | aplay")
