import core

class CalculatorTool(core.tool.Tool):
    async def calculate(self, expression: str):
        """Evaluates a math expression safely."""
        # allow only math characters
        allowed = set('0123456789+-*/(). ')
        if not all(c in allowed for c in expression):
            raise ValueError("Invalid characters in expression")

        try:
            return eval(expression, {'__builtins__': {}}, {})
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")
