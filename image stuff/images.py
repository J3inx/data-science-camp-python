from PIL import Image
import requests
from io import BytesIO
import CustomViewer

answer = input("1 for flight reacts car meme, 2 for gubby gif, 3 for you aight white boy")

if answer.lower() in ['1']:
     response = requests.get("https://preview.redd.it/the-flightreacts-in-a-shoe-car-image-is-from-an-actual-v0-cfq6jll3eg6f1.jpeg?width=640&crop=smart&auto=webp&s=2bda49c64024baec419f036ff33a767beafd3d95", stream=True)
     im = Image.open(response.raw)
     im.show()
if answer.lower() in ['2']:
     response = requests.get("https://i.redd.it/3jkk38mlmb3f1.gif", stream=True)
     im = Image.open(response.raw)
     im.show()
if answer.lower() in ['3']:
     response = requests.get("https://i.redd.it/0gt307o7olr91.jpg", stream=True)
     im = Image.open(response.raw)
     im.show()
     