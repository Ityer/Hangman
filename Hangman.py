def WordValidation():
	done=False
	while done == False:
		word = input("Word: ")
		if (len(word) < 10) and (len(word)>2):
			done = True
			return word.lower()
		else:
			print("Invalid: Please enter a word that is 3-10 letters long")

			
def LetterValidation():
	done=False
	while done == False:
		Letter = input("Letter: ")
		if (len(Letter) == 1):
			done = True
			return Letter
		else:
			print("Invalid: Please only enter a single letter")
			
			
def SetWord():
	word = WordValidation()
	LetterList = []
	for i in word:
		LetterList.append(i)
	print(LetterList)
	return LetterList

	
def MakeDisplayWord(LetterList):
		DisplayWord=[]
		for i in LetterList:
			DisplayWord.append("_")
		print(DisplayWord)
		return DisplayWord
			

def Setup():
	GuessedLetters=[]
	LetterList = SetWord()
	DisplayWord = MakeDisplayWord(LetterList)
	return (LetterList, DisplayWord)
	
def Guessing(LetterList,DisplayWord):
	Letter = LetterValidation()
	if Letter in LetterList:
		for i in range(0,(len(DisplayWord)-1)):
			if LetterList[i] == Letter:
				DisplayWord[i]=Letter
	print(DisplayWord)

LetterList, DisplayWord = Setup()
Guessing(LetterList,DisplayWord)			
	
