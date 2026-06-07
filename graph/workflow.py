from langgraph.graph import StateGraph
from langgaph.graph import END
from graph.state import PriojectState
from agents.product_manager import product_manager_agent
from agents.architect import architect_agent

workflow = StateGraph(PriojectState)

workflow.add_node("product_manager", product_manager_agent)
workflow.add_node("architect", architect_agent)

workflow.set_entry_point("product_manager")
workflow.add_edge("product_manager", "architect")
workflow.add_edge("architect", END)

app = workflow.compile()