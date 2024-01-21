import streamlit as st
import requests
import base64
import wolframalpha
from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI
import openai
import os

openai.api_key = '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'

# Mathpix API credentials
app_id = 'newgrade_ai_45522e_af53e0'
app_key = '70ca7520c72e1f76d7d151b0d77a437555c18644570228421c3ba4e0c4077f82'
api_url = "https://api.mathpix.com/v3/text"

# LangChain and GPT setup
llm = OpenAI(model='gpt-3.5-turbo')
prompt_template = PromptTemplate(
    template="Translate the problem statement: {equation} into Wolfram computational language",
    input_variables=["equation"]
)
llm_chain = LLMChain(prompt=prompt_template, llm=llm)

# Wolfram Alpha setup
wolfram_client = wolframalpha.Client("EHPL84-R8JVY7PT9W")

st.title("STEM Problem Solver")

uploaded_file = st.file_uploader("Upload an image of a STEM problem", type=["jpg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

if st.button("Process Image"):
    with st.spinner("Processing image..."):
        encoded_image = base64.b64encode(uploaded_file.read()).decode()

        headers = {
            "app_id": app_id,
            "app_key": app_key,
            "Content-type": "application/json"
        }
        data = {
            "src": "data:image/jpeg;base64," + encoded_image,
            "formats": ["text", "latex"],
            "ocr": ["math", "text"],
        }
        response = requests.post(api_url, json=data, headers=headers)
        result = response.json()

        problem_text = result.get("text", "")
        problem_latex = result.get("latex", "")

    if problem_text or problem_latex:
        st.write(f"Problem: {problem_text if problem_text else problem_latex}")

        processed_problem = llm_chain.run({"equation": problem_text if problem_text else problem_latex})

        with st.spinner("Solving problem..."):
            res = wolfram_client.query(processed_problem)
            answer = next(res.results).text

        st.write(f"Answer: {answer}")
    else:
        st.error("No problem detected in the image.")