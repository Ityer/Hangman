def WordValidation():
	done=False
	while done == False:
		word = input("Word: ")
		if (len(word) < 10) and (len(word)>2):
			done = True
			return word
		else:
			print("Invalid: Please enter a word that is 3-10 letters long")

def SetWord():
	word = WordValidation()
	LetterList = []
	for i in word:
		LetterList.append(i)
	print(LetterList)
