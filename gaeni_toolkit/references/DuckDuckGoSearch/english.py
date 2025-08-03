# What is the DuckDuckGo Search Tool in Langchain? The DuckDuckGo Search Tool 
# in Langchain is an integration between Langchain, a framework for building
# applications powered by Large Language Models (LLMs), and DuckDuckGo, 
# a search engine that emphasizes user privacy. 

# DuckDuckGo does not track or store personal information, 
# and the search results it provides focus on user privacy. 
# This tool allows LLMs in Langchain to dynamically search
# the web for up-to-date information instead of relying on static,
# pre-trained data within the model.

# Key Features:

# Conduct real-time web searches for the latest information.
# Offers a privacy-focused alternative for developers who need search functionality.
# Can be used in various applications that require real-time or dynamic information,
# such as chatbots, AI assistants, and recommendation systems.
# Brief Review: The DuckDuckGo Search Tool in Langchain is particularly 
# useful for developers who want a privacy-centered search solution for their 
# LLM-based applications. The advantages of this tool include:

# Privacy-first: It does not store personal user data.
# Real-time search: Supports searching for the latest, up-to-date information, 
# unlike AI models that are trained on historical data.
# Easy integration with Langchain: It seamlessly integrates with 
# Langchain-based applications and offers flexibility to fetch information from the web.
# However, the downsides include:

# Limited search results: 

# Compared to other search engines like Google,
# DuckDuckGo's search results can be fewer or less comprehensive in certain cases.

# Less effective for niche or specific searches: 

# Results may not always point to the most relevant resources, 
# especially for highly specific or specialized topics.
# Simple Usage of DuckDuckGo Search Tool in Langchain:

# To use the DuckDuckGo Search Tool in Langchain, 
# you first need to install the relevant libraries for integration. 
# Then, you can add this tool to a Chain in Langchain. 

# Here’s a simple example of how to use it:

from langchain.tools import DuckDuckGoSearchRun

# Inisialisasi DuckDuckGo Search Tool
search = DuckDuckGoSearchRun()

# Melakukan pencarian
query = "latest AI trends"
results = search.run(query)

# Menampilkan hasil pencarian
for result in results:
    print(result['title'], result['link'])

# This tool is highly effective when you need up-to-date 
# information while ensuring that user privacy is respected, 
# without falling into the tracking and ad-targeting that occurs with other search engines.






