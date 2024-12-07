from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Replace "your-fine-tuned-model" with the actual model ID from your dashboard
completion = client.chat.completions.create(
    model="ft:gpt-4o-mini-2024-07-18:personal:haiku-generator2:AaVJvva8",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ],
    temperature=0.8,
    max_tokens=50
)

print(completion.choices[0].message.content)