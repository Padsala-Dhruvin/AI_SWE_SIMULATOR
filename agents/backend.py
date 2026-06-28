from services.llm_factory import get_llm
from prompts.backend_prompt import BACKEND_PROMPT
from knowledge.knowledge_service import knowledge_service
llm = get_llm()

def backend_agent(state):
    knowledge = knowledge_service.search(state["idea"])
    
    prompt = BACKEND_PROMPT.format(
        idea=state["idea"],
        requirements=state["requirements"],
        architecture=state["architecture"],
    )
    response = llm.invoke(prompt)
    state["backend_design"] = response.content
    return state