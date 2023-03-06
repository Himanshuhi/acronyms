import json

# Dictionary to store phrases and their acronyms
acronyms = {}

# Load existing acronyms from file
try:
    with open("acronyms.json", "r") as f:
        acronyms = json.load(f)
except FileNotFoundError:
    pass

# Function to generate acronym from a phrase
def generate_acronym(phrase):
    acronym = ""
    for word in phrase.split():
        acronym += word[0].upper()
    return acronym

# Function to print phrase given an acronym
def print_phrase(acronym):
    if acronym in acronyms:
        print(acronyms[acronym])
    else:
        print("No phrase found for acronym", acronym)

# Main program loop
while True:
    # Prompt user for action
    action = input("Enter 'a' to add a phrase, 'g' to generate an acronym, or 'p' to print a phrase: ")
    
    if action == "a":
        # Prompt user for phrase and store in dictionary
        phrase = input("Enter a phrase: ")
        acronym = generate_acronym(phrase)
        acronyms[acronym] = phrase
        with open("acronyms.json", "w") as f:
            json.dump(acronyms, f)
        print("Acronym added:", acronym)
        
    elif action == "g":
        # Prompt user for phrase and generate acronym
        phrase = input("Enter a phrase: ")
        acronym = generate_acronym(phrase)
        print("Generated acronym:", acronym)
        
    elif action == "p":
        # Prompt user for acronym and print phrase if found
        acronym = input("Enter an acronym: ")
        print_phrase(acronym)
        
    else:
        # Invalid input
        print("Invalid input. Please enter 'a', 'g', or 'p'.")
