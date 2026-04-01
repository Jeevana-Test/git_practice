from helpers import is_palindrome

def test_is_palindrome_true():
    assert is_palindrome("racecar") == True



def test_palindrome_false():
    assert is_palindrome("hello") == False

def test_is_palindrome_space():
    assert is_palindrome("A man a plan a canal Panama") == True