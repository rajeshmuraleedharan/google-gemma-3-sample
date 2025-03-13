import ollama
import chainlit as cl
from chainlit.input_widget import Select

@cl.on_chat_start
async def start():
    # Create settings panel with dropdown
    settings = await cl.ChatSettings(
        [
            Select(
                id="Model",
                label="Choose a Model",
                values=["qwen2:0.5b", "gemma3", "gemma3:1b"],
                initial_index=0
            )
        ]
    ).send()
    
    # Store the initial model in the user session
    selected_model = settings["Model"]
    cl.user_session.set("model", selected_model)
    
    # Display initial welcome message
    if selected_model == "qwen2:0.5b":
        welcome_message = f"Hello! I'm a {selected_model} model running on Ollama. Qwen2.5 models are pretrained on Alibaba's latest large-scale dataset, encompassing up to 18 trillion tokens. The model supports up to 128K tokens and has multilingual support. Check more about me - https://ollama.com/library/qwen2.5 . To see the code, please check my GitHub repo https://github.com/rajeshmuraleedharan/google-gemma-3-sample/tree/main . How can I help you today?"
    elif ( selected_model == "gemma3" or selected_model == "gemma3:1b"):
        welcome_message = f"Hello! I'm a {selected_model} model running on Ollama. Gemma3, developed by Google, is optimized for efficiency and performance, supporting a wide range of tasks with up to 9 billion parameters. Learn more at https://ai.google/discover/gemma/ . To see the code, please check my GitHub repo https://github.com/rajeshmuraleedharan/google-gemma-3-sample/tree/main . How can I help you today?"
    else:
        welcome_message = f"Hello! I'm a {selected_model} model running on Ollama. Details are unavailable. To see the code, please check my GitHub repo https://github.com/rajeshmuraleedharan/google-gemma-3-sample/tree/main . How can I help you today?"
    
    await cl.Message(content=welcome_message).send()

@cl.on_settings_update
async def setup_agent(settings):
    # Update the model in the user session when settings change
    selected_model = settings["Model"]
    cl.user_session.set("model", selected_model)
    
    # Display welcome message based on the new model
    if selected_model == "qwen2:0.5b":
        welcome_message = f"Hello! I'm a {selected_model} model running on Ollama. Qwen2.5 models are pretrained on Alibaba's latest large-scale dataset, encompassing up to 18 trillion tokens. The model supports up to 128K tokens and has multilingual support. Check more about me - https://ollama.com/library/qwen2.5 . To see the code, please check my GitHub repo https://github.com/rajeshmuraleedharan/google-gemma-3-sample/tree/main . How can I help you today?"
    elif ( selected_model == "gemma3" or selected_model == "gemma3:1b"):
        welcome_message = f"Hello! I'm a {selected_model} model running on Ollama. Gemma3, developed by Google, is optimized for efficiency and performance, supporting a wide range of tasks with up to 9 billion parameters. Learn more at https://ai.google/discover/gemma/ . To see the code, please check my GitHub repo https://github.com/rajeshmuraleedharan/google-gemma-3-sample/tree/main . How can I help you today?"
    else:
        welcome_message = f"Hello! I'm a {selected_model} model running on Ollama. Details are unavailable. To see the code, please check my GitHub repo https://github.com/rajeshmuraleedharan/google-gemma-3-sample/tree/main . How can I help you today?"
    
    await cl.Message(content=welcome_message).send()

@cl.on_message
async def main(message: cl.Message):
    # Get the currently selected model from the user session
    selected_model = cl.user_session.get("model", "qwen2:0.5b")
    
    # Call Ollama with the selected model
    try:
        response = ollama.chat(
            model=selected_model,
            messages=[
                {
                    'role': 'user',
                    'content': message.content
                },
            ],
        )
        await cl.Message(content=response['message']['content']).send()
    except Exception as e:
        await cl.Message(content=f"Error: {str(e)}").send()