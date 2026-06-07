from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
	sys.path.insert(0, str(ROOT))

from agents.product_manager import product_manager_agent

print(product_manager_agent("I want to build food delivery"))