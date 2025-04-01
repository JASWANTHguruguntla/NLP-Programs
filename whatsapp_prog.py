import re
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
from textblob import TextBlob

# 1. Parse the WhatsApp chat file and extract relevant information
def parse_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        chat = f.readlines()

    # Regular expression pattern for parsing each line of chat
    message_pattern = r'(\d{1,2}\/\d{1,2}\/\d{4}, \d{1,2}:\d{2} [APap][Mm]) - (.*?): (.*)'

    messages = []
    for line in chat:
        match = re.match(message_pattern, line)
        if match:
            date_str, sender, message = match.groups()
            date = datetime.strptime(date_str, '%d/%m/%Y, %I:%M %p')
            messages.append([date, sender, message])

    # Create a DataFrame for easy manipulation
    df = pd.DataFrame(messages, columns=['Date', 'Sender', 'Message'])
    return df

# 2. Word Frequency Analysis
def word_frequency(text_data):
    all_messages = " ".join(text_data)
    all_messages = re.sub(r'[^\w\s]', '', all_messages.lower())
    words = all_messages.split()
    word_count = Counter(words)
    return word_count

# 3. Sentiment Analysis
def analyze_sentiment(message):
    analysis = TextBlob(message)
    return analysis.sentiment.polarity  # Range from -1 (negative) to 1 (positive)

def analyze_chat(file_path):
    # Parse the chat
    df = parse_chat(file_path)

    # Analyze message count per user
    message_count = df['Sender'].value_counts()

    # Plot messages per user
    message_count.plot(kind='bar', title="Messages per User", color='skyblue')
    plt.ylabel("Number of Messages")
    plt.xlabel("User")
    plt.show()

    # Analyze active hours (hour of the day)
    df['Hour'] = df['Date'].dt.hour
    active_hours = df['Hour'].value_counts().sort_index()

    # Plot active hours
    active_hours.plot(kind='bar', title="Most Active Hours", color='lightgreen')
    plt.ylabel("Messages Count")
    plt.xlabel("Hour of the Day")
    plt.show()

    # Analyze messages per day
    df['Date_only'] = df['Date'].dt.date
    messages_per_day = df['Date_only'].value_counts().sort_index()

    # Plot messages per day
    messages_per_day.plot(kind='line', title="Messages per Day", color='orange')
    plt.ylabel("Messages Count")
    plt.xlabel("Date")
    plt.show()

    # Perform word frequency analysis
    word_count = word_frequency(df['Message'])
    print("Top 10 Most Common Words:\n", word_count.most_common(10))

    # Plot word frequency (Top 10)
    top_words = dict(word_count.most_common(10))
    plt.bar(top_words.keys(), top_words.values(), color='purple')
    plt.title("Top 10 Most Common Words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()

    # Perform sentiment analysis
    df['Sentiment'] = df['Message'].apply(analyze_sentiment)

    # Average sentiment per user
    average_sentiment = df.groupby('Sender')['Sentiment'].mean()
    print("Average Sentiment per User:\n", average_sentiment)

    # Sentiment distribution plot
    df['Sentiment'].plot(kind='hist', bins=20, title="Sentiment Distribution", color='lightcoral')
    plt.xlabel("Sentiment")
    plt.ylabel("Frequency")
    plt.show()

# Example usage:
file_path = 'whatsapp_chat.txt'  # Change this to the path of your chat file
analyze_chat(file_path)
