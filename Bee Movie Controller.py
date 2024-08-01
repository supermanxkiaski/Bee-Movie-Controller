import speech_recognition as sr
import pydirectinput
import time

# Initialize recognizer
recognizer = sr.Recognizer()
recognizer.energy_threshold = 600  # Adjust this value as neededwasdwasdwasd
recognizer.dynamic_energy_threshold = True

def transcribe_and_press_key():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

        try:
            # Transcribe speech to text
            text = recognizer.recognize_google(audio)
            print(f"{text}")

            # Split the transcribed text into words
            words = text.lower().split()

            # Process each word
            for word in words:
                if word == "according":
                    pydirectinput.keyDown('w')
                    time.sleep(0.3)  # Simulate a short keypress (adjust as needed)sd
                    pydirectinput.keyUp('w')
                elif word == "to":
                    pydirectinput.keyDown('a')
                    time.sleep(0.2)  # Simulate a short keypress (adjust as needed)
                    pydirectinput.keyUp('a')
                elif word == "two":
                    pydirectinput.keyDown('a')
                    time.sleep(0.2)  # Simulate a short keypress (adjust as needed)wa
                    pydirectinput.keyUp('a')
                elif word == "all":
                    pydirectinput.keyDown('s')
                    time.sleep(0.2)  # Simulate a short keypress (adjust as needed)
                    pydirectinput.keyUp('s')
                elif word == "known":
                    pydirectinput.keyDown('d')
                    time.sleep(0.2)  # Simulate a short keypress (adjust as needed)
                    pydirectinput.keyUp('d')
                elif word == "laws": 
                    pydirectinput.moveRel(0, -10, relative=True) 
                elif word == "of":
                    pydirectinput.moveRel(-10, 0, relative=True)
                elif word == "aviation": 
                    pydirectinput.moveRel(0, 10, relative=True) 
                elif word == "there":
                    pydirectinput.moveRel(10, 0, relative=True)
                elif word == "is":
                    pydirectinput.mouseDown(button='left') 
                    time.sleep(4)  
                    pydirectinput.mouseUp(button='left')
                elif word == "no":
                    pydirectinput.mouseDown(button='right') 
                    time.sleep(0.1)  
                    pydirectinput.mouseUp(button='right')
                elif word == "way":
                    pydirectinput.keyDown('e')
                    time.sleep(0.1)  # Simulate a short keypress (adjust as needed)
                    pydirectinput.keyUp('e')
                elif word == "wei":
                    pydirectinput.keyDown('e')
                    time.sleep(0.1)  # Simulate a short keypress (adjust as needed)
                    pydirectinput.keyUp('e')
                elif word == "that":
                    pydirectinput.keyDown('1')
                    time.sleep(0.1)  # Simulate a short keypress (adjust as needed)
                    pydirectinput.keyUp('1')
                elif word == "a":
                    pydirectinput.keyDown('2')
                    time.sleep(0.1)  # Simulate a sa12hort keypress (adjust as needed)
                    pydirectinput.keyUp('2')
                elif word == "bee":
                    pydirectinput.keyDown('3')
                    time.sleep(0.1)  # Simulate a sa12hort keypress (adjust as needed)
                    pydirectinput.keyUp('3')
                elif word == "should":
                    pydirectinput.keyDown('4')
                    time.sleep(0.1)  # Simulate a sa12hort keypress (adjust as needed)
                    pydirectinput.keyUp('4')
                elif word == "be":
                    pydirectinput.keyDown('5')
                    time.sleep(0.1)  # Simulate a sa12hort keypress (adjust as needed)
                    pydirectinput.keyUp('5')
                elif word == "able":
                    pydirectinput.keyDown('6')
                    time.sleep(0.1)  # Simulate a sa12hort keypress (adjust as needed)
                    pydirectinput.keyUp('6')
                elif word == "fly":
                    pydirectinput.keyDown('7')
                    time.sleep(0.1)  # Simulate a sa12hort keypress (adjust as needed)
                    pydirectinput.keyUp('7')
                else:
                    print(f"No recognized command for word: {word}")

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    while True:
        transcribe_and_press_key()
