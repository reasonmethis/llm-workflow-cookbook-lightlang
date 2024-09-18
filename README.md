# LightLang Cookbook.

This is a collection of example scripts that demonstrate how to easily create agentic workflows using LightLang. [LightLang](https://github.com/reasonmethis/lightlang) is a Python package for working with LLM, akin to Langchain and Llamaindex, but much more lightweight and "close-to-the-metal".

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/reasonmethis/llm-workflow-cookbook-lightlang.git
cd llm-workflow-cookbook-lightlang
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate # On Windows, run .venv\Scripts\activate instead
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables (Optional)

NOTE: The scripts will (likely) work without setting your own API key - if you don't complete this step, a demo OpenRouter API key will be used. It's set up with a tiny amount of credits, and may potentially have run out of them by the time you are reading this. You are strongly encouraged to complete this step and use your own API keys.

Copy the `.env.example` file to `.env` and fill in the values for the API key you want to use to interact with LLMs, such as your OpenAI API key, as well as other settings.

## Usage

Each script in the root directory is a self-contained example of how to use LightLang to create a specific workflow. To run a script, simply execute it with Python:

```bash
python <script_name>.py
```

### Debate Competition Workflow (Prompt Chaining)

As an illustration, currently the most advanced example is the script [`3_prompt_chaining.py`](3_prompt_chaining.py), which demonstrates how to create a workflow where prompts use the results of prior prompts. It runs a simple mock debate competition, where one agent generates a thesis, another one presents an affirmative argument, and a third one generates a rebuttal to it.

```bash
python 3_prompt_chaining.py
```

## Contributing

If you have a recipe you'd like to share, feel free to fork the repo and submit a pull request! Please ensure that your script is well-documented and follows the same structure as the existing examples.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
