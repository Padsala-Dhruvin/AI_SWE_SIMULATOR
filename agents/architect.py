from services.llm_factory import get_llm

llm = get_llm()

def architect_agent(state):
    prompt = f""" you are a Senior software architect. Your task is to design the architecture for the following idea: {state['idea']}
    requirements: {state['requirements']}
    create :
    1.Architecture
    2.Technology stack
    3.Database design 
    Returen the structured output"""
    
    response = llm.invoke(prompt)
    state["architecture"] = response.content
    return state