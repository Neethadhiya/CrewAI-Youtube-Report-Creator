# Example: Creating an agent with all attributes
from crewai import Agent
from tools import yt_tool
import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]=os.getenv("OPENAI_MODEL_NAME")

llm = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    model_name=os.environ["OPENAI_MODEL_NAME"]
)
blog_resercher = Agent(
  role='Blog resercher from youtube videos',
  goal='get relevent video content for the topic {topic} from youtube channel',
  backstory="""Expert in understanding videos in AI Data Science ,Machine learning and Gen AI""",
  tools=[yt_tool],  # Optional, defaults to an empty list
  llm=llm,
  verbose=True,  # Optional
  memory=True,
  allow_delegation=True,  # Optional

)

blog_writer = Agent(
  role='Blog writer',
  goal='Narrate compelling tech stories about the video {topic} from youtube channel',
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate , bringing new"
    "discoveries to light in an accessible manner"
  ),
  tools=[yt_tool],  # Optional, defaults to an empty list
  verbose=True,  # Optional
  memory=True,
  llm=llm,
  allow_delegation=False,  # Optional

)