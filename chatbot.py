"""
Simple Python Chatbot with Options Display
"""

def display_options():
    print("Hello! I'm a simple chatbot. Here are some things you can ask me:")
    print("1. Say 'hello' or 'hi'")
    print("2. Ask 'how are you?'")
    print("3. Ask about my name ('what's your name?' or 'your name')")
    print("4. Type 'bye' or 'exit' to end the chat")
    print("Let's chat!")

def chatbot():
    display_options()
    
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, so I don't have feelings, but thanks for asking!")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple chatbot created to assist you.")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you rephrase?")

# Start the chatbot
chatbot()
