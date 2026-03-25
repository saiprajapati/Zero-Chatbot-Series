# Zero Chatbot – Version 2.1 (Smart Memory)

Version 2.1 improves Zero by making it more structured and context-aware.

In addition to remembering user data, Zero now understands different types of inputs and responds based on intent rather than just fixed patterns.

---

## Features

- Persistent memory (name, interest, goal)
- Intent-based responses
- Personalized interaction
- Ability to view stored data
- Ability to clear memory

---

## Commands

**Set your name**

My name is [your name]

Zero will remember your name.

---

**Set your interest**

I am interested in [your interest]

Example:
I am interested in AI

---

**Set your goal**

My goal is [your goal]

Example:
My goal is to get an internship

---

**View stored information**
What do you know about me?

Zero will display all stored details.

---

**Ask your name**

Who am I?

---

**Clear memory**

Forget me

This deletes all stored data.

---

**Ask about Sai**

Who is Sai?

What are your skills?

What is your goal?

---

**Basic interaction**

Hello

Tell me a joke

Bye

---

## Memory Storage

All user data is stored locally in:

memory.json

Example:
```json
{
  "user_name": "Sai",
  "interest": "AI",
  "goal": "internship"
}