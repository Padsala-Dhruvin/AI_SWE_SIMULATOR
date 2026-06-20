from services.llm_factory import get_llm

llm = get_llm()


def reviewer_agent(state):

    prompt = f"""
    You are a Principal Software Engineering Reviewer. IMPORTANT: You are NOT allowed to generate new requirements, architectures, APIs, or implementation plans. Your ONLY responsibility is to REVIEW and EVALUATE the outputs produced by other agents.

    PROJECT IDEA:
    {state["idea"]}

    REQUIREMENTS:
    {state["requirements"]}

    ARCHITECTURE:
    {state["architecture"]}

    BACKEND DESIGN:
    {state["backend_design"]}

    QA REPORT:
    {state["qa_report"]}

    Perform the following review:

    1. Check requirement coverage.
    2. Find missing features.
    3. Find architecture inconsistencies.
    4. Find backend design issues.
    5. Identify security concerns.
    6. Identify scalability concerns.
    7. Provide improvement recommendations.

    Return structured output with:

    - Strengths
    - Issues Found
    - Recommendations
    - Overall Assessment
    """

    response = llm.invoke(prompt)

    state["review_report"] = response.content

    return state