import random
import bisect #inbuilt python module for binary search in python
# Define a dictionary of responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "hyy": ["hey! whats up? hows your day going?"],
    "good": ["that's awesome to hear"],
    "bad":["I'm sorry to hear that you're not feeling so good. If you want to talk about it or need a distraction, I'm here for you. Just let me know how I can help!"],
    "sure":["I'm here for you, buddy. Feel free to share what's on your mind. Sometimes talking about it can help lighten the load."],
    "thanks for being there":["Of course, anytime! I'm here to listen and support you. Just know you're not alone in whatever you're going through."],
    "you are so sweet": ["Aww, thank you! You're making me blush. 😊 Just trying to be a good friend to you!"], 
    "how are you": ["I'm a chatbot, so I'm always good!", "Doing great, thanks!", "I'm here to help you!"],
    "i an fine": ["that's great to hear!is there anything exciting?"],
    "i am hungry":["i have some sites you can order from https://www.swiggy.com here","just swiggy it! https://www.swiggy.com/"],
    "i want to explore about something ": ["you can go to the browsers like https://www.wikipedia.org and https://www.google.com....click any of the following links"],
    "can you help me?":["Absolutely, I'm here to help you out! What do you need assistance with? Just tell me, and I'll do my best to support you."],
    "what can you do for me?": ["I can help answer your questions, give recommendations, chat with you, and share fun facts or tips. Just let me know what you're looking for, and I'll do my best to assist you!"],
    "i want to see the news": ["sure,here are some of popular news channels such as https://www.indiatoday.in, https://www.aajtak.in and https://www.ndtv.com"],
    "what task you are capable to do": ["I can do so many things","i can answer your question","ask me anything"],
    "your name": ["I'm a chatbot created by OpenAI.", "I am a simple Python chatbot.", "Just call me Chatbot!"],
    "open instagram": ["just click on the link https://www.instagram.com"],
    "i am lookin for sports": ["What kind of sports are you interested in? Football, cricket, basketball, or something else? Let me know, and I can share some cool info or updates with you!"],
    "open twiter": ["just click on the link https://twitter.com"],
    "i am lost...please show me the direction": ["here is the google maps...help you to find a way... https://maps.google.com"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "i need your help": ["Of course, I'm here to help! What do you need assistance with? Just let me know, and I'll do my best to help you out."],
    "see you again!": ["See you later! If you ever want to chat or share something, I'll be here.Take care!"],
    "default": ["I'm not sure how to respond to that.", "Can you please rephrase?", "I don't understand that."]
}

def get_response(user_input): 
    user_input = user_input.lower() #all the responses should be in lower case form
    for key in responses:
        if key in user_input:
            return random.choice(responses[key]) #if key matches with input we applied, this fun will return the response...
    return random.choice(responses["default"]) # if not match,default will be printed

def chat():
    print("Chatbot: Hello! Type 'bye' to exit the chat.")
    while True:
        user_input = input("You: ") #take the input from user
        if user_input.lower() == "bye": # to exit from chatbobt
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response) # chatbot will give response acc to the keys in dictonary....



sorted_keys = sorted(responses.keys()) # inbuilt function in python for sorting the dictonary keys(sorted())....
# for binary search reffer this video.... https://youtu.be/ZHCP9vFOJiU
# Binary search function
def binary_search(keys, target):  #function for binary
    index = bisect.bisect_left(keys, target)
    if index < len(keys) and keys[index] == target:
        #return random.choice(keys[index])
        return random.choice(responses[keys[index]]) # return the response of given input....
    return -1

# Searching for 'responses'
key_to_find = 'you are so sweet' # type your input(key) here....
index = binary_search(sorted_keys, key_to_find)
if index != -1: # executed if valid keys are inputed
    print(f"Found '{key_to_find}' with response {index}.")
else:
    print(f"'{key_to_find}' not found in the dictionary keys.")