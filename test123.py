def read_text():
	quotes = open("test_file.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
