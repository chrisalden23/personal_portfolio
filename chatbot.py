from groq import Groq
import os

client = Groq(
    api_key = "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",
)
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": "can you tell me what is the meaning of life?"
        },
        {
            "role": "assistant",
            "content": ""
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

print(completion)
for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
