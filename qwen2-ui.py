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
    await cl.Message(content="Hello! I'm a qwen2 model running on Ollama. Qwen2.5 models are pretrained on Alibaba's latest large-scale dataset, encompassing up to 18 trillion tokens. The model supports up to 128K tokens and has multilingual support. Check more about me - https://ollama.com/library/qwen2.5 . To see the code, please check my github repo https://github.com/rajeshmuraleedharan/google-gemma-3-sample/tree/main .  How can I help you today?").send()