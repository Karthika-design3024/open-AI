💬 Python Chatbot using OpenRouter API
A simple command-line chatbot built in Python using the OpenRouter API and Mistral-7B model. This project demonstrates how to interact with large language models via API calls and create a conversational loop with user-friendly input/output.
🚀 Features
- 🔁 Continuous chat loop with exit commands
- 🤖 Uses Mistral-7B via OpenRouter for responses
- 🧠 System prompt sets chatbot personality
- 🛡️ Graceful exit with "exit", "quit", or "bye"
- 🧰 Easy to customize for other models or prompts
🛠️ Technologies Used
- Python 3.x
- openai Python package
- OpenRouter API (https://openrouter.ai)
📦 Installation
- Install the required package:
pip install openai
- Replace the API key with your own from OpenRouter.
🧑‍💻 How to Run
python chatbot.py


Type your message and interact with the chatbot. To exit, type exit, quit, or bye.
🔐 Security Note
Never share your API key publicly.
For safety, store it in an environment variable or a .env file and load it securely in your script.
📈 Future Enhancements
- Add logging for conversation history
- Integrate voice input/output using speech_recognition and gTTS
- Build a GUI using Tkinter or PyQt
- Support multiple models and dynamic switching
🙋‍♀️ About the Developer
Created by Karthika, an aspiring Python developer focused on building practical projects and exploring real-world applications of AI.


