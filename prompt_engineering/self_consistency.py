from typing import List
import json

from models.language_model import LanguageModel
from utils import load_prompt, generate_input

LABEL_MAP = {
    0: "REGULAR",
    1: "SPAM"
}

def get_result(json_string: str) -> int:
    return json.loads(json_string)

def take_majority_vote(voting: List) -> int:
    """
    Boyer-Moore Voting Algorithm
    """
    count     = 0
    candidate = None

    for ans in voting:
        if count == 0:
            candidate = ans
        count += (1 if ans == candidate else -1)
    
    return candidate

model = LanguageModel()

if __name__ == "__main__":

    NUM_ATTEMPTS = 3
    candidates   = []
    
    prompt      = load_prompt("prompts/self_consistency_classification.txt")
    instruction = """
        Hello,

        We've updated our login credential policy. 
        Please confirm your account by logging into Google Docs via the link.

        IT Department
    """

    for i in range(NUM_ATTEMPTS):

        # set temperature to higher value, to introduce more randomness in
        # the response. Otherwise, you're likely to get almost deterministic
        # responses when you send multiple requests.
        response = model.predict(
            prompt=generate_input(prompt=prompt, instruction=instruction),
            temperature=0.4,
            top_k=40,
        )

        print(response)

        try:
            # DON'T expect the LLM will ALWAYS provide the desired response.
            result = get_result(response)
            candidates.append(result.get('class'))
        except Exception as e:
            print("response:\n", response)
            print("ERROR:\n", e)


    final_result = take_majority_vote(voting=candidates)

    print("The email is:", LABEL_MAP[final_result])