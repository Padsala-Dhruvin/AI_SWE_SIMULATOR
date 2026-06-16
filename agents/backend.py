from services.llm_factory import get_llm

llm = get_llm()

def backend_agent(state):
    prompt = f""" you are a Senior backend developer. Your task is to design the backend for the following idea: {state['idea']}
    Requirements: {state['requirements']}
    Architecture: {state['architecture']}
    create :
    1.REST API design
    2.Database schema
    3.Authentication Strategy
    4.Service Structure
    Returen the structured output"""
    
    response = llm.invoke(prompt)
    state["backend_design"] = response.content
    return state