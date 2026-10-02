class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)) + "#" + s)
        return res    
    def decode(self, s: str) -> List[str]:
        res = []
        length = 0
        while s != "":
            c = s[0]
            if c == "#":
                res.append(s[1:length + 1])
                s = s[length + 1:]
                length = 0
            else:
                length = 10 * length + int(c)
                s = s[1:]
        return res
            