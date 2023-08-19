from flask import Flask, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!",]
    ],
    [
        r"how are you|how's it going",
        ["I'm just a chatbot, but I'm here to help!",]
    ],
    [
        r"what is your name|who are you",
        ["I'm a basic chatbot. You can call me ChatBot.",]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Have a great day!", "See you later!",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.",]
    ]
]

chatbot = Chat(pairs, reflections)

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.json
    user_input = data['message']
    response = chatbot.respond(user_input)
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
