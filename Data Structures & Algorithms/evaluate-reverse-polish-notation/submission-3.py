class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        nums = []

        for c in tokens:
            if c == '+':
                nums.append(nums.pop() + nums.pop())
            elif c == '*':
                a, b = nums.pop(), nums.pop()
                nums.append(a*b)
            elif c == '-':
                a, b = nums.pop(), nums.pop()
                nums.append(b-a)
            elif c == '/':
                a, b = nums.pop(), nums.pop()
                nums.append(int(b/a))
            else:
                nums.append(int(c))
        return nums[0]

