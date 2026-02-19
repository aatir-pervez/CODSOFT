# Rule-Based Chatbot
# CodSoft AI Internship - Task 1

print("Hello! I am your chatbot.")
print("Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I assist you today?")

    elif "how are you" in user_input:
        print("Bot: I am just a program, but I am functioning perfectly!")

    elif "your name" in user_input:
        print("Bot: I am a simple rule-based chatbot created for the CodSoft internship.")

    elif "help" in user_input:
        print("Bot: I can respond to greetings, basic questions, and simple queries.")

    else:
        print("Bot: I'm sorry, I don't understand that. Can you rephrase?")
