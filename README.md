# Google Gemma 3 Sample LLM Agents

This repository contains sample implementations of LLM (Large Language Model) agents using Google Gemma 3.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project demonstrates the use of Google Gemma 3 to create and manage LLM agents. The goal is to provide a comprehensive guide and examples for developers interested in leveraging LLM technology.

## Installation

To get started, clone the repository and install the necessary dependencies:

```bash
1) Download - download https://ollama.com/download
2) run "ollama pull gemma3" from your vscode cmd
3) pip install ollama chainlit
```

## Usage

![image](https://github.com/user-attachments/assets/3d8f6634-4ada-4fea-83e0-ec5de968f163)

UI using chainlit
![image](https://github.com/user-attachments/assets/1524b975-b793-4303-ac26-e1df0bfb3895)
![image](https://github.com/user-attachments/assets/adc637c9-da9c-4ec7-b131-c5f2eed38a5a)



Here are some basic usage examples:

```python
from gemma3 import LLM

# Initialize the LLM agent
agent = LLM()

# Example usage
response = agent.process("Hello, how can I assist you today?")
print(response)
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
