from services.llm_factory import get_llm

llm = get_llm()

def qa_agent(state):

    prompt = f"""
    You are a Senior QA Engineer.

    Project Idea:
    {state["idea"]}

    Requirements:
    {state["requirements"]}

    Architecture:
    {state["architecture"]}

    Backend Design:
    {state["backend_design"]}

    Generate:

    1. Functional Test Cases
    2. Edge Cases
    3. Security Tests
    4. Performance Tests
    5. Major Risks

    Return structured output.
    """

    response = llm.invoke(prompt)

    state["qa_report"] = response.content

    return state