import os

from dotenv import load_dotenv

load_dotenv()  # Load the environment variables from the .env file

DEFAULT_FREE_MODEL = "meta-llama/llama-3.1-8b-instruct:free"
PROVIDER = os.getenv("PROVIDER", "openrouter")
MODEL = os.getenv("MODEL", DEFAULT_FREE_MODEL)

# Check if the API key for an LLM provider is set
if not os.getenv("OPENROUTER_API_KEY"):
    # Hardcode the demo OpenRouter API key to make running the examples frictionless.
    # It has only a tiny amount of credits. Still, don't do this in your own code! :)
    os.environ["OPENROUTER_API_KEY"] = (
        "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"
    )
