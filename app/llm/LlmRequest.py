from pydantic import BaseModel, Field, root_validator
from typing import Optional
import os
class LlmRequest(BaseModel):
    prompt: Optional[str] = Field(None, exclude=True)
    event: str

    @root_validator(pre=True)
    def construct_prompt(cls, values):
        event = values.get("event")
        print(f'lets construct prompt from the event: {event}')
        if event:
            try:
                current_dir = os.getcwd()
                print(f"Current directory: {current_dir}")

                with open("app/llm/system_prompt.txt", "r") as file:
                    system_prompt = file.read()
                values['prompt'] = f"{system_prompt}{event}"
            except FileNotFoundError:
                raise ValueError("Text file not found")
        return values
    
class LlmModel(BaseModel):
    llm_model: str