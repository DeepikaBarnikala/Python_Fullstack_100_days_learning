# import libraries
from gtts import gTTS
import os
import playsound
import time
import webbrowser
import uuid
import speech_recognition as sr
import random
import segno


# let us create listen function
def listen():
    """Function for Speech Recognition"""
    r = sr.Recognizer()

    # we will take microphone as source
    with sr.Microphone() as source:
        print("Ika Modaledadhamaa..")
        audio = r.listen(source, phrase_time_limit=10)

    # we need to give our text as voice
    data = ""

    # here we will give exceptions
    try:
        data = r.recognize_google(audio)
        print("you said:", data)

    except sr.UnknownValueError as e:
        print("Request Failed")

    except sr.RequestError as e:
        print("Speak clearly request is failing")

    return data


# Respond function
def respond(String):
    """Function to respond back"""

    print(String)

    tts = gTTS(String)

    filename = "Speech%s.mp3" % str(uuid.uuid4())

    tts.save(filename)

    playsound.playsound(filename)

    os.remove(filename)


# Developer QR Code function
def generate_developer_qr():
    """Generate Developer Profile QR Code"""

    profile = """
================================
        DEVELOPER PROFILE
================================

Name:Deepika Barnikala

Role: Python Full Stack Developer

Skills:
Python
SQL
HTML
CSS
Bootstrap
JavaScript
React

Email:
deepikabarnikala0410@gmail.com

LinkedIn:
https://www.linkedin.com/in/deepika-barnikala-ab5a4b301/?trk=opento_sprofile_topcard

GitHub:
https://github.com/DeepikaBarnikala

YouTube:
https://www.youtube.com/

================================
        THANK YOU!
================================
"""

    # Create QR code
    qr = segno.make(profile)

    # Save QR code
    qr.save("developer_profile.png", scale=10)

    print("Developer Profile QR Code Created Successfully!")


# Here we will make our virtual assistant into action
def va(data):
    """Our Virtual Assistant with the actions"""

    data = data.lower()

    listening = True

    if "how are you" in data:

        respond("I'm fine thanks for asking.")

    elif "what are your plans" in data:

        respond("Only Study... One focus in 2026")

    elif "how are things going" in data:

        respond("OK")

    elif "time" in data:

        respond(time.ctime())

    elif "open google" in data:

        respond("Opening Google")

        webbrowser.open("https://www.google.com")

    elif "open youtube" in data:

        respond("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    elif "open whatsapp" in data:

        respond("Opening Whatsapp")

        webbrowser.open("https://web.whatsapp.com")

    elif "open maps" in data:

        respond("Opening Maps")

        webbrowser.open("https://maps.google.com")

    elif "locate" in data:

        location = data.replace("locate", "").strip()

        respond("Locating " + location)

        webbrowser.open(
            "https://www.google.com/maps/search/" + location
        )

        print("Located")

    # ==============================
    # DEVELOPER QR CODE OPTION
    # ==============================

    elif "qr" in data:

        respond("Okay, generating your developer profile QR code.")

        generate_developer_qr()

        respond("Developer profile QR code has been generated successfully.")

        # Open QR image automatically
        os.startfile("developer_profile.png")

    # ==============================
    # NUMBER GUESSING GAME
    # ==============================

    elif "number game" in data:

        respond(
            "Okay, let's play a number guessing game. "
            "I have selected a number between 1 and 20."
        )

        number = random.randint(1, 20)

        for i in range(3):

            respond("Guess the number")

            guess_data = listen()

            try:

                guess = int(guess_data)

                if guess == number:

                    respond(
                        "Congratulations! You guessed the correct number."
                    )

                    break

                elif guess < number:

                    respond(
                        "Your guess is too low. Try again."
                    )

                else:

                    respond(
                        "Your guess is too high. Try again."
                    )

            except ValueError:

                respond("Please say a valid number.")

        else:

            respond(
                "Sorry, you lost the game. "
                "The number was " + str(number)
            )

    # ==============================
    # STOP ASSISTANT
    # ==============================

    elif "stop talking" in data:

        listening = False

        respond("Okay cool.. Kopadakuu bye")

    else:

        print("Command not recognized.")

    return listening


# Start Virtual Assistant
respond(
    "Hey Deepika.. Good to hear from you. How are you?"
)

listening = True

while listening:

    data = listen()

    listening = va(data)
