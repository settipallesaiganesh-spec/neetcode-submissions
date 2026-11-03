from collections import deque
from typing import List
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q=deque(range(len(deck)))
        result=[0]*len(deck)
        for card in deck:
            index=q.popleft()
            result[index]=card
            if q:
                q.append(q.popleft())

        return result
        #TIme and space is O(n*logn) and O(n) respectively