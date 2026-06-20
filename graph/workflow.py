from langgraph.graph import StateGraph
from langgaph.graph import END
from graph.state import PriojectState
from agents.product_manager import product_manager_agent
from agents.architect import architect_agent
from agents.backend import backend_agent
from agents.qa import qa_agent
from agents.reviewer import reviewer_agent

workflow = StateGraph(PriojectState)

workflow.add_node("product_manager", product_manager_agent)
workflow.add_node("architect", architect_agent)
workflow.add_node("backend", backend_agent)
workflow.add_node("qa",qa_agent)
workflow.add_node(
    "reviewer",
    reviewer_agent
)


workflow.set_entry_point("product_manager")
workflow.add_edge("product_manager", "architect")
workflow.add_edge("architect", "backend")
workflow.add_edge("backend", "qa")
workflow.add_edge("qa", "reviewer")
workflow.add_edge("reviewer", END)  

app = workflow.compile()