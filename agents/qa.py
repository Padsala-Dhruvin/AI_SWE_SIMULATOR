from services.llm_factory import get_llm
from prompts.qa_prompt import QA_PROMPT
from knowledge.knowledge_service import knowledge_service
llm = get_llm()

def qa_agent(state):

    knowledge = knowledge_service.search(state["idea"])
    prompt = QA_PROMPT.format(
        knowledge=knowledge,
        idea=state["idea"],
        requirements=state["requirements"],
        backend_design=state["backend_design"],
    )

    response = llm.invoke(prompt)

    state["qa_report"] = response.content

    return state