from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
import os

# Store the Gemini API key directly in the script
GEMINI_API_KEY = "AIzaSyAidAGbyMSnpDEsNk78aOjH2uHKzRz2PrA"  # Replace with your actual API key

def generate_email(subject, tone):
    # Initialize the LangChain LLM with Google Generative AI
    llm = ChatGoogleGenerativeAI(
        api_key=GEMINI_API_KEY,
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None
    )

    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant that writes an email with the subject '{subject}' in a '{tone}' tone.",
            ),
            ("human", "Generate the email."),
        ]
    )

    # Combine the prompt with the LLM
    chain = prompt | llm

    # Invoke the chain
    response = chain.invoke({"subject": subject, "tone": tone})
    return response.content  # Only return the main content (email body)

if __name__ == "__main__":
    result = generate_email(
        subject="email to the boss for not attending the meeting", tone="professional"
    )
    print(result)
