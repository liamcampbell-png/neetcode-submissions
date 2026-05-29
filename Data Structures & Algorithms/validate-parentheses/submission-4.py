class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = {"(" : ")", "{" : "}", "[" : "]"}
        listPush = []
        for i in s:
            if i in openBrackets.keys():
                listPush.append(i)
            elif not listPush:
                return False
            else:
                if i == ")":
                    if (listPush[-1], i) in openBrackets.items():
                        listPush.pop()
                    else:
                        return False
                elif i == "}":
                    if (listPush[-1], i) in openBrackets.items():
                        listPush.pop()
                    else:
                        return False
                else:
                    if (listPush[-1], i) in openBrackets.items():
                        listPush.pop()
                    else:
                        return False
        return True if len(listPush) == 0 else False