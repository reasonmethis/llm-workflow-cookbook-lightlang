"""This example demonstrates how to chain prompts in a SequentialWorkflow.

In this example, we create a SequentialWorkflow with three prompts, which generates a \
random thesis for debating, provides the affirmative case for the thesis, and prepares a rebuttal."""

from lightlang.llms.llm import LLM
from lightlang.tasks.task_streaming import TaskEvent
from lightlang.workflows.sequential_workflow import SequentialWorkflow

# Define the first prompt
# This prompt instructs the assistant to generate a random thesis for debating.
prompt1 = """
<name thesis>
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
<name affirmative_case>
<system>
You are a debate expert participating in a competition.
</system>
<user>
Provide the affirmative case for the following thesis in just three paragraphs:

{thesis}
</user>
"""

# Define the third prompt
# This prompt instructs the assistant to prepare a rebuttal.
# It provides both the thesis and the affirmative case (from previous prompts).
prompt3 = """
<name rebuttal>
<system>
You are a debate expert preparing a rebuttal.
</system>
<user>
Given the thesis and the affirmative case below, generate a rebuttal in three paragraphs.

Thesis:
{thesis}

Affirmative Case:
{affirmative_case}
</user>
"""

# Create the SequentialWorkflow with the string prompt templates
workflow = SequentialWorkflow(
    tasks=[prompt1, prompt2, prompt3],
    default_llm=LLM("openai", "gpt-4o-mini", temperature=0.9),
    workflow_data={"topic": "philosopy of mind"}, # Structure for inputs and outputs
)

# Run the workflow
for output in workflow.stream():
    if isinstance(output, TaskEvent):
        print(f"\n--- Event '{output.event}' for task {workflow.task_id} ---\n")
    elif output.content is not None:
        print(output.content, end="")
