class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        temp = {
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
        number = list(temp[digits[0]])
        print(number)
        result = []
        for i in digits[1:]:
            # number = [prev + new for prev in number for new in temp[i]]
            for new in temp[i]:
                for prev in number:
                    print(prev + new)
                number = new
        return number
