import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def read_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        chat_text = file.read()
    return chat_text

def extract_messages(chat_text):
    # Define a regular expression pattern for extracting messages
    pattern = re.compile(r'(\d{1,2}/\d{1,2}/\d{2,4},? \d{1,2}:\d{2}(?: [APMapm]{2})? - .+?: .+)')
    
    # Extract messages using the pattern
    messages = re.findall(pattern, chat_text)
    
    return messages

def analyze_participants(messages):
    participants = set()
    
    for message in messages:
        sender = re.search(r' - (.+?):', message)
        if sender:
            participants.add(sender.group(1))
    
    return participants

def filter_messages_by_participant(messages, participant_name):
    # Filter messages to only include those from the specified participant
    filtered_messages = [message for message in messages if re.search(r' - (.+?):', message).group(1).lower() == participant_name.lower()]
    return filtered_messages

def plot_message_frequency(messages):
    senders = [re.search(r' - (.+?):', message).group(1) for message in messages if re.search(r' - (.+?):', message)]
    counter = Counter(senders)
    
    plt.bar(counter.keys(), counter.values())
    plt.xlabel('Participants')
    plt.ylabel('Number of Messages')
    plt.title('Message Frequency by Participant')
    plt.show()

def generate_wordcloud(chat_text):
    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = set(["media", "omitted"]), 
                min_font_size = 10).generate(chat_text)
    
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.show()

def print_messages(messages):
    for message in messages:
        print(message)

if __name__ == "__main__":
    file_path = "whatsapp_chat.txt"  #'path_to_your_chat_file.txt'  # Replace with the path to your exported WhatsApp chat file
    chat_text = read_chat(file_path)
    messages = extract_messages(chat_text)

    participants = analyze_participants(messages)
    print("Participants:", participants)
    
    # Get the participant name as input
    participant_name = input("Enter the name of the participant to filter the chat: ")

    # Filter and print messages for the specified participant
    filtered_messages = filter_messages_by_participant(messages, participant_name)
    if filtered_messages:
        print(f"Chat for {participant_name}:")
        print_messages(filtered_messages)
    else:
        print(f"No messages found for {participant_name}.")
    
    # Optional: You can still plot the message frequency and generate wordcloud
    plot_message_frequency(messages)
    generate_wordcloud(chat_text)
