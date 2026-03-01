from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  # pip install transformers and pip install torch
from flask import Flask, request, jsonify, render_template  # pip install flask

application = Flask(__name__)

# English to Telugu Load the model and tokenizer
eng_to_tel_model_name = "Meher2006/english-to-telugu-model"
eng_to_tel_tokenizer = AutoTokenizer.from_pretrained(eng_to_tel_model_name)
eng_to_tel_model = AutoModelForSeq2SeqLM.from_pretrained(eng_to_tel_model_name)

# English to Hindi Loding
eng_to_hin_model_name = "Helsinki-NLP/opus-mt-en-hi"
eng_to_hin_tokenizer = AutoTokenizer.from_pretrained(eng_to_hin_model_name)
eng_to_hin_model = AutoModelForSeq2SeqLM.from_pretrained(eng_to_hin_model_name)


# Function to translate text from English to Telugu
def translate_eng_to_tel(text):
    inputs = eng_to_tel_tokenizer(text, return_tensors="pt")
    outputs = eng_to_tel_model.generate(**inputs)
    return eng_to_tel_tokenizer.decode(outputs[0], skip_special_tokens=True)

@application.route("/english-to-telugu", methods=["POST"])
def english_to_telugu_api():
    sentence = request.json["sentence"]
    translated_text = translate_eng_to_tel(sentence)
    response_json = {
        "original_text": sentence,
        "translated_text": translated_text
    }
    return jsonify(response_json)



@application.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    application.run()