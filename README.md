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

### 3. Install Requirements (Just `lightlang`)

```bash
pip install -r requirements.txt
```

## Usage

Each script in the root directory is a self-contained example of how to use LightLang to create a specific workflow. To run a script, simply execute it with Python:

```bash
python <script_name>.py
```

### 1. Debate Competition Workflow (Prompt Chaining)
The script [`1_prompt_chaining.py`](1_prompt_chaining.py) demonstrates how to create a workflow where prompts use the results of prior prompts. It runs a simple mock debate competition, where one agent generates a thesis, another one presents an affirmative argument, and a third one generates a rebuttal to it.

```bash
python 1_prompt_chaining.py
```

## Contributing

If you have a recipe you'd like to share, feel free to fork the repo and submit a pull request! Please ensure that your script is well-documented and follows the same structure as the existing examples.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
