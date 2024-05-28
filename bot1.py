import speech_recognition as sr
from gtts import gTTS # type: ignore
import os

# Initialize the recognizer 
r = sr.Recognizer() 
mytext='dont care'

# Function to convert text to speech
def record_text():
    while True: 
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2) # type: ignore
                print("say something")
                audio2 = r.listen(source2)
                text1 = r.recognize_google(audio2) # type: ignore
                return text1
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Unknown error occurred")
            
def output_text(text1):
    f = open("output.txt", "a")
    f.write(text1)
    f.write("\n")
    f.close()
    
while True:

    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    text1 = record_text()
    #output_text(text1)
    print("Wrote text:", text1)
    
    user_input=text1
    print("Welcome to the Simple Chatbox!")


    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive comparisons
    
    if user_input == "hello":
        mytext='Hi there!' 
        print("mytext: Hi there!")
        continue
    elif user_input == "how r u":
        mytext='I am just a computer program, but thanks for asking!' 
        print("mytext: I'm just a computer program, but thanks for asking!")
        continue
    elif user_input == "bye":
        mytext='Goodbye!' 
        print("mytext: Goodbye!")
        break
    else:
        print("mytext: Sorry, I don't understand that.")
        mytext='Sorry, I dont understand that.'
        

    
    
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")