import random
def WordValidation():
	#done=False
	#while done == False:
	#	word = input("Word: ")
	#	if (len(word) < 10) and (len(word)>2):
	#		done = True
	#		return word.lower()
	#	else:
	#	print("Invalid: Please enter a word that is 3-10 letters long")
	word_file = "words.txt"
	WORDS = open(word_file).read().splitlines()
	word = WORDS[random.randint(0,(len(WORDS))-1)]
	return word.lower()
	
	

			
def LetterValidation(GuessedLetters):
	done=False
	while done == False:
		Letter = input("Letter: ")
		if Letter in GuessedLetters:
			print("You have allready tried this Letter")
		else:
			if (len(Letter) == 1):
				done = True
				GuessedLetters.append(Letter)
				return (Letter.lower(), GuessedLetters)
			else:
				print("Invalid: Please only enter a single letter")
			
			
def SetWord():
	word = WordValidation()
	LetterList = []
	for i in word:
		LetterList.append(i)
	return (LetterList, word)

	
def MakeDisplayWord(LetterList):
		DisplayWord=[]
		for i in LetterList:
			if i == " ":
				DisplayWord.append(" ")
			else:
				DisplayWord.append("_")
		print(DisplayWord)
		return DisplayWord
			

def Setup():
	LetterList, word = SetWord()
	DisplayWord = MakeDisplayWord(LetterList)
	return (LetterList, DisplayWord, word)
	
def Guessing(LetterList,DisplayWord,GuessedLetters,Incorrect):
	Letter,GuessedLetters = LetterValidation(GuessedLetters)
	if Letter in LetterList:
		for i in range(0,(len(DisplayWord))):
			if LetterList[i] == Letter:
				DisplayWord[i]=Letter
	else:
		Incorrect-=1
		print("This letter was not in the word")
		print("You can only get %s incorrect guesses"%Incorrect)
	print(DisplayWord)
	return (LetterList, DisplayWord,GuessedLetters, Incorrect)

LetterList, DisplayWord, word = Setup()
done=False
turns=0
Incorrect=10
GuessedLetters=[]
while done == False:
	
	if DisplayWord == LetterList:
		print("Guesser Wins! It took %s guesses"%turns)
		done=True
	elif Incorrect <= 0:
		print("Hangman!")
		print("Player ran out of guesses")
		print("The word was: '%s'"%word)
		done=True
	else:
		turns+=1
		LetterList, DisplayWord, GuessedLetters, Incorrect = Guessing(LetterList,DisplayWord,GuessedLetters,Incorrect)			
	
