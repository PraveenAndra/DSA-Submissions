class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = [0,0]
        curr = start
        lookup = {"U":[0,1],"D":[0,-1],"L":[-1,0],"R":[1,0]}
        for move in moves:
            x,y = lookup[move]
            curr = [curr[0]+x,curr[1]+y]
        return curr==start
        