import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_KEY")

def get_url(data):
      headers = {'authorization': API_TOKEN}
      response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=data)
      url = response.json()["upload_url"]
      return url

def get_transcribe_id(url):
      endpoint = "https://api.assemblyai.com/v2/transcript"
      json = {
        "audio_url": url,
        "language_code": "ru"
      }
      headers = {
        "authorization": API_TOKEN,
        "content-type": "application/json"
      }
      response = requests.post(endpoint, json=json, headers=headers)
      id_response = response.json()['id']
      return id_response

def get_text(transcribe_id):
      endpoint = f"https://api.assemblyai.com/v2/transcript/{transcribe_id}"
      headers = {
        "authorization": API_TOKEN
      }
      result = {}
      while result.get("status") != 'completed':
        print("Ожидание...")
        result = requests.get(endpoint, headers=headers).json()
        if result["status"] == 'completed':
            return result
        elif result["status"] == 'failed':
            raise Exception("Transcription failed")


