class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        previous = 0
        total = 0
        for i in range(len(s) -1, -1, -1):
            current = roman[s[i]]
            if current < previous:
                total -= current
            else:
                total += current
            previous = current
        return total
