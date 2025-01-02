from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
#from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import os
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
web_agent = Agent(
    name="Web Agent",
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown=True,
    instructions=["Always include sources"],
)




finance_agent = Agent(
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["Use table to display the stock price data for the company."],
)

agent_teams = Agent (
    team=[web_agent, finance_agent],
    instructions=["Always include sources","Use table to display the stock price data for the company."],
    show_tool_calls=True,
    markdown=True,
)
agent_teams.print_response("Sumarize analyst recommendations for TESLA and NVDA.") 