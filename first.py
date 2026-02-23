from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  # pip install transformers and pip install torch
from flask import Flask, request, jsonify  # pip install flask

application = Flask(__name__)

# Load the model and tokenizer
model_name = "Meher2006/english-to-telugu-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Function to translate text
def translate(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@application.route("/user-text-translate", methods=["POST"])
def translation_api():
    sentence = request.json["sentence"]
    translated_text = translate(sentence)
    response_json = {
        "original_text": sentence,
        "translated_text": translated_text
    }
    return jsonify(response_json)

if __name__ == "__main__":
    application.run()