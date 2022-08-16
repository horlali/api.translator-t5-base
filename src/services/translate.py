"""
This modules downloads and save the models when the application is started
It is also houses the translator service function use for translating text
to predefined languages
"""
from transformers import T5ForConditionalGeneration, T5Tokenizer

from src.model import MODEL_PATH
from src.schemas.translate import TranslationItem

tokenizer = T5Tokenizer.from_pretrained("t5-base", model_max_length=5120)
model = T5ForConditionalGeneration.from_pretrained("t5-base")

tokenizer.save_pretrained(MODEL_PATH)
model.save_pretrained(MODEL_PATH)


def translator(translation_item: TranslationItem) -> str:
    """Translate text from one language to another"""

    input_ids = tokenizer(
        f"translate {translation_item.source_language} to {translation_item.destination_language}: {translation_item.text}",  # noqa: E501
        return_tensors="pt",
    ).input_ids

    outputs = model.generate(input_ids, max_new_tokens=5120)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
