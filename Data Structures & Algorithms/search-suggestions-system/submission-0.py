class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        from bisect import bisect_left
        products.sort()
        ans=[]
        prefix=""
        for ch in searchWord:
            prefix+=ch
            i=bisect_left(products, prefix)
            suggestions = []

            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
                else:
                    break

            ans.append(suggestions)

        return ans
        #TIme and space is O(M*L) and O(M*l) respectively

