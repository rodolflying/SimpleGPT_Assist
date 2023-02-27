# Simple GPT assistant

A simple repository for a strightforward use of chat gpt on python

This repository contains a Python script to ask questions to OpenAI's GPT-3 chatbot, the popular CHAT GPT and save the response to a JSON file. The script utilizes the OpenAI API and the dotenv package to load the API key from a .env file.

Requirements:
Python 3.x
dotenv package
openai package

Setup
Clone the repository to your local machine.

Install the required packages using pip: pip install -r requirements.txt.

Create a .env file in the root directory with your OpenAI API key in the following format: API_KEY=your-api-key.

Run the script using the command: python main.py.

Usage
When running the script, you will be prompted to enter a question. After entering the question, the script will call OpenAI's GPT-3 chatbot and return a response. The response will also be saved to a JSON file with the name of the file based on the question asked.

Note
The openai package requires an OpenAI API key to be able to utilize GPT-3. You can get your own API key from OpenAI's website.

The current implementation uses the "text-davinci-003" GPT-3 model for generating responses. You can change the model by modifying the engine parameter
