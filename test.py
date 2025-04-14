

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


tokenizer = AutoTokenizer.from_pretrained('/Users/daol/PycharmProjects/sllmproject-2025/app/Google/gemma-2-2b-it')
model = AutoModelForCausalLM.from_pretrained('/Users/daol/PycharmProjects/sllmproject-2025/app/Google/gemma-2-2b-it')

def generate_answer(input_text: str) -> str:
    input_ids = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**input_ids, max_length=512)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer
