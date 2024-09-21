# Langchain-based version of the corresponding LightLang example for comparison.
# References:
#    - https://python.langchain.com/docs/how_to/chat_models_universal_init/
#    - https://python.langchain.com/docs/tutorials/llm_chain/#using-language-models - NO OPENROUTER
#    - https://openrouter.ai/docs/frameworks#using-langchain - DOESN'T QUITE WORK AS IS
#    - Source code for langchain_openai.OpenAI
import os

from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from pydantic import SecretStr

from shared.settings import MODEL, PROVIDER

# Initialize LLM with the model specified in .env (or default) and set the temperature
if PROVIDER != "openrouter":  # The init_chat_model utility is not available for OpenRouter
    llm = init_chat_model(model=MODEL, model_provider=PROVIDER, temperature=0.8)
else:
    llm = ChatOpenAI(
        model=MODEL,
        base_url="https://openrouter.ai/api/v1",
        api_key=SecretStr(os.getenv("OPENROUTER_API_KEY", "")),  # Doesn't get auto-loaded from env
    )
print(f"Using model '{MODEL}' and provider '{PROVIDER}'\n")

# System message, followed by a user prompt
messages = [
    SystemMessage(content="You are an expert at writing very funny stories."),
    HumanMessage(content= "Start a story about a coding duck, just one sentence."),
]

# Stream the response
stream_content = ""
for chunk in llm.stream(messages):
    if isinstance(chunk.content, str): # Otherwise type-checking will fail for next line
        stream_content += chunk.content
        print(chunk.content, end="", flush=True)  # Flush the buffer to print immediately

# Add the response and a new user message to the chat history
messages += [
    AIMessage(content=stream_content),
    HumanMessage(content="Continue with the next sentence."),
]

# Get a new response (we could also stream it here)
response = llm.invoke(messages)
print(response.content)
