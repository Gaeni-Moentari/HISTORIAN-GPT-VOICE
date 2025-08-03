from crewai import Task

class Tasks:
    def historical_task(self, question, location, language, agent):
        historical = Task(
            description=f"""
                Provide a detailed explanation of the historical event related to '{question}' in {location}.
                Your response should include:
                - A summary of the event, outlining the key moments.
                - The significant historical figures involved and their roles.
                - How this event impacted {location} socially, politically, or economically.
                Ensure the explanation is well-structured, easy to follow, and factually accurate.
            """,
            expected_output=f"""
                A comprehensive explanation of the historical event '{question}' in {location} must with {language} language, covering 
                key facts, major figures, the event's impact on the region, and its broader historical significance.
            """,
            agent=agent
        )
        return historical

    
    def weather_task(self, question, location, language, agent):
        weather = Task(
            description=f"""
                Research the historical weather conditions during the event '{question}', focusing specifically 
                on the location '{location}' at the time of the event' language.
                Your research should include:
                - Temperature, precipitation, and wind conditions during the event.
                - Any notable weather phenomena (e.g., storms, extreme temperatures, or droughts) that may have influenced the event.
                Be sure to use reliable historical data sources and clearly explain any uncertainties in the information provided.
            """,
            expected_output=f"""
                A detailed report on the historical weather conditions at {location} during the event '{question}' with {language} language, 
                including temperature, precipitation, wind conditions, and any relevant anomalies or weather phenomena.
                If applicable, explain how the weather may have impacted the event's outcomes.
            """,
            agent=agent
        )
        return weather

    
    def news_task(self, question, location, language, agent):
        news = Task(
            description=f"""
                Search for the latest news related to the event '{question}' in {location}.
                Focus on finding reliable and credible sources. Collect at least three relevant news articles 
                from different sources, ensuring the information is up-to-date.
                
                use the following format for each article:
                - Date: [Date the article was published]
                - Source: [Name of the news source]
                - Description: [Brief description of the article's content]
                - Relevance: [Explain why this article is relevant to the event '
            """,
            expected_output=f"""
                A summary of the latest news related to the event '{question}' in {location} must with {language} language, 
                including three articles with publication dates, sources, and content descriptions, and please ensure the article is accessable.
            """,
            agent=agent
        )
        return news
    
    def photo_task(self, location, language, agent):
        return Task(
            description=(
                f"""Search for a relevant image related to the historical event in '{location}'.
                Ensure the image is from a trustworthy source.
                """
            ),
            expected_output=f"""
            Display the image using st.image() and provide the description in {language} language. 
            The most relevant image should be shown.
            """,
            agent=agent
        )

    def summarize(self, question, location, language, agent):
        sum = Task(
            description=f"""
            collect all the results of the task, and organize the information 
            in a detailed and understandable way for the general public,
            
            for answering this {question}, at {location}=.
            
            """,
            expected_output=f"""
            - A summary of the history, outlining the key moments.
            - The significant historical figures involved and their roles.
            - gave 1 most relevant article include the name of the news and the link of the article.
            
            The answer must be using {language} language.
            
            """,
            agent=agent
        )
        return sum
    
class TaskValidator:
    def question_validate(self, question, agent):
        vquestion = Task(
            description=f"Check if the question '{question}' is related to history.",
            expected_output="Answer with 'yes' if the question is related to history, otherwise 'no'.",
            agent=agent
        )
        return vquestion
    
    def location_validate(self, location, agent):
        vlocation = Task(
            description=f"Verify if the location '{location}' is a real-world location.",
            expected_output="Answer with 'yes' if the location is real, otherwise 'no'.",
            agent=agent
            
        )
        return vlocation
    
    def language_validate(self, language, agent):
        vlanguage = Task(
            description=f"Check if the language '{language}' is a real and valid language.",
            expected_output="Answer with 'yes' if the language exists, otherwise 'no'.",
            agent=agent
        )
        return vlanguage
    