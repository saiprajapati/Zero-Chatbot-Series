import nltk
import json
import os
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

MEMORY_FILE = "memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)


pairs = [
    [r"hi|hello|hey", ["Hello! I am Zero. How can I help you today?"]],
    [r"my name is (.*)", ["Nice to meet you, %1!"]],
    [r"(.*) your name?", ["I am Zero, Sai's personal chatbot."]],
    [r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!"]],
    [r"bye", ["Goodbye! Have a great day!"]],
    [r"(.*)", ["I'm not sure I understand. Could you rephrase that?"]],
]


class ZeroChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)
        self.memory = load_memory()

    def respond(self, user_input):
        if "my name is" in user_input.lower():
            name = user_input.split("my name is")[-1].strip().title()
            self.memory["user_name"] = name
            save_memory(self.memory)
            return f"Nice to meet you, {name}! I'll remember that."

        if "who am i" in user_input.lower():
            if "user_name" in self.memory:
                return f"You told me your name is {self.memory['user_name']}."
            else:
                return "I don't know your name yet."
        
        if "forget me" in user_input.lower():
            self.memory = {}
            save_memory(self.memory)
            return "Okay, I've forgotten everything about you."

        return self.chat.respond(user_input)

        


def chat_with_zero():
    chatbot = ZeroChatbot(pairs)

    print("Hello, I am Zero! Type 'bye' to exit.")

    if "user_name" in chatbot.memory:
        print(f"Welcome back, {chatbot.memory['user_name']}!")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Zero: Goodbye!")
            break

        response = chatbot.respond(user_input)
        print(f"Zero: {response}")


chat_with_zero()