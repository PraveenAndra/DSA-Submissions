class Solution:
    def betterCompression(self, compressed: str) -> str:
        counter = [0]*26
        curr_char = compressed[0]
        curr_count = 0
        for char in compressed[1:]:
            if char.isdigit():
                if curr_count > 0:
                    curr_count = curr_count *10 + int(char)
                else:
                    curr_count = int(char)
            else:
                if curr_count >= 1:
                    counter[ord(curr_char)-ord('a')] += curr_count
                curr_char = char
                curr_count = 0
        
        counter[ord(curr_char)-ord('a')] += curr_count
        # print(counter)
        res = ""
        for i in range(26):
            if counter[i] > 0:
                res+=chr(ord('a')+i)
                res+= str(counter[i])
        return res

        