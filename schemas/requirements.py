from pydantic import BaseModel
from typing import List

class RequirementOutput(BaseModel):
    functional_requirements: List[str]
    non_functional_requirements: List[str]
    user_stories: List[str]
    