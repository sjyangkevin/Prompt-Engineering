from models.language_model import LanguageModel
from utils import load_prompt, generate_input

model = LanguageModel()

if __name__ == "__main__":

    prompt      = load_prompt("prompts/zero_shot_sentiment.txt")
    instruction = "Text: I really like the new design of your website!"

    response = model.predict(
        prompt=generate_input(prompt=prompt, instruction=instruction)
    )

    print(response)