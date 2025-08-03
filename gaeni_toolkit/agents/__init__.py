from crewai import Agent

class Agents:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools
    
    def master_historian_agent(self):
        try:
            history = Agent(
                name="Master World Historian",
                role="Master World Historian",
                goal="""Provide the latest and most specific information about world history.
                        Your task is to uncover detailed insights about historical figures,
                        major events, and their global impact.""",
                memo=False,
                backstory="""You are an expert in global history, with deep knowledge of key figures 
                            and significant events that shaped civilizations. Your mastery allows 
                            you to search for detailed historical accounts and provide specific 
                            insights into world events.""",
                tools=self.tools,
                verbose=True,
                llm=self.llm
            )
            print("Agent created successfully")
            return history
        except Exception as e:
            print(f"Error creating master_historian_agent: {str(e)}")
        return None
    
    def reporter_historian_agent(self):
        try:
            report = Agent(
                name="World Historian Reporter",
                role="World Historian Reporter",
                goal="""Report on the latest news from the historical site in question.
                        Your job is to find the most relevant and up-to-date news related to
                        the specific historical locations.""",
                memo=False,
                backstory="""As a history-focused reporter, you are skilled at connecting current 
                            news with historical relevance. Your investigative skills allow you to 
                            find up-to-date stories from historical locations and report them accurately.""",
                tools=self.tools,
                verbose=True,
                llm=self.llm               
            )
            print("Agent created successfully")
            return report
        except Exception as e:
            print(f"Error creating reporter_historian_agent: {str(e)}")
            return None
    
        
class Validator:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools
        
    def question_validator_agent(self):
        try:
            vquestion = Agent(
                name='Question Validator',
                role='Question Validator',
                goal='Validate if the user question is related to history.',
                verbose=False,
                memory=False,
                backstory=(
                    "As a historian and researcher, you are tasked with ensuring that "
                    "the user question is relevant to historical topics."
                ),
                tools=self.tools,
                llm=self.llm,
                max_iter=3
            )
            print("Agent created successfully")
            return vquestion
        except Exception as e:
            print(f"Error creating question_validator_agent: {str(e)}")
            return None

    def location_validator_agent(self):
        try:
            vlocation = Agent(
                name='Location Validator',
                role='Location Validator',
                goal='Validate if the input location is a real location on Earth.',
                verbose=False,
                memory=False,
                backstory=(
                    "As a geographer and cartographer, your expertise lies in identifying real "
                    "locations on Earth to ensure accurate location recognition."
                ),
                tools=self.tools,
                llm=self.llm,
                max_iter=3
            )
            print("Agent created successfully")
            return vlocation
        except Exception as e:
            print(f"Error creating location_validator_agent: {str(e)}")
            return None
    
    def language_validator_agent(self):
        try:
            vlanguage = Agent(
                name='Language Validator',
                role='Language Validator',
                goal='Validate if the input language is a real language.',
                verbose=False,
                memory=False,
                backstory=(
                    "As a linguist and language expert, your expertise lies in identifying real "
                    "languages to ensure accurate language recognition."
                ),
                tools=self.tools,
                llm=self.llm,
                max_iter=3
            )
            print("Agent created successfully")
            return vlanguage
        except Exception as e:
            print(f"Error creating language_validator_agent: {str(e)}")
            return None
            

