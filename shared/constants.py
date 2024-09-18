import os

from dotenv import load_dotenv

load_dotenv()  # Load the environment variables from the .env file

DEFAULT_FREE_MODEL = "mistralai/mistral-7b-instruct:free"
PROVIDER = os.getenv("PROVIDER", "openrouter")
MODEL = os.getenv("MODEL", DEFAULT_FREE_MODEL)

# Check if the API key for an LLM provider is set
if not os.getenv("OPENROUTER_API_KEY"):
    # Hardcode the demo OpenRouter API key to make running the examples frictionless. 
    # It has only a tiny amount of credits. Still, don't do this in your own code! :)
    os.environ["OPENROUTER_API_KEY"] = (
        "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"
    )

