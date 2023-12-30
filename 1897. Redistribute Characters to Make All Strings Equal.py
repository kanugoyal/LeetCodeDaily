from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts =  Counter("".join(words))
        for i in counts.values():
            if i%len(words)!=0:
                return False
        return True