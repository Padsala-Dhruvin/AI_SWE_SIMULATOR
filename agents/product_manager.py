from services.llm_factory import get_llm    
from schemas.requirements import RequirementOutput
llm = get_llm()

structured_llm = llm.with_structured_output(
RequirementOutput
)


def product_manager_agent(state):
    idea = state["idea"]
    
    prompt = f""" you are a  Senior product manager. Your task is to gather requirements for the following idea: {idea}
    Generate the following:
    1.Functional requirements
    2.Non-functional requirements
    3.User stories 
    
    Returen the structured output"""
    
    result = structured_llm.invoke(prompt)
    state["requirements"] = result.model_dump() if hasattr(result, "model_dump") else result
    return state