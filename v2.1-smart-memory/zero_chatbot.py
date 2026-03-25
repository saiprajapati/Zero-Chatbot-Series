import json
import os

MEMORY_FILE = "memory.json"


# ---------------- MEMORY HANDLING ---------------- #

def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


# ---------------- CHATBOT ---------------- #

class ZeroChatbot:
    def __init__(self):
        self.memory = load_memory()

    def respond(self, user_input):
        user_input = user_input.lower()

        # -------- NAME -------- #
        if "my name is" in user_input:
            name = user_input.split("my name is")[-1].strip().title()
            self.memory["user_name"] = name
            save_memory(self.memory)
            return f"Nice to meet you, {name}! I'll remember that."

        if "who am i" in user_input:
            if "user_name" in self.memory:
                return f"You told me your name is {self.memory['user_name']}."
            return "I don't know your name yet."

        # -------- INTEREST -------- #
        if "i am interested in" in user_input:
            interest = user_input.split("i am interested in")[-1].strip().upper()
            self.memory["interest"] = interest
            save_memory(self.memory)
            return f"Got it. You're interested in {interest}. That's a strong field."

        # -------- GOAL -------- #
        if "my goal is" in user_input:
            goal = user_input.split("my goal is")[-1].strip()
            self.memory["goal"] = goal
            save_memory(self.memory)
            return f"That's a solid goal: {goal}. Stay consistent and you'll get there."

        # -------- SHOW MEMORY -------- #
        if "what do you know about me" in user_input:
            if not self.memory:
                return "I don't know much about you yet. Try telling me your name, interests, or goals."

            info = []
            if "user_name" in self.memory:
                info.append(f"Name: {self.memory['user_name']}")
            if "interest" in self.memory:
                info.append(f"Interest: {self.memory['interest']}")
            if "goal" in self.memory:
                info.append(f"Goal: {self.memory['goal']}")

            return "Here's what I know about you:\n- " + "\n- ".join(info)

        # -------- FORGET MEMORY -------- #
        if "forget me" in user_input:
            self.memory = {}
            save_memory(self.memory)
            return "Done. I've cleared everything I knew about you."

        # -------- ABOUT SAI -------- #
        if "who is sai" in user_input or "about sai" in user_input:
            return (
                "Sai Prajapati is a Computer Science Engineering student focused on building strong skills.\n"
                "He is currently working on:\n"
                "- Full-stack web development\n"
                "- Artificial Intelligence for hackathons\n"
                "- Future goal: Game Development\n"
                "He is preparing for internships and aiming to stand out through real projects."
            )

        if "skills" in user_input:
            return (
                "Sai is developing skills in:\n"
                "- JavaScript and backend development\n"
                "- AI/ML fundamentals\n"
                "- Problem solving and system building\n"
                "Focus is on building strong, real-world projects."
            )

        if "goal" in user_input:
            return (
                "Sai's main goal is to:\n"
                "- Become highly skilled in development\n"
                "- Crack strong internships\n"
                "- Build impactful projects\n"
                "- Compete and win in hackathons"
            )

        # -------- JOKE -------- #
        if "joke" in user_input:
            return "Why do programmers prefer dark mode? Because light attracts bugs 😄"

        # -------- GREETING -------- #
        if any(word in user_input for word in ["hi", "hello", "hey"]):
            if "user_name" in self.memory:
                return f"Hey {self.memory['user_name']}! What do you want to work on today?"
            return "Hello! I'm Zero. You can tell me about yourself or ask about Sai."

        # -------- DEFAULT -------- #
        return (
            "I'm still learning. Try asking things like:\n"
            "- My name is ...\n"
            "- I am interested in ...\n"
            "- My goal is ...\n"
            "- What do you know about me?\n"
            "- Who is Sai?"
        )


# ---------------- MAIN LOOP ---------------- #

def chat_with_zero():
    bot = ZeroChatbot()

    print("Zero 🤖 - Smart Assistant (v2.1)")
    print("Type 'bye' to exit.\n")

    if "user_name" in bot.memory:
        print(f"Welcome back, {bot.memory['user_name']}!\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Zero: Goodbye! Keep building 🚀")
            break

        response = bot.respond(user_input)
        print(f"Zero: {response}")


chat_with_zero()