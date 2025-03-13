import ollama
import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    response = ollama.chat(
        model='qwen2:0.5b',
        messages=[
            {
                'role': 'user',
                'content': message.content
            },
        ],
    )

    await cl.Message(content=response['message']['content']).send()

@cl.on_chat_start
async def start():
    await cl.Message(content="Hello! I'm a qwen2 model running on Ollama. How can I help you today?").send()