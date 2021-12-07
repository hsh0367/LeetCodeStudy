class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if digits == "":
            return []
        number = list(key_map[digits[0]])
        print(number)
        result = []
        for i in digits[1:]:
            number = [prev + new for prev in number for new in key_map[i]]
        return number
