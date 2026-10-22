from typing import List
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_count={}
        for word in words:
            prefix=""
            for ch in word:
                prefix+=ch
                if prefix not in prefix_count:
                    prefix_count[prefix]=0
                prefix_count[prefix]+=1
        result=[]
        for word in words:
            prefix = ""
            score = 0

            for ch in word:
                prefix += ch
                score += prefix_count[prefix]

            result.append(score)

        return result
        #TIme and space is O(n*m^2) and O(n* m^2) respectively