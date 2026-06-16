from graph.workflow import app

initial_state = {
    "idea": "Build a food delivery application for university students",
    "requirements": "",
    "architecture": "",
    "backend_design": "",
    "qa_report": "",
    "review_report": ""
}

result = app.invoke(initial_state)

print("\n===== REQUIREMENTS =====\n")
print(result["requirements"])

print("\n===== ARCHITECTURE =====\n")
print(result["architecture"])

print("\n===== BACKEND DESIGN =====\n")
print(result["backend_design"])

print("\n===== QA REPORT =====\n")
print(result["qa_report"])