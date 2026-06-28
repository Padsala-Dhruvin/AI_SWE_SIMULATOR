from services.llm_factory import get_llm
from schemas.requirements import RequirementOutput
from prompts.pm_prompt import PM_PROMPT

llm = get_llm()

structured_llm = llm.with_structured_output(
RequirementOutput
)


def product_manager_agent(state):
    idea = state["idea"]

    prompt = PM_PROMPT.format(idea=idea)
    
    result = structured_llm.invoke(prompt)
    state["requirements"] = result.model_dump() if hasattr(result, "model_dump") else result
    return state