import base64
import os

from dotenv import load_dotenv


def load_environment_variables():
    """Load the environment variables.

    This function loads the environment variables from the .env file. If no API key for
    an LLM provider is found, it loads a demo OpenRouter API key (which has very few
    credits).
    """
    load_dotenv()  # Load the environment variables from the .env file

    # Check if the API key for an LLM provider is set
    if not os.getenv("OPENROUTER_API_KEY") and not os.getenv("OPENAI_API_KEY"):
        # Load the demo OpenRouter API key. This key has very few credits (~$0.5) and is
        # only for demonstration purposes, to make running the examples frictionless.
        # Please use your own API keys by setting them in the .env file.
        # The demo OpenRouter API key is not guaranteed to work in the future.
        # ATTENTION: You should never hard-code your API keys in your code!
        k = "c2stb3ItdjEtNjBlNjU1Y2M5ZDlhMTJlZjBmMjk0MTNiOTA2NDA0NWYzYTgzZmRhOTQxN2Yw"
        k += "NDQwMzVjYzY4NmIzZmZlN2NiOQ=="
        k = base64.b64decode(k.encode("utf-8")).decode("utf-8")
        os.environ["OPENROUTER_API_KEY"] = k
