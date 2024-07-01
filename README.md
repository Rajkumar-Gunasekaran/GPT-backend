# GPT-backend
This project is a Flask-based web application that uses a GPT-2 model to generate text. The GPT-2 model is a powerful language model provided by the transformers library from Hugging Face.

How It Works
Setup: We import necessary libraries, including Flask for the web application and GPT-2 model/tokenizer from Hugging Face's transformers.
Model Initialization: We initialize the GPT-2 model and tokenizer.
API Endpoint: We create a /generate POST endpoint where users can send a text prompt.
Text Generation: The endpoint takes the input prompt, uses GPT-2 to generate a continuation of the text, and returns the generated text as a JSON response.

Endpoint Details
/generate (POST)
Request: Send a form data with a key prompt containing the text prompt.
Response: Returns a JSON object with the generated text or an error message if no prompt is provided.

Requirements:
pytorch
tensorflow
flask
transformers
