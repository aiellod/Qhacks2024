import openai

# Set your API key
openai.api_key = 'YOUR_API_KEY'

# Generate text using the OpenAI API
response = openai.Completion.create(
    engine="text-davinci-003",  # You can use other engines as well
    prompt="Write a Python script to",
    max_tokens=100
)

# Print the generated text
print(response['choices'][0]['text'])

