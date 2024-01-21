### Introduction

This repository contains a Python-based STEM problem solver that uses a combination of image processing, natural language processing, and machine learning to solve problems in STEM fields. The project includes three main components:

1. `app.py`: A Streamlit application that allows users to upload an image of a STEM problem and process it using the provided functions.
2. `notebook.py`: A Jupyter notebook that contains functions for processing user input through the Wolfram Alpha Short Answers API and the ChatGPT API.
3. `wolfram.py`: A Python script that contains functions for processing queries through the Wolfram Alpha Short Answers API and the ChatGPT API.

### Setup

To run the project, you will need to install the following dependencies:

- Streamlit
- Requests
- Wolfram Alpha API credentials
- OpenAI API credentials
- Mathpix API credentials

You can install the required packages using the following command:

```bash
pip install streamlit requests
```

### Usage

#### App.py

To use the Streamlit application, run the following command:

```bash
streamlit run app.py
```

This will open a web application in your browser where you can upload an image of a STEM problem. Once the image is processed, the application will display the problem statement and the solution.

#### Notebook.py

To use the Jupyter notebook, run the following command:

```bash
jupyter notebook notebook.ipynb
```

This will open the notebook in your default Jupyter notebook viewer. You can interact with the notebook by running cells and exploring the output.

#### Wolfram.py

To use the Python script, run the following command:

```bash
python wolfram.py
```

This will start the chatbot, which processes user input through the Wolfram Alpha Short Answers API and the ChatGPT API. You can interact with the chatbot by entering text and pressing Enter.

### Contributing

If you would like to contribute to the project, please submit a pull request with your proposed changes. Make sure to include a detailed description of the changes you made and any relevant context.
