from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from dotenv import load_dotenv
#from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
agent = Agent(
    model=Groq(id='llama-3.3-70b-versatile'),
   # model=OpenAIChat(id="gpt-3.5-turbo"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use table to display the stock price data for the company."],
    #api_key=os.getenv("GROQ_API_KEY")
)

agent.print_response("Sumarize and compere analyst recommendations for TESLA and NVDA.")