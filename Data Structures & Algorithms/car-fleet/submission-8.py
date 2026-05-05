class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_to_speed = []
        stack = []

        for i in range(len(position)):
            pos_to_speed.append([position[i], speed[i]])
        
        pos_to_speed.sort()

        for i in range(len(pos_to_speed)-1, -1, -1):
            time_to_target = float(target-pos_to_speed[i][0])/pos_to_speed[i][1]

            if stack and time_to_target <= stack[-1]:
                continue

            stack.append(time_to_target)

        return len(stack)