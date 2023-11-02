from langchain import PromptTemplate, OpenAI, LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_email(subject, tone):
    llm = OpenAI(temperature=0.5)
    prompt_template_name = PromptTemplate(input_variables=["subject", "tone"], template="generate a brief e-mail on the subject {subject} and make sure the tone is {tone} in 20 line only")

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="text")

    response = name_chain({"subject": subject, "tone": tone})
    return response

if __name__ == "__main__":
    result = generate_email("email to the boss for not attending the meeting", "american english")
    print(result)
