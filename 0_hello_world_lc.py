# References:
#    - https://python.langchain.com/docs/tutorials/llm_chain/#using-language-models - NO OPENROUTER
#    - https://openrouter.ai/docs/frameworks#using-langchain - DOESN'T QUITE WORK AS IS
#    - Source code for langchain_openai.OpenAI
import os

from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from shared.settings import DEFAULT_FREE_MODEL  # Also loads .env

# Initialize the LLM with the free 'meta-llama/llama-3.1-8b-instruct:free' model
llm = ChatOpenAI(
    model=DEFAULT_FREE_MODEL,
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr(os.getenv("OPENROUTER_API_KEY", "")),  # Doesn't get auto-loaded from env
)

# Send a single user message to the assistant
print("USER:", msg := "Write a dad joke about ducks.")
print("AI:", llm.invoke(msg).content)
