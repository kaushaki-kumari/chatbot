import json

DEFAULT_REPLY = "I'm sorry, I don’t have information about that. Please email us at support@example.com."

def load_data(file_path='data.json'):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: data.json not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in data.json.")
        return {}

def get_response(user_input, rules):
    user_input = user_input.lower().strip()
    return rules.get(user_input, DEFAULT_REPLY)

def chat():
    print("🤖 Chatbot is running! Type 'exit' to quit.\n")
    rules = load_data()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break
        response = get_response(user_input, rules)
        print("Bot:", response)

if __name__ == "__main__":
    chat()
