import time
import random
from google import genai # Naya SDK

# 1. API Configuration
API_KEY = "AIzaSyCcAWH8PUNzmi7M4827Ce37q5rFkONNh8w" 
client = genai.Client(api_key=API_KEY) # 'model' banane ki zaroorat nahi, seedha client banega

def send_notification(price):
    print(f"\n[ALERT]: Price {price} ho gaya!")

def ai_generate_message(price, business_name):
    prompt = f"Professional 1-line message: {business_name} needs 100kg makhana as price is {price}."
    try:
        # 2. Naya tarika message generate karne ka
        response = client.models.generate_content(
            model="gemini-flash-latest", # Model ka naam yahan likhte hain
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI Error: {e}"

# --- Baaki Logic Waisa hi rahega ---
active = True
target_price = 150

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

print("\nBhai Mission Successful!")
