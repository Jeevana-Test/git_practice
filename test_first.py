"""using assertion"""
def test_char_count():
    word="hello world"
    freq={}
    for ch in word:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    print(freq)
    assert freq["l"]==3
