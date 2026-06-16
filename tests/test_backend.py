from agents.product_manager import product_manager_agent
from agents.architect import architect_agent
from agents.backend import backend_agent

state = {
    "idea": "Build a food delivery app for students",
    "requirements": "",
    "architecture": "",
    "backend_design": "",
    "qa_report": "",
    "review_report": ""
}

state = product_manager_agent(state)
state = architect_agent(state)
state = backend_agent(state)

print(state["backend_design"])