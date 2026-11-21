# def count_vowels(s):
#     count=0
#     s1=s.lower()
#     for ch in s1:
#         if ch in "aeiou":
#             count+=1
#     return count

# print(count_vowels("neha"))
from Collection import Counter

def check_anagram(s1,s2):
    s1= ''.join(ch.lower() for ch in s1 if ch.isalnum())
    s2= ''.join(ch.lower() for ch in s2 if ch.isalnum())
    return Counter(s1) == Counter(s2)
check_anagram("Listen", "Silent")