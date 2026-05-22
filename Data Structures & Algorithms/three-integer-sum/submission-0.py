class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        listSorted = sorted(nums)
        finalList = []
        for i in range(len(nums)):
            L = i + 1
            R = len(nums) - 1
            if i > 0 and listSorted[i] == listSorted[i - 1]:
                continue
            while L < R:
                if listSorted[i] + listSorted[L] + listSorted[R] == 0:
                    finalList.append([listSorted[i], listSorted[L], listSorted[R]])
                    L += 1
                    R -= 1
                    while L < R and listSorted[L] == listSorted[L - 1]:
                        L += 1
                    while L < R and listSorted[R] == listSorted[R + 1]:
                        R -= 1
                elif listSorted[i] + listSorted[L] + listSorted[R] < 0:
                    L += 1
                else:
                    R -= 1
        return finalList


