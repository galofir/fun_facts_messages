import os
import requests
from twilio.rest import Client

def get_fact():
    # Fetching a random fact
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    return response.json()['text']

def send_whatsapp(fact):
    # These variables will be pulled from GitHub Secrets for safety
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    to_number = os.environ['MY_PHONE_NUMBER'] 
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_='whatsapp:+14155238886', # Default Twilio Sandbox number
        body=f"🌟 Daily Fact: {fact}",
        to=f"whatsapp:{to_number}"
    )
    print(f"Message sent! SID: {message.sid}")

if __name__ == "__main__":
    try:
        fact = get_fact()
        send_whatsapp(fact)
    except Exception as e:
        print(f"Error: {e}")
