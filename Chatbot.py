import random
import re

class AdvancedChatBot:
    def __init__(self):
        self.user_name = None
        self.memory = []

    def greet(self):
        greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Nice to meet you!"]
        return random.choice(greetings)

    def ask_name(self):
        return "I don't think I know your name yet. What should I call you?"

    def detect_malaria(self, symptoms):
        malaria_symptoms = {"fever", "chills", "headache", "sweating", "vomiting", "muscle pain", "fatigue"}
        reported = set(symptoms.lower().split(","))
        matched = malaria_symptoms.intersection(reported)
        if len(matched) >= 3:
            return (
                f"It seems you're experiencing {', '.join(matched)}. "
                "These could be symptoms of malaria. Please consult a doctor immediately."
            )
        elif matched:
            return f"You have {', '.join(matched)} — a few common symptoms, but not enough for concern. Stay alert and hydrated!"
        else:
            return "Your symptoms don't strongly match malaria indicators. But if you feel unwell, see a doctor!"

    def respond_to_input(self, user_input):
        self.memory.append(user_input)  # store input for future context
        user_input = user_input.lower().strip()
        
        if user_input == "bye":
            return "Goodbye! Have a wonderful day!"

        
        elif user_input in ["hi", "hello", "hey", "good morning", "good evening"]:
            return self.greet()

        
        elif re.search(r"\b(your name|who are you)\b", user_input):
            return "I'm ChadBot, your friendly AI companion."

        
        elif "how are you" in user_input:
            return "I'm just code, but I'm feeling chatty today!"
        
        elif re.match(r"my name is", user_input):
            self.user_name = user_input.split("is")[-1].strip().capitalize()
            return f"Nice to meet you, {self.user_name}!"

        elif self.user_name and "my name" in user_input:
            return f"You already told me your name is {self.user_name}, right?"

        elif "what is my name" in user_input:
            return f"Your name is {self.user_name}!" if self.user_name else self.ask_name()

    
        elif "joke" in user_input:
            jokes = [
                "Why did the computer get cold? Because it forgot to close its Windows!",
                "Why don't programmers like nature? It has too many bugs.",
                "What do you call 8 hobbits? A hob-byte!"
            ]
            return random.choice(jokes)

    
        elif "malaria" in user_input or "symptom" in user_input:
            return (
                "Please list your symptoms separated by commas (e.g., fever, chills, headache):"
            )

        elif any(symptom in user_input for symptom in ["fever", "chills", "headache", "vomiting", "fatigue", "sweating", "muscle pain"]):
            return self.detect_malaria(user_input)

        
        elif "help" in user_input:
            return (
                "I can chat with you, tell jokes, remember your name, help with malaria symptom checking, or say goodbye."
            )

        
        else:
            return "Hmm, I didn't understand that. Can you rephrase?"

    def chat(self):
        print("ChadBot: Hello! I'm ChadBot. Type 'bye' to exit.\n")

        while True:
            user_input = input("You: ")
            response = self.respond_to_input(user_input)
            print(f"ChadBot: {response}")
            if response.startswith("Goodbye"):
                break



if __name__ == "__main__":
    bot = AdvancedChatBot()
    bot.chat()
