class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = []
        stack = []
        for i in range(len(position)):
            posSpeed.append([position[i], speed[i]])
        
        posSpeed = sorted(posSpeed, key=lambda x: x[0])
        print(posSpeed)
        for i in range(len(posSpeed)-1, -1, -1):
            time_to_target = float((target-posSpeed[i][0]) / posSpeed[i][1])
            print(time_to_target)
            if stack and time_to_target <= stack[-1]:
                continue
            stack.append(time_to_target)
        print(stack)
        return len(stack)
            
            
