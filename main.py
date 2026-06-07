from agents.product_manager import product_manager_agent
from agents.architect import architect_agent

idea = "Build a food delivery app for students"

requirements = product_manager_agent(idea)

architecture - architect_agent(idea, requirements)

print("\n===== REQUIREMENTS =====\n")
print(requirements)

print("\n===== ARCHITECTURE =====\n")
print(architecture)