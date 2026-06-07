from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
	sys.path.insert(0, str(ROOT))

from services.llm_factory import get_llm

llm = get_llm()

response = llm.invoke("What is the capital of France?")
print(response.content)