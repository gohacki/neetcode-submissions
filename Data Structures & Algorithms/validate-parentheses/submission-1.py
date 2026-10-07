class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = { ")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in ")]}":
                if stack == []:
                    return False
                mapped = stack.pop()
                if maps[c] != mapped:
                    return False
            else:
                stack.append(c)
        if stack != []:
            return False
        return True
