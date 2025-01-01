from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
agent = Agent(
    model=Groq(id='llama-3.3-70b-versatile'),
    #api_key=os.getenv("GROQ_API_KEY")
)

agent.print_response("Write a sentence about a llama.")