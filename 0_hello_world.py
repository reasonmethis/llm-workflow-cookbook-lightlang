from lightlang.llms.llm import LLM

from shared.settings import DEFAULT_FREE_MODEL  # Also loads .env

# Initialize the LLM with the free 'meta-llama/llama-3.1-8b-instruct:free' model
llm = LLM(provider="openrouter", model=DEFAULT_FREE_MODEL)

# Send a single user message to the assistant
print("USER:", msg := "Write a dad joke about ducks.")
print("AI:", llm.invoke(msg).content)
