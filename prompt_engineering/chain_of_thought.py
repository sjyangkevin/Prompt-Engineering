from models.language_model import LanguageModel
from utils import load_prompt, generate_input

model = LanguageModel()

if __name__ == "__main__":

    # few-shot, but still not working
    prompt      = load_prompt("prompts/few_shot_reasoning.txt")
    instruction = "Find the value of x in the equation 8x - 8 = 8x / 2."
    
    response = model.predict(
        prompt=generate_input(prompt=prompt, instruction=instruction)
    )

    print(response) # => 0, the answer should be 2.

    # few-shot chain-of-thought
    prompt      = load_prompt("prompts/chain_of_thought_reasoning.txt")
    instruction = "Find the value of x in the equation 8x - 8 = 8x / 2."
    
    response = model.predict(
        prompt=generate_input(prompt=prompt, instruction=instruction)
    )

    print(response) # => 2, it returns the correct answer

    # zero-shot chain-of-thought
    prompt = ""
    instruction = "Find the value of x in the equation 8x - 8 = 8x / 2. Let's think step by step."
    
    response = model.predict(
        prompt=generate_input(prompt=prompt, instruction=instruction)
    )

    print(response) # => 2, it returns the correct answer