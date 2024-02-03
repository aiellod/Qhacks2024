from openai import OpenAI
import keys
client = OpenAI(api_key = keys.KEY_OPENAI)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are writing python code"},
    {"role": "user", "content": "Make code about a: stack class"},

  ]
)

print(response.choices[0].message.content)