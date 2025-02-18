import nltk
from nltk import CFG

# Define a simple grammar for natural language (CFG)
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP | V
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'ball'
    V -> 'chased' | 'saw' | 'liked'
""")

# Create a parser using Top-Down Parsing (Recursive Descent Parser)
parser = nltk.RecursiveDescentParser(grammar)

# Get input from the user
sentence = input("Enter a simple sentence").lower().split()
#the cat chased a dog
# Parse the sentence
print("\nParsing Tree:")
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()  # Visual representation
