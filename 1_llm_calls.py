from lightlang.llms.llm import LLM
from lightlang.types import ChatMessage

from shared.settings import MODEL, PROVIDER

# Initialize LLM with the model specified in .env (or default) and set the temperature
llm = LLM(provider=PROVIDER, model=MODEL, temperature=0.8)
print(f"Using model '{MODEL}' and provider '{PROVIDER}'\n")

# System message, followed by a user prompt
messages: list[ChatMessage] = [
    dict(role="system", content="You are an expert at writing very funny stories."),
    dict(role="user", content="Start a story about a coding duck, just one sentence."),
]

# Stream the response
for chunk in llm.stream(messages):
    if chunk.content:
        print(chunk.content, end="", flush=True)  # Flush the buffer to print immediately

# Add the response and a new user message to the chat history
messages += [
    dict(role="assistant", content=llm.stream_content),
    dict(role="user", content="Continue with the next sentence."),
]

# Get a new response (we could also stream it here)
response = llm.invoke(messages)
print(response.content)
