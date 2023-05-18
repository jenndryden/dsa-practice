class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for letter in s:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
        for letter in t: 
            if letter not in letters:
                return False
            if letters[letter] == 0:
                return False
            else:
                letters[letter] -= 1
        if len(s) != len(t): 
            return False
        return True