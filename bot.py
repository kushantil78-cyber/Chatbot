# ==========================================
# AI MINI PROJECT
# Simple AI Chatbot
# ==========================================

print("===================================")
print("       🤖 SIMPLE AI CHATBOT")
print("===================================")

print("Hello! I am your AI-style chatbot.")
print("You can ask me simple questions.")
print("Type 'bye' to exit the chatbot.\n")


def chatbot_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! Nice to meet you 😊"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    elif "your name" in user_input:
        return "My name is Python AI Chatbot."

    elif "python" in user_input:
        return "Python is a popular programming language used in AI, data science and web development."

    elif "machine learning" in user_input:
        return "Machine Learning allows computers to learn patterns from data and make predictions."

    elif "artificial intelligence" in user_input or "ai" in user_input:
        return "AI is the field of creating systems that can perform tasks that normally require human intelligence."

    elif "thank" in user_input:
        return "You're welcome! 😊"

    elif "bye" in user_input:
        return "Goodbye! Have a great day! 👋"

    else:
        return "I'm still learning. Try asking me about Python, AI or Machine Learning."


while True:

    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if "bye" in user_input.lower():
        break


print("\n===================================")
print("       CHATBOT SESSION ENDED")
print("===================================")