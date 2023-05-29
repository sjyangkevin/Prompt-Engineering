import os

def load_prompt(fpath: str) -> str:

    PROJECT_DIR = os.environ.get('PROJECT_DIR')
    
    with open(os.path.join(PROJECT_DIR, fpath), 'r') as f:
        prompt = f.read()

    return prompt

def generate_input(prompt: str, instruction: str) -> str:
    return prompt + instruction