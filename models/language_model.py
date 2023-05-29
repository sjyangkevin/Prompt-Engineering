import os

from google.cloud import aiplatform
from vertexai.preview.language_models import (
    TextGenerationModel, 
    TextGenerationResponse,
)

class LanguageModel:
    
    def __init__(self, model_name: str = "text-bison@001") -> None:
        
        self.project: str  = os.environ.get('PROJECT')
        self.location: str = os.environ.get('LOCATION')

        aiplatform.init(project=self.project, location=self.location)

        self.model: TextGenerationModel = TextGenerationModel \
            .from_pretrained(model_name=model_name)

    def predict(
        self,
        prompt: str,
        temperature: float = 0.0,
        max_output_tokens: int = 256,
        top_k: int = 1,
        top_p: float = 0.8,
    ) -> TextGenerationResponse:
        
        print(f"prompt:\n{prompt}")
        
        response: TextGenerationResponse = self.model.predict(
            prompt=prompt,
            max_output_tokens=max_output_tokens,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
        )

        return response
