# BINARY WIZARDS PROTOTYPE SIH2023

### Translation Prototype using Helsinki-NLP/opus-mt-en-hi
This prototype is a simple web application that uses the "Helsinki-NLP/opus-mt-en-hi" open-source model to translate text from English to Hindi. The prototype consists of a frontend UI that allows users to input text and a backend API that processes the text using the pre-trained T5 model and returns the translated text as a response.
### How it works
The prototype uses the following technologies:
- HTML, CSS, and JavaScript for the frontend UI.
- Flask, a Python web framework, for the backend API.
- Transformers, a Python library for natural language processing, for the pre-trained T5 model.

When a user inputs text in English, the frontend UI sends an HTTP POST request to the backend API with the text as a parameter. The backend API processes the text using the pre-trained T5 model and returns the translated text as a response. The frontend UI then displays the translated text to the user.

-----------
### Getting started
To run the prototype, you will need to install the following dependencies:
- Python 3.x
- Flask
- Transformers
You can install Flask and Transformers using pip:
```
pip install flask transformers
```

Once you have installed the dependencies, you can run the prototype by running the following command in the terminal:
```
python project.py
```

This will start the Flask development server on http://localhost:5000. You can then open the frontend UI in your web browser by navigating to http://localhost:5000.

----------------------
### Credits
The "Helsinki-NLP/opus-mt-en-hi" open-source model was developed by the Language Technology Research Group at the University of Helsinki. You can find more information about the model and related projects on their GitHub page: https://github.com/Helsinki-NLP.