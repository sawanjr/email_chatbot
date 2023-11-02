from langchain import PromptTemplate, OpenAI, LLMChain
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import load_tools , initialize_agent , AgentType

def generate_emails(subject , tone ):
    llm= OpenAI(temperature = 0.5)
    prompt_template_name = PromptTemplate(input_variables=["subject" , "tone" ],template = f"generate a brief e-mail on the subject{subject} and make sure the tone is {tone} in 1 line only")

    name_chain = LLMChain(llm = llm , prompt = prompt_template_name , output_key ="text")

    response = name_chain({"object":object , "tone":tone})
    return response
# def langchain_agent():
#     llm = OpenAI(temperature = 0.5)
#     tools = load_tools(["Grammarly", "Hemingway Editor" , "ProWritingAid"], llm = llm)
#     agent  = initialize_agent(llm , tools,agent = AgentType.CONVERSATIONAL_REACT_DESCRIPTION , verbose = true)
if __name__ == "__main__":
    print(generate_emails("email to the boss for not attending the meeting","crying"))



