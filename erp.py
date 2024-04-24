from openai import OpenAI
client = OpenAI()

# Ask a question
question = "is there any pending invoice? what is the latest invoice amount? don't talk too much. just answer the question. can you do that"

# Import files
import json
filepath = 'files/all_data.json'
with open(filepath, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Chat with GPT-4
completion = client.chat.completions.create(
  model="gpt-4-turbo-preview",
  messages=[
    {"role": "system", "content": "You are a Microsoft Business Central expert. You know it's APIs and JSON structure."},
    {"role": "user", "content": question + " from the json below " + json.dumps(data)},
  ]
)

print(completion.choices[0].message.content)