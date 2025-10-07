from agents import Agent, Runner, function_tool, ModelSettings, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI
from models import gemini_model

# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# client = AsyncOpenAI(
#     api_key = GEMINI_API_KEY,
#     base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
# )
# model = OpenAIChatCompletionsModel(
#         model = "gemini-2.5-flash",
#         openai_client = client
# )


@function_tool
def calc_area(lenght: float, width: float) -> str:
    """Calculates area of a rectangle."""
    area = lenght * width
    return f"Area = {lenght} x {width} = {area} square units"

agent = Agent(
    name = "Tool Agent",
    instructions = "You're a helpfull assistant. Use tools whenever needed",
    tools = [calc_area],
    model = gemini_model,
    model_settings = ModelSettings(
        temperature=0.1, # lower -> concise, higher -> creative
        tool_choice = "auto", # auto -> Agent decide, required -> Must use, none -> no use  
        max_tokens = 200,
        # parallel_tool_calls = True, # True -> Use multiple tools simultenously, False -> Vice versa
        # top_p = 0.3, # Use only top 30% of vocab
        # frequency_penalty = 0.5, # Avoid repeated words
        # presence_penalty = 0.3, # Encourage new topics
    )
)

result = Runner.run_sync(
    agent, "What's the area of 5x3 rectangle?"
)
print(result.final_output)