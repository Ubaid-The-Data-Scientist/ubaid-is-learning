################################################################
### 1. HOSTED TOOLS (By OpenAI, requires a paid openai api key)
################################################################
from agents import Agent, Runner, WebSearchTool, FileSearchTool

agent = Agent(
    name="Assistant",
    tools=[
        WebSearchTool(),
        FileSearchTool(max_num_results=3, vector_store_ids=["VECTOR_STORE_ID"]),
    ],
)

async def main():
    result = await Runner.run(
        agent,
        "Which coffee shop should I go to, considering my preferences and the weather today?",
    )
    print(result.final_output)


################################################################
### 2. FUNCTION TOOLS (Python functions that agents used as tools)
################################################################
from typing_extensions import TypedDict, Any
from agents import Agent, RunContextWrapper, FunctionTool, function_tool
import json

class Location(TypedDict):
    lat: float
    long: float

@function_tool
async def fetch_weather(location: Location) -> str:
    """Fetch weather for a given location
    Args:
        Location: The location to the fetch the weather for.
    """
    # Agent will use docstring as the description of the agent.
    return "Sunny"

@function_tool
def read_file(ctx: RunContextWrapper[Any], path: str, directory: str | None = None) -> str:
    """Read the contents of a file.
    Args:
        path: The path to the file to read.
        directory: The directory to read the file from.
    """
    # In real life, we'd read the file from the file system
    return "<file contents>"

agent = Agent(
    name = "Assistant",
    tools = [fetch_weather, read_file]
)

# for tool in agent.tools:
#     if isinstance(tool, FunctionTool):
#         print(tool.name)
#         print(tool.description)
#         print(json.dumps(tool.params_json_schema, indent = 2))
#         print()

################################################################
### 3. AGENTS AS TOOLS
################################################################
from agents import Agent, Runner
import asyncio

spanish_agent = Agent(
    name = "Spanish Agent",
    instructions = "You translate the user's message to spanish." 
)
french_agent = Agent(
    name = "French Agent",
    instructions = "You translate the user's message to french." 
)

orchestration_agent = Agent(
    name = "orchestration_agent",
    instructions = (
        "You are a translation agent. You use the tools given to you to translate."
        "If asked for multiple translations, you call the relevant tools."
    ),
    tools = [
        spanish_agent.as_tool(
            tool_name = "translate_to_spanish",
            tool_description = "Translate the user's message to Spanish"
        ),
        french_agent.as_tool(
            tool_name = "translate_to_french",
            tool_description = "Translate the user's message to French"
        )
    ]
)

async def main():
    result = await Runner.run(orchestration_agent, input = "Say, 'Hello, how are you?' in Spanish")
    print(result.final_output)  