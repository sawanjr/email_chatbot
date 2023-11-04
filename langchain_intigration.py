from langchain import PromptTemplate, OpenAI, LLMChain
import openai

def generate_email(subject, tone):
    api_key = "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"  # Replace with your actual OpenAI API key
    llm = openai.ChatCompletion.create(
        temperature=0.5,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        stop=None,
        engine="gpt-3.5-turbo",
        max_responses=1,
        api_key=api_key  # Manually set your API key
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
