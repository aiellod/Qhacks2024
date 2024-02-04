from openai import OpenAI
import localvars
import settings


class ai:

    client = OpenAI(api_key = localvars.KEY_OPENAI)

    response = None

    log = {}

    def __init__(self, context, prompt):
        self.response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            ]
        )

        self.log = [{"role": "system", "content": context},
           ]
        
            
    def user_response(self, prompt):
        prompt = "Make me a " + prompt + " and say nothing else. Use the fewest tokens possible. Do not state a word that isnt part of my content and do not acknowledge my command."
        self.log.append({"role": "user", "content": prompt})


        self.response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.log
        )

        response = self.response.choices[-1].message.content
        print(response)

        settings.KeyQueue.queue.clear()

        for char in response:
            settings.KeyQueue.put(char)
