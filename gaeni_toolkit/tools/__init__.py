import os
from langchain.agents import Tool
from newsapi import NewsApiClient
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from crewai_tools import SerperDevTool

# def image_searching(query, serper_key):
#     try:
#         image_search_tool = GoogleSerperAPIWrapper(api_key=serper_key, type="images")
#         results = image_search_tool.results(query)
        
#         if results and len(results) > 0:
#             first_result = results[0]
#             image_url = first_result.get("image_url")
#             description = first_result.get("description", "No description available.")
#             return image_url, description
#         return None, None
#     except Exception as e:
#         print(f"Error fetching image: {str(e)}")
#         return None, None

class Tools:
    def search_tool(self, serper_key):
        return Tool(
            name="Search",
            func=SerperDevTool(api_key=serper_key).run,
            description="A powerful search tool for finding up-to-date information on various topics. Use this to answer questions about current events, facts, or general knowledge. Input should be a specific, well-formulated question or search query. Returns relevant search results including snippets and URLs."
        )
         
    # def image_search(self, serper_key):
    #     return Tool(
    #         name="Image Search",
    #         func=image_searching(serper_key=serper_key),
    #         description="Useful for when you need to find images of something. Input should be a search query."
    #     )
    
    def weather_tool(self, weather_key):
        os.environ["OPENWEATHERMAP_API_KEY"] = weather_key
        return Tool(
            name="Weather",
            func=OpenWeatherMapAPIWrapper().run,
            description="Useful for when you need to find the weather of a location. Input should be a location."
        )
         
    
    def news_finder(self, query, news_key):
        newsapi = NewsApiClient(api_key=news_key)
        
        def get_news():
            return newsapi.get_everything(q=query)
        
        return Tool(
            name="NewsFinder",
            func=get_news,
            description="Useful for finding recent news articles on a specific topic. Input should be a search query or keywords related to the news you're looking for. Returns a list of relevant articles with their titles, descriptions, and URLs."
        )
