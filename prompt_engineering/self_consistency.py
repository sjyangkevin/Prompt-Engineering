from typing import List

from models.language_model import LanguageModel
from utils import load_prompt, generate_input

def majority_vote(voting: List):
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
    pass