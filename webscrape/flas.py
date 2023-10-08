from flask import Flask, render_template, jsonify, request
from bs4 import BeautifulSoup
import requests
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-hi")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-hi")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape_text', methods=['GET'])
def scrape_text():
    # Scrape the text using Beautiful Soup and requests
    url = "https://karunya.edu"  # Replace with the URL you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    input_text = soup.get_text()

    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    text_content = tokenizer.decode(outputs[0])

    return text_content

if __name__ == '__main__':
    app.run(debug=True)
