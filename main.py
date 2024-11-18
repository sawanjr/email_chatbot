# import langchain_intigration as li
# import streamlit as st

# # Set page title
# st.set_page_config(page_title="Email Generator", page_icon="✉️")

# # Custom CSS for centering the content and equal spacing
# st.markdown(
#     """
#     <style>
#     body {
#         display: flex;
#         flex-direction: column;
#         justify-content: space-between;
#         min-height: 100vh;
#     }
#     main {
#         flex: 1;
#         display: flex;x
#         flex-direction: column;
#         justify-content: center;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Title and description
# st.title("Email Generator")
# st.write("Generate emails with your preferred tone and subject.")

# # User Inputs on the main screen
# st.subheader("your Inputs")
# subject = st.text_input("What is your subject?", max_chars=30, help="Enter your email subject here")
# tone = st.selectbox("Select your tone", ("Formal", "Informal", "Friendly", "Authoritative", "Sympathetic", "Confident", "Humble", "Casual", "Professional", "Sarcastic or Humorous", "Motivational"), help="Specify the tone you want your email to be in")

# # Generate email on button click
# if st.button("Generate Email"):
#     if tone:
#         response = li.generate_email(subject, tone)
#         st.subheader("this is how you chooseed your email to be :")
#         st.write(f"Subject: {subject}")
#         st.write(f"Tone: {tone}")
#         st.subheader("Generated Email:")
#         st.markdown(f"<div style='background-color: #262640; padding: 10px; border-radius: 5px; color: white;'>{response['text']}</div>", unsafe_allow_html=True)

# # Sidebar for Developer Information
# with st.sidebar:
#     st.title("Developer Information")
#     st.markdown("Meet Sawan: A Passionate Explorer of machine learning and LLM ")
#     st.markdown("Allow me to introduce you to Sawan, a dynamic individual who has a deep passion for large language models .")
#     st.markdown("[GitHub](https://github.com/sawanjr)")
#     st.markdown("[LinkedIn](https://www.linkedin.com/in/sawan-kumar-bb8793243)")


# import langchain_intigration as li
# import streamlit as st

# # Set page title
# st.set_page_config(page_title="Email Generator", page_icon="✉️")

# # Custom CSS for centering the content and equal spacing
# st.markdown(
#     """
#     <style>
#     body {
#         display: flex;
#         flex-direction: column;
#         justify-content: space-between;
#         min-height: 100vh;
#     }
#     main {
#         flex: 1;
#         display: flex;x
#         flex-direction: column;
#         justify-content: center;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Title and description
# st.title("Email Generator")
# st.write("Generate emails with your preferred tone and subject.")

# # User Inputs on the main screen
# st.subheader("your Inputs")
# subject = st.text_input("What is your subject?", max_chars=30, help="Enter your email subject here")
# tone = st.selectbox("Select your tone", ("Formal", "Informal", "Friendly", "Authoritative", "Sympathetic", "Confident", "Humble", "Casual", "Professional", "Sarcastic or Humorous", "Motivational"), help="Specify the tone you want your email to be in")

# # Generate email on button click
# if st.button("Generate Email"):
#     if tone:
#         response = li.generate_email(subject, tone)
#         st.subheader("this is how you chooseed your email to be :")
#         st.write(f"Subject: {subject}")
#         st.write(f"Tone: {tone}")
#         st.subheader("Generated Email:")
#         st.markdown(f"<div style='background-color: #262640; padding: 10px; border-radius: 5px; color: white;'>{response['text']}</div>", unsafe_allow_html=True)

# # Sidebar for Developer Information
# with st.sidebar:
#     st.title("Developer Information")
#     st.markdown("Meet Sawan: A Passionate Explorer of machine learning and LLM ")
#     st.markdown("Allow me to introduce you to Sawan, a dynamic individual who has a deep passion for large language models .")
#     st.markdown("[GitHub](https://github.com/sawanjr)")
#     st.markdown("[LinkedIn](https://www.linkedin.com/in/sawan-kumar-bb8793243)")





import langchain_intigration as li
import streamlit as st

# Set page title
st.set_page_config(page_title="Email Generator", page_icon="✉️")

# Custom CSS for centering the content and equal spacing
st.markdown(
    """
    <style>
    body {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 100vh;
    }
    main {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("Email Generator")
st.write("Generate emails with your preferred tone and subject.")

# User Inputs on the main screen
st.subheader("Your Inputs")
subject = st.text_input("What is your subject?", max_chars=80, help="Enter your email subject here")
tone = st.selectbox("Select your tone", 
                    ("Formal", "Informal", "Friendly", "Authoritative", "Sympathetic", "Confident", "Humble", 
                     "Casual", "Professional", "Sarcastic or Humorous", "Motivational"), 
                    help="Specify the tone you want your email to be in")

# Generate email on button click
if st.button("Generate Email"):
    if subject and tone:
        response = li.generate_email(subject, tone)
        
        # Display selected options and the generated email
        st.subheader("This is how you chose your email:")
        st.write(f"Subject: {subject}")
        st.write(f"Tone: {tone}")
        
        st.subheader("Generated Email:")
        st.markdown(f"<div style='background-color: #262640; padding: 10px; border-radius: 5px; color: white;'>{response}</div>", unsafe_allow_html=True)

# Sidebar for Developer Information
with st.sidebar:
    st.title("Developer Information")
    st.markdown("Meet Sawan: A Passionate Explorer of machine learning and LLM ")
    st.markdown("Allow me to introduce you to Sawan, a dynamic individual who has a deep passion for large language models .")
    st.markdown("[GitHub](https://github.com/sawanjr)")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/sawan-kumar-bb8793243)")
