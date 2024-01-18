from fuzzywuzzy import fuzz
import re



class MentalHealthChatbot:

    def __init__(self):
        self.diagnosis_pairs = [
            [
                r"(.*)(feel|feeling|felt|been feeling|not feeling|been having)",
                ["I'm very sorry to hear that, can you describe how you've been feeling?"],
            ],
        ]
        self.anxiety_pairs = [
            [
                r"(.*)nervous|restless|muscle tension|on edge|panic attacks|danger|overthinking|worry|",
                ["You seem to be experiencing anxiety, can you tell me more about how it's impacting your daily life?"],
            ],
            [
                r"(.*)its too much",
                [
                    "It sounds like you're feeling overwhelmed, have you tried any strategies to help reduce your anxiety?"],
            ]
        ]
        self.depression_pairs = [
            [
                r"(.*)sad|hopeless|tired|worthless|drained|",
                ["It seems like you might be experiencing %1 , can you tell me more about how you're feeling?"],
            ],
            [
                r"(.*)its too much",
                [
                    "It sounds like you're feeling hopeless, have you considered talking to a professional about your feelings?"],
            ]
        ]
        self.adhd_pairs = [
            [
                r"I can't seem to focus",
                [
                    "It seems like you might be experiencing ADHD, have you tried breaking your tasks down into smaller, more manageable pieces?"],
            ],
            [
                r"yes|yes I have|(.*)",
                ["Have you talked to a therapist?", "That's good then, "],
            ],
            [
                r"no(.*)",
                ["you should talk to a therapist, it is always good to seek professional advice"],
            ],
            [
                r"Thank you|sure|alright",
                ["You're welcome, never forget to seek help, you are not alone in this"],
            ],
        ]
        self.sleep_disorder_pairs = [
            [
                r"I have trouble sleeping",
                ["You seem to be experiencing sleep disorder, what else do you feel?"],
            ],
            [
                r"(.*)its too much",
                ["You seem to be overwhelmed by it. Have you tried medications?"],
            ],
        ]

        self.current_pair = None

    def chatbot_response(self, message):
        for pairs in [self.diagnosis_pairs, self.anxiety_pairs, self.depression_pairs, self.adhd_pairs,
                      self.sleep_disorder_pairs]:
            for pattern, responses in pairs:
                if re.search(pattern, message, re.IGNORECASE):
                    response = responses[0]
                    if len(responses) > 1:
                        responses.pop(0)
                    return response.format(*message.split())
        return None

    def mh_respond(self, message):

        if self.current_pair:

            for pattern, responses in self.current_pair:
                match = fuzz.token_set_ratio(pattern, message)
                if match > 60:

                    response = self.chatbot_response(pattern)
                    if response:
                        return response.format(*message.split())


            self.current_pair = None

        for pair in [self.diagnosis_pairs, self.anxiety_pairs, self.depression_pairs, self.adhd_pairs,
                     self.sleep_disorder_pairs]:
            for pattern, responses in pair:
                match = fuzz.token_set_ratio(pattern, message)
                if match > 60:
                    self.current_pair = pair
                    response = self.chatbot_response(message)
                    if response:
                        return response.format(*message.split())


        return "I'm sorry, can you please rephrase that?"


if __name__ == "__main__":

    chatbot = MentalHealthChatbot()
    print("Hi there, I'm orpheus, a mental healthcare chatbot")
    print("How are you feeling today?")
    while True:
        user_input = input("> ")
        response = chatbot.mh_respond(user_input)
        print(response)