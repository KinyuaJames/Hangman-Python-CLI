import random
import string
from PyDictionary import PyDictionary


with open ('./word2.txt') as f:
    datta = f.read()
    z = datta.split(", ")
    words=[]#initialize the variable words that will store all the words file from the txt file in this array
    for i in z:
        if " " in i:
            l =  i.replace(' ','')#remove any preceding space from the word after the split
            # print (i)
            words.append(l)
        elif "," in i:
            m = i.split(",")#split any word in the array joined with a comma
            for o in m:
                words.append(o)
        else:
            words.append(i)
f.close()
# above gets a cleaner words array
    
    
# >>>>>>>>>>>>>>>>>>method to get valid words from a dictionary<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def get_valid_word(words):
                
    word =  random.choice(words)
    # >>>>>>>>>>>>>>>>>>>>>>>remove spaces and dashes from words <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    while '-' in word or " " in word:
        word = random.choice(words)
    return word
# print(get_valid_word(words))


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>method to get the meaning of the passed word<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def getMeaning(wordie):
    dict = PyDictionary(wordie).getMeanings()#>>>>>>>>>>>>>>>>>>get the meaning from pydic, need internet connection<<<<<<<<<<<<<<<<<<
   
    # check if there are the following in the pydict and take the first two if any
    if 'Noun'or'Adjective'or'Verb' or 'Adverb' in dict[wordie]:
        if 'Noun' in dict[wordie]:
            print("As a Noun: -", dict[wordie]['Noun'][:2])
        if 'Verb' in dict[wordie]:
            print("As a verb: -",dict[wordie]['Verb'][:2])
        if 'Adjective' in dict[wordie]:
            print("As a adjective: -",dict[wordie]['Adjective'][:2])
        if 'Adverb' in dict[wordie]:
            print("As a Adverb: -",dict[wordie]['Adverb'][:2])
    

# >>>>>>>>>>>>>>>>method to start the game<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def hangman():
    word = get_valid_word(words).upper()#>>>>>get a word from the word.py document
    word_letters = set(word)#>>>>>put the word in a set<<<<<<<<<<
    alphabet = set(string.ascii_uppercase)#>>>>>>put all letters of the alphabet in a set<<<<<<<<<<<<
    used_letters = set()#>>>>>>>>>>define a set to append used letters<<<<<<<<<<<<<<<<<<<
    
    
    life = round(len(word)*1.5)#>>>>>>>>>>>>variable for storing players life/lives available
    
    # defining conditions for playing the game
    while len(word_letters) > 0 and life>0:
        displayLetters = [ letter if letter in used_letters else " ? " for letter in word]#>>>>>>display a ? in place of a letter in the word not used/played by player
        print(f"\n Current word is {len(word)} Characters : \n"," ".join(displayLetters), "\n Lives available ", life)
        
        # >>>>>>>>>>>the commented line below follows the same logic as its line below<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # if (life <= len(word)) and (len(word_letters) == (life or life+1 )) :
        if ( life-1 <= displayLetters.count(" ? ")):#check if player lives is below or equal to unused letters in word
            print("to get meaning  type 'MNG' ")
        
        user_letter = input("\n guess a letter: ").upper()#recieve the players letter input 
        # print(life)
        
        
        # >>>>>>>>>>>>>>>Logic to check/add/remove player letter input and check if game won<<<<<<<<<<<<<<<<<<<<<<<<<<<
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            life -= 1
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('\n','good guess ',user_letter,' Niiiiice ')
            else:
                print(user_letter, ' not in word')
        elif user_letter in used_letters:
            life -= 1
            print("Letter already provided. Try another letter...Careful, dont waste lives")
            print("Letters used: \n {", "  ".join(used_letters),"}")
            
        else:#check if the user wants the meaning of the word
            if user_letter == 'MNG':
                if ( life-1 <= displayLetters.count(" ? ")) :
                    getMeaning(word)
                else:
                    print('nice try')
            else:
                print("Invalid/Not a letter ")
            # return
    # this conditions are outside the loop and are called if the game is won or lost
    if life==0 and (len(word_letters)>0):
        print('\n \n \n Haangman, broke thy neck😵🤪🤕, word was',word, '\n \n \n')
    else:
        print("\n \n \n Escaped the gallows🎶🎉 word was", word, '\n \n \n \n')
hangman()
