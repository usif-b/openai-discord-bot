import requests
import config

class HttpRequestHandler:
    def __init__(self):
        self.textUrl = 'https://api.openai.com/v1/completions'
        self.imageUrl = 'https://api.openai.com/v1/images/generations'
        self.headers = {'Authorization' : f'Bearer {config.API_KEY}'}
    
    def text(self, prompt):
        data = {
            'model' : 'gpt-3.5-turbo-0301',
            'messages' : [{'role': 'user', 'content' : prompt}]
        }
        response = requests.post(self.textUrl, headers = self.headers, json = data)
        return response.json()['choices'][0]['message']['content']

    def image(self, prompt):
        data = {
            'prompt': prompt,
        }
        response = requests.post(self.imageUrl, headers = self.headers, json = data)
        imageUrl = response.json()['data'][0]['url']
        return imageUrl