import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a bot created by you. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good, How about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon!",]
    ]
]

def chatbot():
    print("Hi, I'm Chatbot and I like to chat\nPlease type lowercase English language to start a conversation.\nType 'quit' to leave ")
    chat = Chat(pairs, reflections)
    chat.converse()

# Call the chatbot function
chatbot()
