class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ""
        for word in strs:
            s += (word.replace("/","//")+'/:')
        return s

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        res = []
        curr_s = ""
        while i < len(s):
            if s[i:i+2] == "/:":
                res.append(curr_s)
                curr_s = ""
                i += 2
            elif s[i:i+2] == "//":
                curr_s += "/"
                i+= 2
            else:
                curr_s += s[i]
                i += 1
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))