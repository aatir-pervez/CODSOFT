# Rule-Based Chatbot
# CodSoft AI Internship - Task 1

def get_response(user_input):
    user_input = user_input.lower()

    if user_input == "exit":
        return "Goodbye! Have a great day."

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I am functioning perfectly. Thanks for asking!"

    elif "your name" in user_input:
        return "I am a rule-based chatbot created for the CodSoft AI Internship."

    elif "help" in user_input:
        return "You can greet me, ask my name, or ask how I am."

    elif "internship" in user_input:
        return "This chatbot was developed as part of the CodSoft Artificial Intelligence Internship."

    else:
        return "I'm sorry, I don't understand that. Please try something else."


def main():
    print("Hello! I am your chatbot.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "exit":
            break


if __name__ == "__main__":
    main()
