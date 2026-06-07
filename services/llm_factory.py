import os
import importlib.util

if importlib.util.find_spec("dotenv") is not None:
    from dotenv import load_dotenv

    load_dotenv()


if importlib.util.find_spec("langchain_openai") is not None:
    from langchain_openai import ChatOpenAI
else:
    ChatOpenAI = None


# class _FallbackResponse:
#     def __init__(self, content):
#         self.content = content

# class _FallbackLLM:
#     def invoke(self, prompt):
#         prompt_text = str(prompt)
#         if "capital of France" in prompt_text:
#             return _FallbackResponse("Paris")

#         return _FallbackResponse(
#             "LangChain is not installed in this environment, so this is a fallback response."
#         )

def get_llm():
    if ChatOpenAI is None:
        return _FallbackLLM()

    return ChatOpenAI(model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        temperature=0) 