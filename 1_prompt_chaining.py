"""This example demonstrates how to chain prompts in a SequentialWorkflow.

In this example, we create a SequentialWorkflow with three prompts, which generates a \
random thesis for debating, provides the affirmative case for the thesis, and prepares a rebuttal."""

import os

from lightlang.llms.llm import LLM
from lightlang.workflows.sequential_workflow import SequentialWorkflow

from utils.load_env import load_environment_variables

# Load the environment variables and model/provider settings
load_environment_variables()
PROVIDER = os.getenv("PROVIDER", "openrouter")
MODEL = os.getenv("MODEL", "mistralai/mistral-7b-instruct:free")
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.8))

print(f"Using:\n- Model: {MODEL}\n- Provider: {PROVIDER}\n- Temperature: {TEMPERATURE}")

# Define the input data for the workflow
workflow_data = {"topic": "philosopy of mind"}  # Each task will add its output to this

# Define the first prompt
# This prompt instructs the assistant to generate a random thesis for debating.
prompt1 = """
<system>
You are a creative organizer of a debating competition.
</system>
<user>
Generate a random thesis on the topic of '{topic}' for competitors to debate. \
Respond in one sentence in the format: "Thesis: <thesis>".
</user>
"""

# Define the second prompt
# It asks the assistant to provide the affirmative case for the thesis generated in the first prompt.
prompt2 = """
<system>
You are a debate expert participating in a competition.
</system>
<user>
Provide the affirmative case for the following thesis in just one short paragraph:

{task_1_output}
</user>
"""

# Define the third prompt
# This prompt instructs the assistant to prepare a rebuttal.
# It provides both the thesis and the affirmative case (from previous prompts).
prompt3 = """
<system>
You are a debate expert preparing a rebuttal.
</system>
<user>
Given the thesis and the affirmative case below, generate a rebuttal in just one short paragraph.

Thesis:
{task_1_output}

Affirmative Case:
{task_2_output}
</user>
"""
# Create the LLM instance
llm = LLM(model=MODEL, provider=PROVIDER, temperature=TEMPERATURE)

# Create the SequentialWorkflow with the string prompt templates
workflow = SequentialWorkflow(
    tasks=[prompt1, prompt2, prompt3], default_llm=llm, workflow_data=workflow_data
)

# Run the workflow
for chunk in workflow.stream():
    if chunk.event_type != "DEFAULT":
        print(f"\n--- Task {workflow.task_id}: event '{chunk.event_type}' ---\n")
    elif chunk.content is not None:
        print(chunk.content, end="")
