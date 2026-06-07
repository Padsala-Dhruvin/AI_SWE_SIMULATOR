from services.llm_factory import get_llm    
llm = get_llm()

def product_manager_agent(state):
    idea = state["idea"]
    
    prompt = f""" you are a  Senior product manager. Your task is to gather requirements for the following idea: {idea}
    Generate the following:
    1.Functional requirements
    2.Non-functional requirements
    3.User stories 
    
    Returen the structured output"""
    
    response = llm.invoke(prompt)
    state["requirements"] = response.content
    return state