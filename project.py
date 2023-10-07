# Load model directly
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi")
# model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-hi")

# input_text = "How are you?"
# input_ids = tokenizer(input_text, return_tensors="pt").input_ids

# outputs = model.generate(input_ids)
# translated_text=tokenizer.decode(outputs[0])

# with open("translated_text.txt", "w", encoding="utf-8") as f:
#     f.write(translated_text)

from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-hi")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/translate', methods=['POST','GET'])
def translate():
    input_text = request.data.decode('utf-8')
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    translated_text = tokenizer.decode(outputs[0])
    return translated_text

if __name__ == '__main__':
    app.run(debug=True)