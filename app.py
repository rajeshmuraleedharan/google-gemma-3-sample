import ollama

response = ollama.chat(
    model='gemma3',
    messages=[
        {
        'role': 'user',
        'content': 'Give me a meal plan for today',
        },
    ],
)

print(response['message']['content'])