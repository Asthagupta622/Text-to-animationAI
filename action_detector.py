import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_action(text):
    doc = nlp(text)
    for token in doc:
        if token.pos_ == "VERB":
            return token.lemma_.lower()
    return "idle"

# Example usage
if __name__ == "__main__":
    user_text = input("Enter your command: ")
    action = extract_action(user_text)
    print("Extracted action:", action)

    with open("action.txt", "w") as f:
        f.write(action)
