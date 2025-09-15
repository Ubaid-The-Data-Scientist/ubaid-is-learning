from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_default_openai_api, set_default_openai_client, set_tracing_disabled
from agents.run import RunConfig
import asyncio

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key = GEMINI_API_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

################################################################
### 1. AGENT LEVEL CONFIGURATION
################################################################
async def agent_level_config():
    agent = Agent(
        name = "Assitant",
        instructions = "You only respond in English.",
        model = OpenAIChatCompletionsModel(
            model = "gemini-2.5-flash",
            openai_client=client
        )
    )

    result = await Runner.run(
        agent,
        "Hi! My name is Ubaid Ali Khan."
    )
    print(result.final_output)
# asyncio.run(agent_level_config())

################################################################
### 2. RUN LEVEL CONFIGURATION
################################################################
def run_level_config():
    model = OpenAIChatCompletionsModel(
        model = "gemini-2.0-flash",
        openai_client=client
    )
    config = RunConfig(
        model = model,
        model_provider = client,
        tracing_disabled = True
    )
    agent = Agent(
        name = "Assistant",
        instructions = "You only respond in English.",
    )
    result = Runner.run_sync(agent, "Hi! Im Ubaid Ali Khan.", run_config=config)
    print(result.final_output)
# run_level_config()

################################################################
### 3. GLOBAL LEVEL CONFIGURATION
################################################################
def global_level_config():
    set_tracing_disabled(True)
    set_default_openai_api("chat_completions")
    set_default_openai_client(client)
    agent = Agent(
        name = "Ässistant",
        instructions = "You ara a helpfull assistant",
        model = "gemini-2.0-flash"
    )
    result = Runner.run_sync(agent, "Hey!")
    print(result.final_output)
# global_level_config()


### Set Debug Mode
# from agents import enable_verbose_stdout_logging
# enable_verbose_stdout_logging()