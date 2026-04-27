class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dics = {}

        for string in strs:
            dic = [0]*26
            for i in string:
                dic[ord(i) - ord('a')] += 1

            if tuple(dic) in dics.keys():
                dics[tuple(dic)].append(string)
            else:
                dics[tuple(dic)] = [string]
        
        return list(dics.values())