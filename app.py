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

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, verbose=True)

        agent = create_csv_agent(
            llm,
            csv_file,
            verbose=True,
            allow_dangerous_code=True  
        )


        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question:
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()
