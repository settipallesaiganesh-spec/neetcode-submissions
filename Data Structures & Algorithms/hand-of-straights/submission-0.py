class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count={}
        for card in hand:
            count[card]= count.get(card,0)+1
        hand.sort()
        for card in hand:
            if count[card]==0:
                continue
            for i in range(card, card+groupSize):
                if i not in count or count[i]==0:
                    return False
                count[i]-=1
        return True
        #Time and space complexity is O(n*logn ) and O(n ) respectively