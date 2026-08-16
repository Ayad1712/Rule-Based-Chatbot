!pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import random

#Goodbye Messages
goodbye_url = "https://faruk-hasan.com/ai_resources/goodbyes.html"
goodbye_request = requests.get(goodbye_url)
parsed_goodbye = BeautifulSoup(goodbye_request.text,'html.parser') #parse
goodbye_raw = parsed_goodbye.find_all("p",class_="container") #find the raw html of the actual messages

goodbye_list = []
for i in goodbye_raw:
  goodbye_list.extend(i.text.split("\n")) #.extend() takes each individual message and adds them each as an element to the goodbye_list
  #text and split removes whitespace and takes the text without the html.


#Thank You Messages
thanks_url = "https://faruk-hasan.com/ai_resources/thanks.html"
thanks_request = requests.get(thanks_url)
parsed_thanks = BeautifulSoup(thanks_request.text,'html.parser') #same here
thanks_raw = parsed_thanks.find_all("p",class_="container")

thanks_list = []
for a in thanks_raw:
  thanks_list.extend(a.text.split("\n"))


#Greetings
url = "https://faruk-hasan.com/ai_resources/greetings.html" #part 1: make a list with all the greetings.
greetings_request = requests.get(url)
parsed_greetings = BeautifulSoup(greetings_request.text,'html.parser')
greetings_raw = parsed_greetings.find_all("div",class_="container")

greetings = []
for i in greetings_raw:
  greetings.extend(i.text.split("\n"))

clean_greetings = []

for i in greetings:
  if "Welcome" in i or "More" in i:
    pass
  else:
    if i.strip():
      clean_greetings.append(i)

#greetings is our key, and clean_greetings is the value
#when the chatbot recognizes the users input as one of the patterns in the clean_greetings list, it will respond with two unique sentences
intents ={"greetings":{"patterns":clean_greetings,"responses":["Hi there!", "Hey there! How can I help you today?"]},
          "goodbyes":{"patterns":goodbye_list,"responses":["Goodbye!", "See you soon!", "Until we meet again!"]},
          "thanks":{"patterns":thanks_list,"responses":["You're welcome!", "Any time!", "No problem, happy to help!"]}}

#print(greetings_intents.items()) #this will print a special object mainly used in for loops to go through both items (keys and values)
#for key, value in intents.items():
  #print(key,"-->",value)

copy1 = [] #now we create a second list with the same items as clean_greetings, but without the exclamation mark
for i in clean_greetings:
  if i.endswith("!"):
    j = i.replace("!","")
    copy1.append(j)
clean_greetings = clean_greetings + copy1 #add the list to clean_greetings

#for intent, data in intents.items(): #key is the intent, value is the data
  #print("Intent:", intent) #the type of input the robot will detect
  #print("Patterns:",data["patterns"]) #pattern that the chatbot will recognize
  #print("Responses",data["responses"]) #what the robot will respond back with

def normalize(pattern):
  pattern = pattern.lower().strip()
  pattern = pattern.replace("!","").replace(",","").replace("?","").replace(".","")
  return pattern
def response(user_input):
  user_input = normalize(user_input) #variable is user_input, parameter is normalize
  for intent, data in intents.items(): #to look at type of intent
    for pattern in data["patterns"]: #to look at the patterns
      if normalize(pattern) in user_input:  #if it matches with user_input
        return random.choice(data["responses"]) #uses random.choice to randomly choose a response depending on the intent
      return "I'm not sure how to respond to that." 

#begin frontend
while True:
  user_input = input("User: ")
  if user_input.lower() in ["quit","exit"]:
    break
  print("Chatbot:",response(user_input))
