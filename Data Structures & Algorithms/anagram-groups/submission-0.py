class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedList = []
        sortedKey = {}
        for i in range(len(strs)):
            sortedList.append(''.join(sorted(strs[i])))
            if sortedList[i] in sortedKey:
                #check if sorted str alr in our key, if so add our str to that value list
                sortedKey[sortedList[i]].append(strs[i])
            else: 
                sortedKey[sortedList[i]] = [strs[i]]
        return list(sortedKey.values())