from PIL import Image
import requests
from io import BytesIO
import CustomViewer
answer = input("who's the goat?")
if answer.lower() in ['bron', 'lebron']:
        print("your damn right")
else:
        print("wrong it's LEBRONNNN")
        response = requests.get("https://cdn.nba.com/headshots/nba/latest/1040x760/2544.png", stream=True)
        im = Image.open(response.raw)
        im.show()