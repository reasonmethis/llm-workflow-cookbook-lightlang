from lightlang.llms.llm import LLM

from shared.constants import DEFAULT_FREE_MODEL

# Initialize the LLM for with the free 'mistralai/mistral-7b-instruct:free' model
llm = LLM(provider="openrouter", model=DEFAULT_FREE_MODEL)

# Send a single user message to the assistant
print("USER:", msg := "Write a dad joke about ducks.")
response = llm.invoke(msg)
print("AI:", response.content)
