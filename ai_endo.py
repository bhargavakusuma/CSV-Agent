from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType

csv_path = '/Users/sakastudio/python/endo-5.csv'
chat_gpt_api_key = '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'
chat_gpt_api_key2 = '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'

type_of_arifical_intelligence_model = 'text-davinci-003'


def index_data():
    # Existing code for indexing data
    
    # Add the provided code for creating the CSV agent
    agent = create_csv_agent(OpenAI(openai_api_key=chat_gpt_api_key2,temperature= 0,
                         model_name=type_of_arifical_intelligence_model), 
                         csv_path,
                         max_rows = 10,
                         verbose=True)
    
    # Running queries
    while True:
        user_question = input("Enter your question: ")
        response = agent.run(user_question)
        print(response)
    
    # Continue with the rest of the indexing method

# Call the indexing method
index_data()