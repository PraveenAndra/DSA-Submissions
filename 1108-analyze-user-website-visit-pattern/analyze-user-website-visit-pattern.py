class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visits = defaultdict(list)
        for u, t, w in zip(username, timestamp, website):
            user_visits[u].append((t, w))
        
        # Step 2: Generate all patterns for each user
        pattern_count = Counter()
        for visits in user_visits.values():
            # Sort the visits based on timestamps
            visits.sort()
            
            # Step 3: Extract all unique patterns of 3 websites in order
            visited_websites = [w for _, w in visits]
            patterns = set()
            
            # Generate all unique patterns of length 3
            for i in range(len(visited_websites) - 2):
                for j in range(i + 1, len(visited_websites) - 1):
                    for k in range(j + 1, len(visited_websites)):
                        patterns.add((visited_websites[i], visited_websites[j], visited_websites[k]))
            
            # Increment the count of each pattern
            for pattern in patterns:
                pattern_count[pattern] += 1
        
        # Step 4: Find the pattern with the largest score
        max_count = max(pattern_count.values())
        best_pattern = min(pattern for pattern, count in pattern_count.items() if count == max_count)
        
        return list(best_pattern)
