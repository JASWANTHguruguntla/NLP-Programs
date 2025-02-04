import nltk

# Ensure the necessary resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

def get_parts_of_speech(sentence):
    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    # Tag the tokens with their parts of speech
    pos_tags = pos_tag(tokens)
    return pos_tags

while True:
    # Take input from the user
    sentence = input("Enter a sentence (or type 'exit' to quit): ")
    if sentence.lower() == 'exit':
        break
    pos_tags = get_parts_of_speech(sentence)

    # Print the parts of speech
    print("\nParts of Speech:")
    for word, tag in pos_tags:
        print(f"{word}: {tag}")
    print("\n")
