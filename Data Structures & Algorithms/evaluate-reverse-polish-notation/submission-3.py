class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b : b + a,
            "-": lambda a, b : b - a,
            "*": lambda a, b : b * a,
            "/": lambda a, b : int(b / a),
        }

        nums = []

        for char in tokens:
            if char in operations:
                a = nums.pop()
                b = nums.pop()
                nums.append(operations[char](a, b))
            else:
                nums.append(int(char))
        
        return nums[0]

        