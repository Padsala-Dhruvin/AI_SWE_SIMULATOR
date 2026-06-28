from agents.product_manager import product_manager_agent

state = {
"idea": "Build a food delivery app",
"requirements": {},
"architecture": "",
"backend_design": "",
"qa_report": "",
"review_report": ""
}

result = product_manager_agent(state)

print(result["requirements"])
