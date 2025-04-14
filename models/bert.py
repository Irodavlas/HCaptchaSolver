from transformers import BertTokenizer, BertForSequenceClassification
import torch

class NewYesNoPredictor:
    def __init__(self, model_path="tuned/bert-yesno-model", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = BertTokenizer.from_pretrained(model_path)
        self.model = BertForSequenceClassification.from_pretrained(model_path)
        self.model.to(self.device)
        self.model.eval()
        self.label_map = {0: "no", 1: "yes"}

    def predict(self, question):
        inputs = self.tokenizer(
            question,
            return_tensors="pt",
            truncation=True,
            padding="max_length",
            max_length=64
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predicted_class = torch.argmax(logits, dim=1).item()
            return self.label_map[predicted_class]
