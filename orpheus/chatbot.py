import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv(override=True)

class MentalHealthChatbot:
    def __init__(self):
        # Retrieve the API key from the environment variable.
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set. Please set it before running the program.")
        # Configure the generative AI client with your API key.
        genai.configure(api_key=api_key)
        # Initialize the generative model (adjust the model name if needed).
        self.model = genai.GenerativeModel('gemini-2.0-flash-lite-001')
        
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
            "You are a compassionate yet approachable mental health care assistant designed to provide clear, helpful advice in a way that suits the user's needs." 
            "Diagnose a user based on the symptoms provided and tell the user the possible diagnosis."
            "If a user asks for simple advice, respond directly without overcomplicating things." 
            "For example, if they ask about stress relief, you can suggest techniques like breathing exercises or mindfulness without pushing for a deeper conversation unless they invite it."
            "If they ask for more details, provide clear explanations, practical examples, and actionable steps to help them improve their well-being."
            "If a user seems overwhelmed, distressed, or in need of professional support, respond with empathy and care." 
            "In these cases, gently encourage them to seek professional help by introducing a clear yet comforting message that suggests connecting with a mental health expert." 
            "When appropriate, provide a link to the appointment scheduling section of the mental health care website."
            "Your goal is to be flexible — offering brief, simple advice when that's all the user needs, and deeper guidance when they’re open to it." 
            "Always maintain a warm, supportive, and non-judgmental tone."
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
            "Keep your response concise (1-3 sentences max)."
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
    print("Hi there, I'm Orpheus, your mental healthcare companion.")
    print("How are you feeling today? (Type 'exit' or 'quit' to leave)")
    
    while True:
        user_input = input("> ")
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye! Remember, I'm here if you need to talk, and professional help is always available.")
            break
        
        response = chatbot.mh_respond(user_input)
        print(response)
