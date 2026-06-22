from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="1447de8c76c2436c9fcc60755cb2ff81.vBDQwUX0DYbv-iuC-N-QDWzT"  # dummy key
)

response = client.chat.completions.create(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain MXFP4 quantization."}
    ]
)
print(response.choices[0].message.content)