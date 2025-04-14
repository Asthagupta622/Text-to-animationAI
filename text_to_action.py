import re

# utils/text_to_action.py

def extract_action(input_text):
    actions = {
        "man is swimming": "swimming",
        "man is jumping": "jump",
        # Add more actions here if needed
    }

    # Search for the action in the input text
    for action, action_name in actions.items():
        if action in input_text.lower():
            return action_name
    return None  # If no action found
