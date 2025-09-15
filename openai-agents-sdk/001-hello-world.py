import asyncio
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, ModelSettings, set_tracing_disabled, enable_verbose_stdout_logging
from dotenv import load_dotenv
import os


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()


client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a question answering bot. Keep answers 1-2 lines long.",
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash", 
            openai_client=client
            ),
        model_settings=ModelSettings(max_tokens=100)
    )

    result = await Runner.run(
        agent,
        "What is AI?"
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())