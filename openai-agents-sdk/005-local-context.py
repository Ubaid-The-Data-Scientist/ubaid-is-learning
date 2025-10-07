from dataclasses import dataclass
from agents import Agent, function_tool, RunContextWrapper, Runner, set_tracing_disabled
import asyncio
from models import gemini_model

set_tracing_disabled(disabled=True)

## Define a local context using a data class
@dataclass
class UserInfo:
    name: str
    uid: int
    location: str = "Pakistan"

##  A tool function that access the local context via wrapper
@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    """"Returns the age of the user."""
    return f"User {wrapper.context.name} is 24 years old."

@function_tool
async def fetch_user_location(wrapper: RunContextWrapper[UserInfo]) -> str:
    """"Returns the location of the user."""
    return f"User {wrapper.context.name} is from {wrapper.context.location}."


async def main():
    # Create local context object
    user_info = UserInfo(name="Ubaid", uid=123)

    # Agent that uses above tool
    agent = Agent[UserInfo](
        name = "Assistant",
        model=gemini_model,
        tools = [fetch_user_age, fetch_user_location]
    )

    result = await Runner.run(
        starting_agent=agent,
        input="What is the age of the user? What's his location?",
        context=user_info
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())