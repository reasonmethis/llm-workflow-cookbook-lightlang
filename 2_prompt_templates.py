import random

from lightlang.llms.llm import LLM
from lightlang.prompts.prompt_template import PromptTemplate

from shared.settings import MODEL, PROVIDER

# Define the model config. Possible parameters are described in the API documentation:
#     - for OpenAI: https://platform.openai.com/docs/api-reference/chat/create)
#     - for OpenRouter: https://openrouter.ai/docs/parameters
#     - for OpenRouter, by model: https://openrouter.ai/docs/parameters-api
model_config = {"temperature": 0.9, "stop": "\n"}

# Initialize the LLM with the model specified in .env (or default) and above settings
llm = LLM(provider=PROVIDER, model=MODEL, model_config=model_config)
print(f"Using model '{MODEL}' and provider '{PROVIDER}'\n")

# Define a prompt template with placeholders
template = PromptTemplate("Write a one-liner stand-up comedy joke about a {adjective} {noun}")

# Dynamically substitute the placeholders
adjective = random.choice(["huge", "tiny", "sleepy", "hungry", "squishy", "fluffy"])
noun = random.choice(["duck", "dog", "dodo", "dolphin", "dinosaur", "donkey"])
prompt = template.format(adjective=adjective, noun=noun)

# Invoke the LLM with the dynamically generated prompt
print("USER:", prompt)
print("AI:", llm.invoke(prompt).content)
