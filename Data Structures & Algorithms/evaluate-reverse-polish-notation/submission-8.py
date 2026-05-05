class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for n in tokens:
            if n == '+':
                nums.append(nums.pop() + nums.pop())
            elif n == '*':
                nums.append(nums.pop() * nums.pop())
            elif n == '-':
                a, b = nums.pop(), nums.pop()
                nums.append(b-a)
            elif n == '/':
                a, b = nums.pop(), nums.pop()
                nums.append(int(float(b)/a))
                print(b, "/", a, ":", b//a)
            else:
                nums.append(int(n))
        return nums[0]


                
