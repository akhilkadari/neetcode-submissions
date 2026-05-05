class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_to_speed = []
        stack = []
        for i in range(len(position)):
            position_to_speed.append([position[i], speed[i]])

        position_to_speed.sort()
        for i in range(len(position_to_speed)-1, -1, -1):
            time_to_target = float(target-position_to_speed[i][0])/position_to_speed[i][1]
            if stack and time_to_target <= stack[-1]:
                continue
            stack.append(time_to_target)
        
        return len(stack)


            
            
