import os
from dotenv import load_dotenv
import speech_recognition as sr
import openai
from elevenlabs import generate, play, set_api_key

# Load API keys from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
set_api_key(os.getenv("ELEVENLABS_API_KEY"))

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Initial Hindi greeting
initial_prompt = (
    "Namaste! Main PM-KUSUM yojna se bol rahi hoon. "
    "Aap solar pump ke liye 60 pratishat subsidy pa sakte hain. "
    "Kya aap jaankari chahenge?"
)

def speak(text):
    print("Agent:", text)
    audio = generate(text=text, voice="Anika", model="eleven_multilingual_v2")
    play(audio)

def listen():
    with sr.Microphone() as source:
        print("🎤 Boliye...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        print("Farmer:", text)
        return text
    except sr.UnknownValueError:
        return "Mujhe samajh nahi aaya, kripya dobara boliye."
    except sr.RequestError as e:
        return f"Speech service unavailable: {e}"

def chat_with_agent(user_input):
    messages = [
        {"role": "system", "content": "Tum ek helpful krishi salahkaar ho. Hindi mein jawab do."},
        {"role": "user", "content": user_input}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Agent se jawab lene mein samasya hui: {e}"

# --- Main Conversation Loop ---
if __name__ == "__main__":
    speak(initial_prompt)
    while True:
        farmer_input = listen()
        agent_reply = chat_with_agent(farmer_input)
        speak(agent_reply)
