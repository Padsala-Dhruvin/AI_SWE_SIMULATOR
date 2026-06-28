from services.llm_factory import get_llm
from prompts.reviewer_prompt import REVIEWER_PROMPT
from knowledge.knowledge_service import knowledge_service
llm = get_llm()


def reviewer_agent(state):

    knowledge = knowledge_service.search(state["idea"])
    prompt = REVIEWER_PROMPT.format(
        idea=state["idea"],
        requirements=state["requirements"],
        architecture=state["architecture"],
        backend_design=state["backend_design"],
        qa_report=state["qa_report"],
    )
    response = llm.invoke(prompt)

    state["review_report"] = response.content

    return state