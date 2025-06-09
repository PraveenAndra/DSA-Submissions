class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # l = len(nums)
        # dp = [[0]*nums for i in range(l)]
        # for i in range(l):
        #     for j in range(l):
        #         if 
        tails = [0] * len(nums)
        result = 0
        for num in nums:
            left_index, right_index = 0, result
            # print("Before Loop")
            print(num,left_index,right_index)
            # print("In loop")
            while left_index != right_index:
                middle_index = left_index + (right_index - left_index) // 2
                if tails[middle_index] < num:
                    left_index = middle_index + 1
                else:
                    right_index = middle_index
                # print(left_index,middle_index,right_index)
            result = max(result, left_index + 1)
            # print("Result "+str(result))
            tails[left_index] = num
            # print(tails)
        return result

        