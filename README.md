# Google Gemma 3 Sample LLM Agents

This repository contains sample implementations of LLM agents using Google Gemma 3 and other models like Qwen2 and GPT-2. The goal is to provide a comprehensive guide and examples for developers interested in leveraging LLM technology.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project demonstrates the use of Google Gemma 3 to create and manage LLM agents. It also includes examples of using other models like Qwen2 and GPT-2. The goal is to provide a comprehensive guide and examples for developers interested in leveraging LLM technology.

## Installation

To get started, clone the repository and install the necessary dependencies:

```bash
1) Download - download https://ollama.com/download
2) run "ollama pull gemma3" from your vscode cmd
3) run "ollama pull qwen2:0.5b" from your vscode cmd
4) pip install ollama chainlit transformers

```

#Running the app.py Script
The app.py script demonstrates a simple usage of the Gemma 3 model to generate a meal plan for the day:
![image](https://github.com/user-attachments/assets/513f603b-fc8c-449b-82d0-34939b5dac90)

To run this script, execute it with Python: 
```bash
python app.py
```

#Running the Gemma 3 model via web ui (gemma3-ui.py Script)
gemma3-ui.py script demonstrates a simple usage of the Gemma 3 model and shows in a web ui using chainlit lib
![image](https://github.com/user-attachments/assets/0abe2e79-78e6-4e98-a665-eda5d927acb0)

To run this script, execute it with Python:
```bash
chainlit run gemma3-ui.py
```
#Running the Qwen2 Model via web ui (qwen2-ui.py Script)
![image](https://github.com/user-attachments/assets/27e0f3d4-5e6e-4e63-a191-b2e9157e1ae5)

To run this script, execute it with Python:
```bash
chainlit run qwen2-ui.py
```

