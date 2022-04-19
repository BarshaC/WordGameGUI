from wordgameProject import *

def test_make_hand():
    """
    Unit test for the function make_hand which functions for making hand from letters
    """
    hand = make_hand(HAND_SIZE)
    if not type(hand) is dict:
        print("TEST FAILED for test_make_hand()")
        return

def test_get_word_score():
    """
    Unit test for get_word_score() function
    """
    expected = get_word_score('hi',10)
    assert expected == 5
    expected = get_word_score('everything',10)
    assert expected == 120

def test_display_hand_letters():
    """
    Unit test for display_hand_letters()
    """
    expected = " w w o p p p i i x x"
    assert display_hand_letters({'w':2, 'o': 1, 'p':3,'i': 2, 'x':2}) == expected
    assert display_hand_letters({'w': 0, 'o': 1, 'p':3,'i': 2, 'x':2}) != expected

def test_check_validity_word():
    """
    Unit test for check_validity_word()
    """
    """
    Unit test for is_valid_word
    """
    failure=False
    word = "hello"
    hand = get_word_frequency(word)

    if not check_validity_word(word, hand, wordlist):
        print ("FAILURE: test_is_valid_word()")
        failure = True

    hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
    word = "rapture"

    if  check_validity_word(word, hand, wordlist):
        print ("FAILURE: test_is_valid_word()")
        failure = True        

    hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
    word = "honey"

    if  not check_validity_word(word, hand, wordlist):
        print ("FAILURE: test_is_valid_word()")
        failure = True                        

    hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
    word = "honey"

    if  check_validity_word(word, hand, wordlist):
        print ("FAILURE: test_is_valid_word()")
        failure = True    

def test_update_hand():
    """
    Unit test for update_hand()
    """
    hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    word = "quail"

    hand2 = update_hand(hand.copy(), word)
    expected_hand1 = {'l':1, 'm':1}
    expected_hand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print ("TEST FAILED: test_update_hand('"+ word +"', " + str(hand) + ")")
        print ("Returned: ", hand2, "-- but expected:", expected_hand1, "or", expected_hand2)
        return
    
    hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    word = "evil"

    hand2 = update_hand(hand.copy(), word)
    expected_hand1 = {'v':1, 'n':1, 'l':1}
    expected_hand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expected_hand1 and hand2 != expected_hand2:
        print ("TEST FAILED: test_update_hand('"+ word +"', " + str(hand) + ")")        
        print ("Returned: ", hand2, "-- but expected:", expected_hand1, "or", expected_hand2)
        return     
    
if __name__ == "__main__":
    wordlist = load_words()
    test_make_hand()
    test_get_word_score()
    test_display_hand_letters()
    test_check_validity_word()
    test_update_hand()
    
    
