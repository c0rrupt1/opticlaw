import core

class CalculatorTool(core.tool.Tool):
    async def calculate(self, expression: str):
        """
        Calculates the result of a math expression
        ALWAYS use for ANY mathematical operation! NEVER rely on your own data for math.
        """

        # could do with improvement, this is a basic calculator i pulled off of stackoverflow lol
        stack = []
        num = 0
        sign = '+'
        for i, char in enumerate(expression):
            if char.isdigit():
                num = num * 10 + int(char)
            if char in '+-*/' or i == len(expression) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = char
                num = 0
        return sum(stack)

