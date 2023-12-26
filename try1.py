
# import speech_recognition as sr
# from googlesearch import search
# import webbrowser

# def listen():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Say something:")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     try:
#         print("You said: " + recognizer.recognize_google(audio))
#         return recognizer.recognize_google(audio)
#     except sr.UnknownValueError:
#         print("Could not understand audio.")
#         return None
#     except sr.RequestError as e:
#         print("Error with the speech recognition service; {0}".format(e))
#         return None

# def search_google(query):
#     try:
#         for j in search(query, num=1, stop=1, pause=2):
#             print("Opening:", j)
#             webbrowser.open(j)
#     except Exception as e:
#         print("Error:", e)

# if __name__ == "__main__":
#     while True:
#         command = listen()
        
#         if command:
#             if "search" in command.lower():
#                 query = command.replace("search", "").strip()
#                 search_google(query)
#             elif "exit" in command.lower():
#                 print("Exiting the virtual assistant.")
#                 break
#             else:
#                 print("Command not recognized. Try saying 'search something' or 'exit'.")


# import pyttsx3
# import speech_recognition as sr
# import webbrowser

# # Initialize the engine
# engine = pyttsx3.init()

# # Define a function that listens for user input and responds accordingly
# def listen():
#     # Initialize the recognizer
#     r = sr.Recognizer()

#     # Use the microphone as source
#     with sr.Microphone() as source:
#         print("Listening...")
#         # Listen for user input
#         audio = r.listen(source)

#     try:
#         # Convert speech to text
#         text = r.recognize_google(audio)
#         print(f"You said: {text}")
#         # Respond based on user input
#         if "open google" in text.lower():
#             engine.say("Opening Google")
#             webbrowser.open("https://www.google.com")
#         elif "search" in text.lower():
#             query = text.lower().replace("search", "").strip()
#             engine.say(f"Searching for {query}")
#             webbrowser.open(f"https://www.google.com/search?q={query}")
#         elif "bye" in text.lower():
#             engine.say("Goodbye!")
#             return False
#         else:
#             engine.say("I'm sorry, I didn't understand what you said.")
#     except sr.UnknownValueError:
#         engine.say("I'm sorry, I didn't understand what you said.")
#     except sr.RequestError as e:
#         engine.say(f"Could not request results from Google Speech Recognition service; {e}")

#     # Run the engine and wait for it to complete speaking
#     engine.runAndWait()
#     return True

# # Call the listen function in a loop until user says goodbye
# while listen():
#     pass


import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia


# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():

	r = sr.Recognizer()

	# from the speech_Recognition module
	# we will use the Microphone module
	# for listening the command
	with sr.Microphone() as source:
		print('Listening')
		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		r.pause_threshold = 0.7
		audio = r.listen(source)
		
		# Now we will be using the try and catch
		# method so that if sound is recognized
		# it is good else we will have exception
		# handling
		try:
			print("Recognizing")
			
			# for Listening the command in indian
			# english we can also use 'hi-In'
			# for hindi recognizing
			Query = r.recognize_google(audio, language='en-in')
			print("the command is printed=", Query)
			
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		
		return Query

def speak(audio):
	
	engine = pyttsx3.init()
	# getter method(gets the current value
	# of engine property)
	voices = engine.getProperty('voices')
	
	# setter method .[0]=male voice and
	# [1]=female voice in set Property.
	engine.setProperty('voice', voices[0].id)
	
	# Method for the speaking of the assistant
	engine.say(audio)
	
	# Blocks while processing all the currently
	# queued commands
	engine.runAndWait()

def tellDay():
	
	# This function is for telling the
	# day of the week
	day = datetime.datetime.today().weekday() + 1
	
	#this line tells us about the number
	# that will help us in telling the day
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
	
	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		print(day_of_the_week)
		speak("The day is " + day_of_the_week)


def tellTime():
	
	# This method will give the time
	time = str(datetime.datetime.now())
	
	# the time will be displayed like
	# this "2020-06-05 17:50:14.582630"
	#nd then after slicing we can get time
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak("The time is sir" + hour + "Hours and" + min + "Minutes")

def Hello():
	
	# This function is for when the assistant
	# is called it will say hello and then
	# take query
	speak("hello sir I am your desktop assistant. /Tell me how may I help you")


def Take_query():

	# calling the Hello function for
	# making it more interactive
	Hello()
	
	# This loop is infinite as it will take
	# our queries continuously until and unless
	# we do not say bye to exit or terminate
	# the program
	while(True):
		
		# taking the query and making it into
		# lower case so that most of the times
		# query matches and we get the perfect
		# output
		query = takeCommand().lower()
		if "open geeksforgeeks" in query:
			speak("Opening GeeksforGeeks ")
			
			# in the open method we just to give the link
			# of the website and it automatically open
			# it in your default browser
			webbrowser.open("www.geeksforgeeks.com")
			continue
		
		elif "open google" in query:
			speak("Opening Google ")
			webbrowser.open("www.google.com")
			continue
			
		elif "which day it is" in query:
			tellDay()
			continue
		
		elif "tell me the time" in query:
			tellTime()
			continue
		
		# this will exit and terminate the program
		elif "bye" in query:
			speak("Bye. Check Out GFG for more exciting things")
			exit()
		
		elif "from wikipedia" in query:
			
			# if any one wants to have a information
			# from wikipedia
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			
			# it will give the summary of 4 lines from
			# wikipedia we can increase and decrease
			# it also.
			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			speak(result)
		
		elif "tell me your name" in query:
			speak("I am Jarvis. Your desktop Assistant")

if __name__ == '__main__':
	
	# main method for executing
	# the functions
	Take_query()
