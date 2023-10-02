import pandas as pd
import openai

# Load your workbook using pandas
workbook = pd.read_csv("HR Accs Open AI.csv")

# Define the question you want to ask
question = "Based on the following criteria, can the company description be classified as an HR Tech company - answer with yes or no. criteria: xx, xx, xx..."

# Set your OpenAI API key
api_key = "your_api_key_here"  # Replace with your actual API key

# Create an empty list to store the generated answers
generated_answers = []

# Function to make a request to OpenAI
def generate_answer(input_text):
    prompt = f"{question}\n{input_text}\nAnswer:"
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            api_key=api_key,  # Include your API key here
        )
        answer = response.choices[0].text.strip()
    except Exception as e:
        print("Error:", e)
        answer = "Error generating answer"

    return answer

# Iterate through rows and perform interaction with ChatGPT
for index, row in workbook.iterrows():
    input_text = row["Description"]  # data in column H
    print(input_text)

    answer = generate_answer(input_text)
    print(answer)
    
    # Append the generated answer to the list
    generated_answers.append(answer)

# Add the generated answers to the DataFrame
workbook["RELEVANT"] = generated_answers

# Save the updated DataFrame to the Excel file
workbook.to_csv("HR Accs Open AI.csv", index=False)