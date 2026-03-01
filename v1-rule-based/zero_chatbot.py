import nltk
from nltk.chat.util import Chat, reflections

# Download required resources (only needed first time)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

pairs = [

    # Greetings
    [r"hi|hello|hey",
     ["Hello! I'm Zero 🤖 — Sai's personal chatbot.",
      "Hey there! Zero here. How can I help you?"]],

    # Bot identity
    [r"what is your name|who are you",
     ["I am Zero, a basic rule-based chatbot created by Sai Prajapati."]],

    # About Sai
    [r"(.*) sai(.*)",
     ["Sai Prajapati is a CSE student passionate about Web Development, AI, and Game Development.",
      "Sai is focused on building strong technical skills and preparing for internships."]],

    [r"(.*) about sai(.*)",
     ["Sai Prajapati is currently mastering full-stack development and exploring AI for hackathons."]],

    # Education
    [r"(.*) study(.*)|what does sai do",
     ["Sai is a Computer Science Engineering student balancing academics and skill development."]],

    # Skills
    [r"(.*) skills(.*)|what is sai learning",
     ["Sai is learning JavaScript, backend development, and exploring Artificial Intelligence.",
      "Currently focused on becoming strong in full-stack web development."]],

    # Goals
    [r"(.*) goal(.*)",
     ["Sai's goal is to build powerful projects, grow confidence, and stand out through real skills."]],

    # Hackathons
    [r"(.*) hackathon(.*)",
     ["Sai aims to reach a competitive level in hackathons using AI and development expertise."]],

    # Joke
    [r"tell me a joke",
     ["Why do programmers prefer dark mode? Because light attracts bugs 😄"]],

    # Help
    [r"(.*) help(.*)",
     ["You can ask me about Sai, his skills, goals, or interests!"]],

    # Exit
    [r"bye|exit",
     ["Goodbye! Keep building ",
      "See you soon! Stay consistent 💻🔥"]],

    # Default fallback
    [r"(.*)",
     ["I'm still a basic chatbot and didn't understand that yet 😅",
      "Try asking something about Sai or his goals!"]]
]


class ZeroChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)

    def respond(self, user_input):
        return self.chat.respond(user_input)


def chat_with_zero():
    print("Hello, I am Zero 🤖 — Sai's personal rule-based chatbot.")
    print("Ask me about Sai, his skills, goals, or interests.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Zero: Goodbye! Keep grinding 🚀")
            break

        response = zero.respond(user_input)
        print(f"Zero: {response}")


zero = ZeroChatbot(pairs)
chat_with_zero()