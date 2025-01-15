import os
from cohere import Client

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Cohere-command-r-plus-08-2024"

client = Client(
    base_url=endpoint,
    api_key=token,
)

response = client.chat(
    model=model_name,
    preamble='You are a helpful assistant.',
    message='What is the specification of your training data?',
    temperature=1.0,
    max_tokens=5000,
    p=1.0
)

print(response.text)