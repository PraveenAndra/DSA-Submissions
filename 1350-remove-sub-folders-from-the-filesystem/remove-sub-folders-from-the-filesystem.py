class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        parent_directories = {}
        folder.sort()
        for path in folder:
            i = 1
            curr = "/"
            while i <= len(path):
                if i==len(path) and curr !="/" and curr not in parent_directories:
                    parent_directories[curr] = 1
                    break
                if path[i] == "/":
                    if curr in parent_directories:
                        break
                curr += path[i]
                i+=1
        return list(parent_directories.keys())
            
        