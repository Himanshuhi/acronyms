import json

# himanshu
acronyms = {}

try:
    with open("acronyms.json", "r") as f:
        acronyms = json.load(f)
except FileNotFoundError:
    pass

def generate_acronym(phrase):
    acronym = ""
    for word in phrase.split():
        acronym += word[0].upper()
    return acronym

def print_phrase(acronym):
    if acronym in acronyms:
        print(acronyms[acronym])
    else:
        print("No phrase found for acronym", acronym)

while True:
    action = input("Enter 'a' to add a phrase, 'g' to generate an acronym, or 'p' to print a phrase: ")
    
    if action == "a":
        phrase = input("Enter a phrase: ")
        acronym = generate_acronym(phrase)
        acronyms[acronym] = phrase
        with open("acronyms.json", "w") as f:
            json.dump(acronyms, f)
        print("Acronym added:", acronym)
        
    elif action == "g":
        phrase = input("Enter a phrase: ")
        acronym = generate_acronym(phrase)
        print("Generated acronym:", acronym)
        
    elif action == "p":
        acronym = input("Enter an acronym: ")
        print_phrase(acronym)
        
    else:
        print("Invalid input. Please enter 'a', 'g', or 'p'.")
