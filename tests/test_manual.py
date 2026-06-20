from agents.product_manager import product_manager_agent
from agents.architect import architect_agent

def test_flow():
    idea = "Build a food delivery app for students"

    print("\n===== STEP 1: PRODUCT MANAGER =====\n")
    requirements = product_manager_agent(idea)
    print(requirements)

    print("\n===== STEP 2: ARCHITECT =====\n")
    architecture = architect_agent(idea, requirements)
    print(architecture)

if __name__ == "__main__":
    test_flow()