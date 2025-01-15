import os
from mistralai import Mistral, UserMessage, SystemMessage

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Codestral-2501"

client = Mistral(api_key=token, server_url=endpoint)

response = client.chat.complete(
    model=model_name,
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content="Why did the Ottoman empire fail to reform?"),
    ],
    temperature=1.5,
    max_tokens=10000,
    top_p=1.0
)

print(response.choices[0].message.content)