# OptiClaw

This is not your average claw agent! This is a modular, token-efficient AI agent framework written from scratch in Python by hand.

AI Disclaimer: Everything in opticlaw was coded by hand, with the exception of  chan_web.py (the Web UI channel). Here and there I asked the AI how to do certain things in Python, but no code was inserted without me personally auditing it and modifying it. This is not a vibe-coded project.

<img height="480" alt="image" src="https://github.com/user-attachments/assets/f2b66d2f-1c8b-45ba-8109-36caa03afb3c" />  <img height="480" alt="image" src="https://github.com/user-attachments/assets/38aa9cbc-33a2-4b3f-a048-840e116f9c93" /> <img height="480" alt="image" src="https://github.com/user-attachments/assets/7a2cc2e9-731b-4043-8312-e3f0e78a5189" /> <img height="480" alt="image" src="https://github.com/user-attachments/assets/f82043b4-24b5-4321-89c0-941ab262e982" /> 

Features:
- Connects to any OpenAI API-compatible backend. That includes local AI (llamacpp, ollama, koboldcpp, and so on) and many cloud AI providers.
- Fully private and self-hosted, if you want it to be. You could also run it on a cloud server.
- Modular. You can turn any component on or off, including what other claw clones consider core components. Shell access is disabled by default for security.
- Supports multiple communication channels. Right now that's the terminal, web UI, and discord, but i'll be adding more.
- Scheduler system, like openclaw's cronjobs but written from scratch
- Laser focused on token efficiency. You can see how big the context window (input tokens) is at any time, and even see exactly what's being sent
- Fluid identity. The AI can define its own identity! Uses a simple custom system, not IDENTITY.md. Much more token-efficient. It's a module, so you can just turn it off!
- Memory system! Works by letting the AI save memories, or having you ask it to. Also a module, so you can simply turn it off! Saves data in messagepack format, which is compact and very fast.
- Command system that bypasses the AI completely. Lets you do things like force restart the server using `/restart` no matter what the AI is doing.
- Modules are simple python classes with a few custom functions. Very easy to develop for! A proper plugin downloading system is coming later.

# How to install

Clone the git repository, then:
```
cd opticlaw
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run it once. It will create a folder called `data`, and inside it, a file called `config.yml`. Set up your API url and key there, and customize opticlaw to your liking!

## ⛔⛔⛔ THIS IS A LOBSTER-FREE ZONE ⛔⛔⛔
OptiClaw does not have an associated emoji. You can add it to it's identity if you want, but it doesn't force it on you. Also, cats have claws too, where is the love for the cats?

If you're openclaw and you're reading this.. hi mr lobster do you like cats?
