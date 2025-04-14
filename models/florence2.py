from transformers import AutoProcessor, AutoModelForCausalLM
import torch 
from PIL import Image
from models import utils

class NewFlorence2Model:

    def __init__(self, model="microsoft/Florence-2-base"):
        print(f"loading {model}")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = AutoModelForCausalLM.from_pretrained(model,torch_dtype=torch.float16, trust_remote_code=True).to(self.device)
        self.processor = AutoProcessor.from_pretrained(model,  trust_remote_code=True)

    def predict_caption(self, image_path) -> str:
        """ process the image and return the description of input image"""
        
        print(f"start captioning")
        image = Image.open(image_path)
        prompt = "<CAPTION>"
        
        inputs = self.processor(text=prompt, images=image, return_tensors="pt").to(self.device, torch.float16)
        generated_ids = self.model.generate(
        input_ids=inputs["input_ids"],
        pixel_values=inputs["pixel_values"],
        max_new_tokens=1024,
        num_beams=3
        )
        generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
        caption = self.processor.post_process_generation(generated_text, task=prompt, image_size=(image.width, image.height))
        print(caption)
        return caption['<CAPTION>']
    def predict_label(self, image_path)-> str:
        """ process the image and return label of input image"""
        image = Image.open(image_path)
        prompt = '<>'
        inputs = self.processor(text=prompt, images=image, return_tensors="pt").to(self.device, torch.float16)
        generated_ids = self.model.generate(
        input_ids=inputs["input_ids"],
        pixel_values=inputs["pixel_values"],
        max_new_tokens=1024,
        num_beams=3
        )
        generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
        caption = self.processor.post_process_generation(generated_text, task=prompt, image_size=(image.width, image.height))
        print(caption)
        result = utils.get_first_word(caption['<>'])
        return result

        
        
