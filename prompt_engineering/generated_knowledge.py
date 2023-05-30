from vertexai.preview.language_models import TextGenerationModel

from models.language_model import LanguageModel
from utils import load_prompt

def knowledge_generation(
    model: TextGenerationModel,
    prompt: str,
) -> str:
    
    knowledge = model.predict(prompt=prompt)

    return knowledge

def predict(
    model: TextGenerationModel,
    prompt: str,
) -> str:
    
    response = model.predict(prompt=prompt)
    return response

model = LanguageModel()

if __name__ == "__main__":
    
    question="Do dolphins swim in packs because of safety?"

    # asking the question without using any knowledge
    response  = predict(
        model=model,
        prompt=question,
    )
    print(response)

    # knowledge generation
    prompt = load_prompt("prompts/generated_knowledge_qa.txt") \
        .format(question=question)
    
    knowledge = knowledge_generation(model=model, prompt=prompt)

    # knowledge integration
    prompt = """
    {knowledge}
    {question}
    """.format(knowledge=knowledge, question=question)

    response  = predict(
        model=model,
        prompt=prompt,
    )

    print(response)

    

