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
			return Letter.lower()
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
	print(0)
	if Letter in LetterList:
		print(1)
		for i in range(0,(len(DisplayWord))):
			print(2)
			print("i=%s"%i)
			if LetterList[i] == Letter:
				print(3)
				DisplayWord[i]=Letter
	print(DisplayWord)
	return (LetterList, DisplayWord)

LetterList, DisplayWord = Setup()
done=False
turns=0
while done == False:
	
	if DisplayWord == LetterList:
		print("Guesser Wins! It took %s guesses"%turns)
		done=True
	else:
		turns+=1
		LetterList, DisplayWord = Guessing(LetterList,DisplayWord)			
	
