import os
from crewai import Crew, Process
from gaeni_toolkit.agents import Agents, Validator
from gaeni_toolkit.tasks import Tasks, TaskValidator 
from static import Static
from dotenv import load_dotenv
load_dotenv()

llmx = Static.load_api()

if llmx is None:
    raise ValueError("Failed to load API. Please check your API key and connection.")

# Using crewai's built-in search tool instead
from crewai.tools import tool
import requests

@tool("search_tool")
def search_tool(query: str) -> str:
    """Search the web for information using Serper API"""
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        return "No Serper API key found"
    
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": api_key, "Content-Type": "application/json"}
    data = {"q": query, "num": 2}
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        results = response.json()
        return str(results.get("organic", []))
    return "Search failed"
class SetAgent:
    masterH = Agents(llm=llmx, tools=[search_tool]).master_historian_agent()
    questionV = Validator(llm=llmx, tools=[search_tool]).question_validator_agent()
    locationV = Validator(llm=llmx, tools=[search_tool]).location_validator_agent()
    languageV = Validator(llm=llmx, tools=[search_tool]).language_validator_agent()

class Crews:
    def __init__(self, question, location, language):
        self.iquestion = question
        self.ilocation = location
        self.ilanguage = language
        
    def main_crew(self):
        return Crew(
            agents=[
                SetAgent.masterH,
            ],
            tasks=[
                Tasks().historical_task(question=self.iquestion, location=self.ilocation, language=self.ilanguage, agent=SetAgent.masterH),
                Tasks().summarize(question=self.iquestion, location=self.ilocation, language=self.ilanguage, agent=SetAgent.masterH)
            ],
            process=Process.sequential,
            manager_llm=llmx
        )
        
    def validate_crew(self):
        return Crew(
            agents=[
                SetAgent.questionV, SetAgent.locationV, SetAgent.languageV    
            ],
            tasks=[
                TaskValidator().question_validate(self.iquestion, agent=SetAgent.questionV),
                TaskValidator().location_validate(self.ilocation, agent=SetAgent.locationV),
                TaskValidator().language_validate(self.ilanguage, agent=SetAgent.languageV)
            ],
            process=Process.sequential,
            manager_llm=llmx,
            verbose=True
        )