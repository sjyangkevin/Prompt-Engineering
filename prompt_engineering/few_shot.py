from models.language_model import LanguageModel
from utils import load_prompt, generate_input

model = LanguageModel()

if __name__ == "__main__":

    # zero-shot
    prompt      = ""
    instruction = "Find the value of x in the equation 4x - 9 = 27."
    
    response = model.predict(
        prompt=generate_input(prompt=prompt, instruction=instruction)
    )

    print(response) # => 6, the answer should be 9.

    # few-shot, providing few examples
    prompt      = load_prompt("prompts/few_shot_reasoning.txt")
    
    response = model.predict(
        prompt=generate_input(prompt=prompt, instruction=instruction)
    )

    print(response) # => 9, it returns the right answer.

    # few-shot, but still not working
    prompt      = load_prompt("prompts/few_shot_reasoning.txt")
    instruction = "Find the value of x in the equation 8x - 8 = 8x / 2."
    
    response = model.predict(
        prompt=generate_input(prompt=prompt, instruction=instruction)
    )

    print(response) # => 0, the answer should be 2.