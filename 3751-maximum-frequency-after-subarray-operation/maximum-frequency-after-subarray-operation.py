class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        initial_k_count = nums.count(k)
        max_gain = 0

        for target_val in range(1, 51):
            if target_val == k:
                continue
            
            gain_array = []
            for num in nums:
                if num == target_val:
                    gain_array.append(1)
                elif num == k:
                    gain_array.append(-1)
                else:
                    gain_array.append(0)
            
            current_max_gain = 0
            for gain in gain_array:
                current_max_gain = max(0, current_max_gain + gain)
                max_gain = max(max_gain, current_max_gain)
        
        return initial_k_count + max_gain
    
        