from langchain_experimental.agents import create_csv_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import streamlit as st

def main():
    load_dotenv()

    # Load the Gemini API key from the environment variable
    if os.getenv("GOOGLE_API_KEY") is None or os.getenv("GOOGLE_API_KEY") == "":
        print("GOOGLE_API_KEY is not set")
        exit(1)
    else:
        print("GOOGLE_API_KEY is set")

    st.set_page_config(page_title="Wedding planner")
    st.header("Ask your CSV 📈")

    # Set the path to your CSV file
    csv_file_path = r"C:\Users\Sahil\Desktop\weds\wedding_venues.csv"

    # Create the agent using the local file
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, verbose=True)
    agent = create_csv_agent(
        llm,
        csv_file_path,
        verbose=True,
        allow_dangerous_code=True
    )

    user_question = st.text_input("Give me the location,geust capacit and budget i will recomment you the venue?")

    if user_question:
        with st.spinner(text="In progress..."):
            st.write(agent.run(user_question))

if __name__ == "__main__":
    main()
