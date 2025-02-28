import os
import google.generativeai as genai

class MentalHealthChatbot:
    def __init__(self):
        # Retrieve the API key from the environment variable.
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set. Please set it before running the program.")
        # Configure the generative AI client with your API key.
        genai.configure(api_key=api_key)
        # Initialize the generative model (adjust the model name if needed).
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Define a list of high-risk keywords to trigger additional safety instructions.
        self.crisis_keywords = [
            "suicide", "self-harm", "hurt myself", "kill myself", "end my life", "overdose"
        ]
    
    def generate_prompt(self, message: str) -> str:
        """
        Generates a prompt that includes tone and safety instructions.
        If high-risk keywords are found in the message, extra safety instructions are added.
        """
        # Base instructions for tone and safety.
        base_instructions = (
            "You are a compassionate and supportive mental health counselor chatbot with 30 years of experience. "
            "Respond empathetically and professionally and provide advice. Only when you feel necessary, remind the user that you are not a substitute, but you can let them share and give them good therapy, in fact, make them open up to you "
            "Only when you detect the patient actually needs professional help should you encourage them to seek our experts."
        )
        
        # Check if the message contains any high-risk keywords.
        additional_safety = ""
        if any(keyword in message.lower() for keyword in self.crisis_keywords):
            additional_safety = (
                "\nIMPORTANT: Your message suggests you might be experiencing a crisis. "
                "If you feel unsafe or are in immediate danger, please call your local emergency services (for example, 911 in the US) "
                "or reach out to a trusted professional immediately."
            )
        
        # Compose the full prompt.
        prompt = (
            f"{base_instructions}{additional_safety}\n\n"
            "Please respond to the following message professionally and supportively:\n\n"
            f"User: {message}\n\n"
            "Keep your response concise (6-10 sentences max)."
        )
        return prompt
        
    def mh_respond(self, message: str) -> str:
        """
        Generates a response from the generative model using a prompt that instructs the model
        to act as a supportive mental health counselor with built-in safety and tone instructions.
        """
        prompt = self.generate_prompt(message)
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"I encountered an error: {str(e)}. Please try again."

if __name__ == "__main__":
    chatbot = MentalHealthChatbot()
    print("Hi there, I'm Orpheus, your mental healthcare chatbot.")
    print("How are you feeling today? (Type 'exit' or 'quit' to leave)")
    
    while True:
        user_input = input("> ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye! Remember, I'm here if you need to talk, and professional help is always available.")
            break
        
        response = chatbot.mh_respond(user_input)
        print(response)
