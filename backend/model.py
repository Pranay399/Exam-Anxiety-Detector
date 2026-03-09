import torch
from transformers import BertTokenizer, BertForSequenceClassification
import os

MODEL_PATH = "../models/saved_model"

class AnxietyModel:
    def __init__(self):
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.tokenizer = None
        self.model = None
        self.label_map = {0: "Low", 1: "Moderate", 2: "High"}
        self.load_model()
        
    def load_model(self):
        print(f"Loading model from {MODEL_PATH}...")
        try:
            if os.path.exists(MODEL_PATH):
                self.tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
                self.model = BertForSequenceClassification.from_pretrained(MODEL_PATH)
                self.model = self.model.to(self.device)
                self.model.eval()
                print("Model loaded successfully.")
            else:
                print("WARNING: Model path not found. Using untraiend base model for demonstration.")
                # Fallback to untrained base model just for demonstration
                self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
                self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)
                self.model = self.model.to(self.device)
                self.model.eval()
        except Exception as e:
            print(f"Error loading model: {e}")
            
    def predict(self, text: str):
        if not self.model or not self.tokenizer:
            return {"error": "Model not loaded properly."}
            
        encoding = self.tokenizer(
            text,
            add_special_tokens=True,
            max_length=128,
            return_token_type_ids=False,
            padding='max_length',
            return_attention_mask=True,
            return_tensors='pt',
            truncation=True
        )
        
        input_ids = encoding['input_ids'].to(self.device)
        attention_mask = encoding['attention_mask'].to(self.device)
        
        with torch.no_grad():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            probs = torch.nn.functional.softmax(logits, dim=1)
            confidence, predicted_class = torch.max(probs, dim=1)
            
        label_id = predicted_class.item()
        confidence_score = confidence.item()
        
        return {
            "prediction_id": label_id,
            "prediction_label": self.label_map.get(label_id, "Unknown"),
            "confidence": round(confidence_score * 100, 2)
        }

# Singleton instance
anxiety_model = AnxietyModel()
