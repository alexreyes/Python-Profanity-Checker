import urllib

def read_text():
	quotes = open("test_file.txt")
	contents_of_file = quotes.read()
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
	output = connection.read()
	
	if "true" in output:
		print("There is profanity in your file.")
	elif "false" in output:
		print("There is not profanity in your file.")
	else: 
		print("I couldn't read the file properly.")
	connection.close()

read_text()