from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agents.product_manager import product_manager_agent
from agents.architect import architect_agent

state = {
    "idea": "Build a food delivery app for university students",
    "requirements": "",
    "architecture": "",
    "backend_design": "",
    "qa_report": "",
    "review_report": ""
}

print("\n===== PM AGENT =====\n")

state = product_manager_agent(state)

print(state["requirements"])

print("\n===== ARCHITECT AGENT =====\n")

state = architect_agent(state)

print(state["architecture"])