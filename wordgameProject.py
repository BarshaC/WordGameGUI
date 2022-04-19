import random
import string
import PySimpleGUI as sg
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
HAND_SIZE = 10

LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words in lower case.
    """
    file = open(FILENAME,"r")
    wordlist = []
    for line in file:
        wordlist.append(line.strip().lower())
    return wordlist


def get_word_frequency(sequence):
    """
    Returns a dictionary mapped from the letters of the sequence and the number
    times letters are repeated
    sequence - list
    returns - dictionary object
    """
    freq = dict()
    for i in sequence:
        freq[i] = freq.get(i,0) + 1
    return freq


def get_word_score(word,n):
    """
    word - string(lowercase)
    returns - int (length of word)
    """
    score = 0
    for letter in word:
        score += LETTER_VALUES[letter.lower()]
    if len(word) == n:
        score += 100
    return score

def display_hand_letters(hand):
    """
    The main work of this function is to display hand to the user.
    hand: dictionary (string mapped to number of time string is repeated)
    if dictionary is {'w':2, 'o': 1, 'p':3,'i': 2, 'x':2}, hand will be as follows:
     w w o p p p i i x x

    hand: dictionary mapping from string to score
    return string/ set of letters as shown above
    """
    string = ""
    for letter in hand.keys():
        for j in range(hand[letter]):
            string = string + " " + letter
    return string

def make_hand(n):
    """
    This function is to generate random set of letters with the combination of
    vowels and consonants.
    n - int (totally depends on HAND_SIZE)
    return: dictionary (string --> int)
    """
    hand = dict()
    vowels = int(n/3)
    for i in range(vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for j in range(vowels,n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x,0) + 1
    return hand

def update_hand(hand,word):
    """
    hand - dictionary (string --> int)
    word - string
    returns dictionary (string --> int)
    """
    freq = get_word_frequency(word)
    new_hand = dict()
    for char in hand:
        new_hand[char] = hand[char] - freq.get(char,0)
    return new_hand

    
def check_validity_word(word, hand, wordlist):
    """
    word: string
    hand: dictionary
    wordlist: list of lowercase valid words
    """
    freq = get_word_frequency(word)
    for letter in word:
        if freq[letter] > hand.get(letter,0):
            return False
    return word in wordlist

       
def play_hand(hand, wordlist):
    """
    Takes: hand: dictionary mapping from letter to number of occurences of letter
           wordlist: list of lowercase english valid words
    Allows the user to play the given hand, prints the instructions and help the user to play
    """
    num_hand = len(hand)
    total = 0
    while num_hand >0:
        sg.theme('DarkPurple4')
        letters = display_hand_letters(hand)
        message1 = " CURRENT HAND "
        display_letters = str(letters)
        layout3 = [[sg.Text(message1)],
                   [sg.Text(display_letters)],
                   [sg.Text("MAKE WORD OUT OF ABOVE LETTERS OR ENTER '.' TO QUIT"),sg.InputText()],
                       [sg.OK()]]
        window3 = sg.Window("Displaying Hand", layout3)
        event3,value3 = window3.read()
        #print("Current hand... :", display_hand_letters(hand))
        #user_input = str(input("Enter your word, or a '.' to indicate you are finished "))
        if value3[0] == ".":
            break
        else:
            if check_validity_word(value3[0], hand, wordlist):
                current_score = get_word_score(value3[0], num_hand)
                total += current_score
                message2 = "BINGO YOU SCORED"
                display_score = str(current_score)
                layout4 = [[sg.Text(message2)],
                           [sg.Text(display_score)],
                           [sg.Text("GOING GOOD")],
                           [sg.OK()]]
                window4 = sg.Window("SCORE!", layout4)
                event,value = window4.read()
                if event == sg.WIN_CLOSED or event == 'OK':
                    window4.close()
                hand = update_hand(hand, value3[0])
            else:
                message3  = "LOOKS LIKE YOUR WORD IS NOT VALID. TRY AGAIN "
                layout5 = [[sg.Text(message3)],
                           [sg.OK()]]
                window5 = sg.Window("INVALID WORD :(", layout5)
                event2,value2 = window5.read()
                if event2 == sg.WIN_CLOSED or event2 == "OK":
                    window5.close()
    message4 = "GOOD JOB! YOUR TOTAL SCORE IS: %d" %total
    message5 = "PRESS ENTER FOR ANOTHER ROUND!"
    layout6 = [[sg.Text(message4)],
               [sg.Text(message5)],
                [sg.OK()]]
    window6 = sg.Window("TOTAL SCORE", layout6)
    eventx, valuex = window6.read()
    if eventx == "OK" or eventx == sg.WIN_CLOSED:
        window6.close()
    if total >= 20:
        message5 = "WOW THAT'S IMPRESSIVE. PRESS ENTER TO PLAY ANOTHER ROUND"
        layout7 = [[sg.Text(message5)],
                   [sg.OK()]]
        win = sg.Window("", layout7)
        event,value = win.read()
        if event == sg.WIN_CLOSED or event == "OK":
            win.close()
"""  
while True:
    event,values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED or event in (sg.WIN_CLOSED,'Cancel'):
        break
window.close()
"""
def play_game(wordlist):
    """
    Allows user to play arbitrary number of hands
    Asks user to input "n" for new hand, "r" for replay of hand and "." to end game
    """
    sg.theme('DarkGreen')
    layout1 = [[sg.Text("WELCOME TO SCRABBLE GAMES!")],
                  [sg.Text("LET'S GET STARTED")],
                  [sg.OK(), sg.Cancel()]]
    window1 = sg.Window("",layout1)
    event, values = window1.read()
    layoutr = [[sg.Text("HERE ARE THE RULES FOR THIS WORD GAME: ")],
               [sg.Text(" PRESS Cancel IF YOU WANT TO START PLAYING ")],
               [sg.Text("1.You can chose a new hand by pressing 'n' then you get set of letters and you make word out of the set of letters given to you ")],
               [sg.Text("2.As you make the word. Your hand will be updated. You can make another word from the remaining set of letters.")],
               [sg.Text("3.If you can make word out of all the letters you get 100 extra score.")],
               [sg.Cancel()]]
    windowr = sg.Window("", layoutr)
    eventr, valuer = windowr.read()
    if eventr == sg.WIN_CLOSED or eventr == "Cancel":
        windowr.close()
    hand = make_hand(HAND_SIZE)
    found = False
    while not found:
        if event == sg.WIN_CLOSED or event == "Cancel":
            found = True
            window1.close()
            break
        elif event == "OK":
            sg.theme('DarkAmber')
            layout2 = [[sg.Text("   ENTER  'n'  FOR  NEW  SET  OF  LETTERS  ")],
                       [sg.Text("   Enter  'r'  TO  REPLAY  THE  LAST  HAND ")],
                [sg.Text("  SIMPLY  ENTER  '.' / FULL STOP TO  END  THE  GAME :   "), sg.InputText()],
                       [sg.Text("")],
                       [sg.OK()]]
            window2 = sg.Window("", layout2)
            event,values = window2.read()
            window2.close()
            if values[0] == "n":
                hand = make_hand(HAND_SIZE)
                play_hand(hand.copy(), wordlist)
            elif values[0] == "r":
                play_hand(hand.copy(), wordlist)
            elif values[0] == ".":
                break
            else:
                sg.theme('DarkTeal')
                layout3 = [[sg.Text("INVALID")],
                           [sg.Text("ENTER 'n' FOR NEW DEAL OF HAND, 'r' TO REPLAY THE LAST HAND or '.' TO END THE GAME :")],
                           [sg.OK()]]
                continue

if __name__ == '__main__':
    wordlist = load_words()
    play_game(wordlist)
    
    
    
