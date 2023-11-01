from nltk.chat.util import Chat, reflections
from flask import Flask, request, render_template

app = Flask(__name__)

# Define patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),  # Greetings pattern and responses
    (r'how are you', ["I'm good, thanks. How can I help you?"]),  # Inquiry about chatbot's well-being
    (r'what is your name|your name', ["I'm a chatbot. You can call me ChatBuddy."]),  # Inquiry about chatbot's name
    (r'(.*) your name?', ["I'm a chatbot. You can call me ChatBuddy."]),  # Extracting chatbot's name
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),  # Farewell pattern
]

# Create a Chat instance
chatbot = Chat(patterns, reflections)

@app.route('/')
def chatbot_interface():
    return render_template('index.html')  # Render the HTML template for the chat interface

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input'].lower()  # Get the user's input from the HTML form
    response = chatbot.respond(user_input)  # Use the Chat instance to generate a response

    # Check if the response is the fallback response
    if response not in [response for pattern, responses in patterns for response in responses]:
        response = "I'm sorry for any confusion, but I'm a text-based AI model, and I'm unable to understand your request."

    return response  # Return the response to the client

if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask application in debug mode
