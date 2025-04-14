import requests
import os
from PIL import Image
url = "http://localhost:4000/"
#craft a 9 image challenge

input_dir = "../captcha_examples/yesno/"
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".png"):
        full_path = os.path.join(input_dir, filename)
        try:
            with Image.open(full_path) as img:
                rgb_img = img.convert("RGB")  # Optional: to ensure consistent format
                rgb_img.save(full_path, format="PNG")  # Overwrite in real PNG format
                print(f"Converted: {filename}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
data = dict()
for i in range(1,10):
    data[i] = os.path.join("captcha_examples/yesno/", f"{i}.png")
data[10] = os.path.join("captcha_examples/yesno/", "prompt.png") 
numbers_body = {}
yesno_body = {}

print(data)
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
