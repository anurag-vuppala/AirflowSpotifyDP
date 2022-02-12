import pytest

# @pytest.mark.parametrize("test_input, expected",
#                          [("hello world", "world hello"),
#                           ("the cat sat on the mat", "mat the on sat cat the")])
# def test_reverse_word_order(test_input: str, expected: str):
#     result = reverse_word_order(test_input)
#     assert result == expected

# def reverse_word_order(sentence: str) -> str:
#     se = sentence.split()
#     temp = []
#     for word in range(len(se)):
#         temp.append(se[-word-1])   
#         print(temp)
        
        
    
#     return " ".join(temp)

@pytest.mark.parametrize("s1,s2,expected",
                         [("not an anagram", "hello world", False),
                          ("debit card", "bad credit", True),
                          ("dormitory", "dirty room", True)])
def test_is_anagram(s1: str, s2: str, expected: str):
    result = is_anagram(s1, s2)
    assert result == expected


def is_anagram(s1: str, s2: str) -> bool:
    s2 = s2.replace(" ","")
    s1 = s1.replace(" ","")
    for c in range(len(s2)):
        print(s2[c]) 
        if s2[c] in s1:
            s1 = s1.replace(s2[c],"")
    print(s1)        
    if s1 == "":
        return True
    else:
        return False
       