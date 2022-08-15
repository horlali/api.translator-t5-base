from enum import Enum
from transformers import T5Tokenizer, T5ForConditionalGeneration

from src.model import MODEL_PATH


text = """You’ll find interesting articles to read on topics like how 
to stop procrastinating as well as personal 
recommendations like my list of the best books to read 
and my minimalist travel guide. Ready to dive in? You 
can use the categories below to browse my best articles.
This page shares my best articles to read on topics like 
health, happiness, creativity, productivity and more. The 
central question that drives my work is, “How can we live 
better?” To answer that question, I like to write about 
science-based ways to solve practical problems."""

text2 = "How are you?"


class Language(Enum):
    EN = "English"
    FR = "French"
    DE = "German"
    RO = "Romanian"


tokenizer = T5Tokenizer.from_pretrained("t5-base", model_max_length=5120)
model = T5ForConditionalGeneration.from_pretrained("t5-base")

tokenizer.save_pretrained(MODEL_PATH)
model.save_pretrained(MODEL_PATH)

input_ids = tokenizer(
    f"translate {Language.EN.value} to {Language.FR.value}: {text}",
    return_tensors="pt",
).input_ids

outputs = model.generate(input_ids, max_new_tokens=5120)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
