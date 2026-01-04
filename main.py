import time
import random
import os 
from google import genai 

API_KEY = os.environ.get("google_key2") 
client = genai.Client(api_key=API_KEY)

def send_notification(price):
    print(f"\n[ALERT]: Price {price} ho gaya!")

def ai_generate_message(price, business_name):
    prompt = f"Professional 1-line business message: {business_name} needs 100kg makhana as price is {price}."
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest", 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI Error: {e}"

# --- Logic ---
active = True
target_price = 150

print("Agent: Secure monitoring shuru...\n")

while active:
    current_price = random.randint(100, 200)
    if current_price <= target_price:
        send_notification(current_price)
        msg = ai_generate_message(current_price, "Makhana King")
        print(f"AI Message: {msg}")
        active = False
    else:
        print(f"Abhi price {current_price} hai... wait kar raha hoon.")
        time.sleep(5)

print("\nBhai Mission Successful aur Secure!")
