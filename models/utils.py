import cv2
import os
import numpy as np
import requests
import io
from io import BytesIO
from PIL import Image
import aiohttp
import re
import asyncio
import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

TARGET_SIZE = (128, 128)
OUTPUT_DIR = "images/"

def processImage(image: np.ndarray, image_name: str) -> str:
    # Apply Non-Local Means Denoising (better for heavy noise)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    img = cv2.fastNlMeansDenoisingColored(image, None, h=10, templateWindowSize=7, searchWindowSize=21)
    # Apply Gaussian Blur to smooth out remaining noise
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # Resize image using high-quality interpolation
    img = cv2.resize(img, TARGET_SIZE, interpolation=cv2.INTER_LANCZOS4)
    # Convert to PNG and save
    new_path = os.path.join(OUTPUT_DIR, os.path.splitext(image_name)[0] + ".png")
    cv2.imwrite(new_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
    return new_path

def downloadImage(url : str) -> str:
    response = requests.get(url)
    image_name = url.split("/")[-1].replace(".jpeg", "")
    img_in_mem = io.BytesIO(response.content)
    image_path = processImage(np.frombuffer(img_in_mem.getvalue(), dtype=np.uint8),image_name)
    return image_path





def Download_BytesIO(url):
    response = requests.get(url)
    response.raise_for_status()  

    filename = url.split("/")[-1]
    image_path = os.path.join("immagini", filename)

    image = Image.open(BytesIO(response.content))
    image.save(image_path)

    return image_path  # Restituisce il percorso dell'immagine salvata


async def fetch_images(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            img_bytes = await response.read()

            filename = url.split("/")[-1].replace(".jpeg", "")
            image_path = os.path.join("immagini", filename)

            image = Image.open(BytesIO(img_bytes))
            image.save(image_path)
            return image_path  # Restituisce il percorso dell'immagine salvata
        else:
            print(f"Errore nel download: {url}")
            return None

async def Download_aiohttp(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_images(session, url) for url in urls]
        image_paths = await asyncio.gather(*tasks)
        return image_paths  # Restituisce una lista dei percorsi delle immagini salvate
'''
def parse_number(stringa : str) -> int:
    for word in stringa.split(" "):
        try:
           number = int(word)
           return number 
        except ValueError: #if use TypeError it wont work
            continue
    return 0 
'''
def parse_number(stringa):
    match = re.search(r'\d+', stringa)
    return int(match.group()) if match else 0
def get_first_noun(caption: str) -> str:
    """
    Uses spaCy to extract the first noun from a caption string.
    Example: "a red apple with a leaf" → "apple"
    """
    doc = nlp(caption)
    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN']:
            return token.text.lower()
    return ""
