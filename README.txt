Elite Speak

Don't you hate it when you don't understand what someone is saying? Now, with Elite Speak, just press record and all those complicated words will be defined as they speak!

Dependencies: Speech Recognizer (Google Speech Recognition)
	pip install SpeechRecognition
	
Can be run from the command line by typing:
	python3 main_script.py

Initially started at Codestellation 2017, Brandeis University's annual hackathon.

Alex T. Reese
Ben Albert 
Ellis Miranda
Lizzie Koshelev
Jamie Brandon


There's an external error from speech recognition that users should ignore. 

C:\Users\jamie\Anaconda3\lib\site-packages\bs4\__init__.py:181: UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 882 of the file C:\Users\jamie\Anaconda3\lib\threading.py. To get rid of this warning, change code that looks like this:

 BeautifulSoup([your markup])

to this:

 BeautifulSoup([your markup], "lxml")

  markup_type=markup_type))

We tried to get rid of this, but we're not exactly sure where it's coming from. The location it gives doesn't have those lines of code. Weird.
