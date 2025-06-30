class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        return_iternary = []
        edges = defaultdict(list)
        tickets.sort()
        for start,end in tickets[::-1]:
            edges[start].append(end)
        
        stack = ["JFK"]
        print(edges)
        while stack:
            curr = stack[-1]
            if not edges[curr]:
                return_iternary.append(stack.pop())
            else:
                stack.append(edges[curr].pop())
        return return_iternary[::-1]



        


        