from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

model_name = "gpt2-medium"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt_text = request.form.get('prompt', '')
    if not prompt_text:
        return jsonify({'error': 'No prompt provided'}), 400

    input_ids = tokenizer.encode(prompt_text, return_tensors="pt")

    output = model.generate(input_ids, max_length=150, num_return_sequences=1, temperature=0.7)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
