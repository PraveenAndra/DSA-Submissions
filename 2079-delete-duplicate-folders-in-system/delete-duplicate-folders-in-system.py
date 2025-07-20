class Trie: 
    serial: str = ""
    children: dict

    def __init__(self):
        self.children = dict()


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # root node
        root = Trie()

        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]
        # print(list(root.children.items()))
        freq = Counter()
        def construct(node: Trie) -> None:
            if not node.children:
                return
            v = list()
            for folder, child in node.children.items():
                construct(child)
                v.append(folder + "(" + child.serial + ")")

            v.sort()
            node.serial = "".join(v)
            freq[node.serial] += 1

        construct(root)
        # print(freq)

        ans = list()
        path = list()

        def operate(node: Trie) -> None:
            print(node.serial)
            if freq[node.serial] > 1:
                return
            if path:
                ans.append(path[:])
            # print(ans)
            
            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()

        operate(root)
        return ans