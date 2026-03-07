# Zero Chatbot – Version 2.0 (Persistent Memory)

Version 2.0 of **Zero** introduces persistent memory.

Unlike the previous version, Zero can now remember information about the user and retrieve it in future conversations. The memory is stored using a simple JSON file, allowing the chatbot to recognize returning users even after the program is restarted.

---

## What’s New in v2

- Persistent memory using JSON storage
- Zero remembers the user's name
- Returning users are greeted automatically
- Basic conversational context added

---

## Commands

Zero supports a few simple commands to demonstrate its features.

- **Introduce yourself**
Zero will store your name and remember it for future sessions.

- **Ask Zero who you are**
Zero will retrieve your stored name from memory.

- **Clear stored memory**
Zero will delete the stored user data from `memory.json`.

- **Basic interaction**
Hello,
Tell me a joke,
Bye