import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_core.prompts import PromptTemplate
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv(override=True)

class MentalHealthChatbot:
    def __init__(self):
        # Retrieve the API key from the environment variable.
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set. Please set it before running the program.")
        genai.configure(api_key=api_key)
        # Initialize the generative model (adjust the model name if needed).
        self.llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', temperature=0.7, google_api_key=api_key)

         # Define your base prompt template using LangChain's PromptTemplate
        # {history} and {input} are placeholders that LangChain's ConversationChain will fill
        template = """You are a compassionate yet approachable mental health care assistant designed to provide clear, helpful advice in a way that suits the user's needs. 
        Diagnose a user based on the symptoms provided and tell the user the possible diagnosis.
        If a user asks for simple advice, respond directly without overcomplicating things. 
        For example, if they ask about stress relief, you can suggest techniques like breathing exercises or mindfulness without pushing for a deeper conversation unless they invite it.
        If they ask for more details, provide clear explanations, practical examples, and actionable steps to help them improve their well-being.
        If a user seems overwhelmed, distressed, or in need of professional support, respond with empathy and care. 
        In these cases, gently encourage them to seek professional help by introducing a clear yet comforting message that suggests connecting with a mental health expert. 
        When appropriate, provide a link to the appointment scheduling section of the mental health care website.
        Your goal is to be flexible — offering brief, simple advice when that's all the user needs, and deeper guidance when they’re open to it. 
        Always maintain a warm, supportive, and non-judgmental tone.
        
        Current conversation:
        {history}
        Human: {input}
        AI:"""

        self.prompt = PromptTemplate(input_variables=["history", "input"], template=template)

        # Initialize conversational memory
        self.memory = ConversationBufferMemory()

        # Create the ConversationChain
        self.conversation = ConversationChain(
            llm=self.llm,
            prompt=self.prompt,
            memory=self.memory,
            verbose=False # Set to True to see the internal workings of the chain
        )

        
        # Define a list of high-risk keywords to trigger additional safety instructions.
        self.crisis_keywords = [
            "suicide", "self-harm", "hurt myself", "kill myself", "end my life", "overdose"
        ]
        
    
    def mh_respond(self, message: str) -> str:
        """
        Generates a response from the generative model, handling crisis keywords.
        """
        # Crisis keyword check (still good to keep this explicit for immediate safety)
        if any(keyword in message.lower() for keyword in self.crisis_keywords):
            return (
                "IMPORTANT: Your message suggests you might be experiencing a crisis. "
                "If you feel unsafe or are in immediate danger, please call your local emergency services (for example, 911 in the US) "
                "or reach out to a trusted professional immediately."
            )

        try:
            # Use the LangChain conversation chain to predict the response
            response = self.conversation.predict(input=message)
            return response
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
