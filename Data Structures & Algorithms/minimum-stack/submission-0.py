class MinStack:

    def __init__(self):
        self.stack = []
        self.m_array = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(self.m_array[-1] if self.m_array else val, val)
        self.m_array.append(val)
    
        

    def pop(self) -> None:
        self.stack.pop()
        self.m_array.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.m_array[-1]




        
