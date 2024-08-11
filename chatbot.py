from datetime import datetime

def chatbot():
    print("Namaste! I am your chatbot. You can ask me the following:")
    print("1. 'How are you?' or 'What's up?'")
    print("2. 'What can you do?' or 'What are your capabilities?'")
    print("3. 'Thank you!' or 'Thanks!'")
    print("4. 'Goodbye' or 'Bye'")
    print("5. 'What is the time?' or 'What time is it?'")
    print("6. 'What is the date?' or 'What day is it?'")
    print("7. 'Tell me a joke' or 'Can you make me laugh?'\n")

    while True:
        user_input = input("You: ").strip().lower()

        if any(phrase in user_input for phrase in ['how are you', "what's up", 'how do you do']):

            print("Chatbot: I'm doing well, thank you! How can I assist you today?\n")

        elif any(phrase in user_input for phrase in ['what can you do', 'what are your capabilities', 'what can you do for me']):
            print("Chatbot: I can answer basic questions and help you with common queries. Just ask!\n")

        elif any(phrase in user_input for phrase in ['thank you', 'thanks', 'thanks a lot']):

            print("Chatbot: You're welcome! If you have more questions, feel free to ask.\n")

        elif any(phrase in user_input for phrase in ['goodbye', 'bye', 'see you later']):

            print("Chatbot: Goodbye! Have a great day.\n")
            break

        elif any(phrase in user_input for phrase in ['what is the time', 'what time is it']):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            print(f"Chatbot: The current time is {current_time}.\n")

        elif any(phrase in user_input for phrase in ['what is the date', 'what day is it']):
            today = datetime.now()
            current_date = today.strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {current_date}.\n")

        elif any(phrase in user_input for phrase in ['tell me a joke', 'can you make me laugh']):
            
print("Chatbot:Why was six afraid of seven?\nUser: Why?\nChatbot: Because seven eight (ate) nine!\n")

        else:

            print("Chatbot: I'm not sure how to respond to that. Please ask something from the options above.\n")

chatbot()
