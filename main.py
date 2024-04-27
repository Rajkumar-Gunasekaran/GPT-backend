from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name = "gpt2-medium"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

prompt_text = "You will become a rival for me to measure my vessel against. you have that hidden potential. That is why I'm allowing you to live. For my sake."
input_ids = tokenizer.encode(prompt_text, return_tensors="pt")

output = model.generate(input_ids, max_length=150, num_return_sequences=1, temperature=0.7)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated Text:")
print(generated_text)
