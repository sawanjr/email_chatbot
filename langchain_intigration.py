# from langchain import PromptTemplate, OpenAI, LLMChain
# from dotenv import load_dotenv

# load_dotenv()
from langchain import PromptTemplate
import openai  # Import the openai module
# from dotenv import load_dotenv

# load_dotenv()
OPENAI_API_KEY = "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"

def generate_email(subject, tone):
    llm = openai.ChatCompletion.create(temperature=0.5, max_tokens=50, top_p=1, frequency_penalty=0, stop=None, engine="gpt-3.5-turbo", max_responses=1)
    prompt_template_name = PromptTemplate(input_variables=["subject", "tone"], template="generate a brief e-mail on the subject {subject} and make sure the tone is {tone} in 5 lines only")

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="text")

    response = name_chain({"subject": subject, "tone": tone})
    return response

if __name__ == "__main__":
    result = generate_email("email to the boss for not attending the meeting", "american english")
    print(result)
