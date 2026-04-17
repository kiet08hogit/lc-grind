class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        firstnum = int("".join(str(x) for x in num1))
        second= int("".join(str(x) for x in num2))
        total= firstnum * second
        val= str(total)
        return val