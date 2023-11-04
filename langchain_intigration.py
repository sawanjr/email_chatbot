from langchain import PromptTemplate, LLMChain
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access your OpenAI API key from the environment variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def generate_email(subject, tone):
    # Initialize OpenAI with your API key
    openai.api_key = OPENAI_API_KEY

    llm = openai.ChatCompletion.create(
        temperature=0.5, max_tokens=50, top_p=1, frequency_penalty=0,
        stop=None, engine="gpt-3.5-turbo", max_responses=1
    )
    prompt_template_name = PromptTemplate(
        input_variables=["subject", "tone"],
        template="generate a brief e-mail on the subject {subject} and make sure the tone is {tone} in 5 lines only"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="text")

    response = name_chain({"subject": subject, "tone": tone})
    return response

if __name__ == "__main__":
    result = generate_email("email to the boss for not attending the meeting", "american english")
    print(result)
