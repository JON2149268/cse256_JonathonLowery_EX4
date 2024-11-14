# Jonathon Lowery
# CIS256 Fall 2024
# EX 4 - Test



import pytest

from jonathon_lowery_EX4 import words

# check if the guess matches the word
#def test_word():
    #return word == guess

# tests the check_guess function
def test_word():
    assert word("fiction", "fiction") == True
    assert word("fiction", "real") == False

if __name__ == "__main__":
    pytest.main()
    
