class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dp = []
        curr = [0,0]
        dp.append(curr)
        dir = [(0,1),(1,0),(0,-1),(-1,0)]
        curr_dir = 0
        for i in instructions:
            if i == "G":
                curr = [curr[0]+dir[curr_dir][0],curr[1]+dir[curr_dir][1]]
            elif i=="L":
                if curr_dir == 0:
                    curr_dir = 3
                else:
                    curr_dir -= 1

            else:
                if curr_dir == 3:
                    curr_dir = 0
                else:
                    curr_dir += 1
        return curr == [0,0] or curr_dir != 0

        