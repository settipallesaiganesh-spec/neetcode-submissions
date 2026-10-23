from collections import defaultdict,deque
from typing import List
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        indegree={}
        for i , recipe in enumerate(recipes):
            indegree[recipe]=len(ingredients[i])
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
        queue = deque(supplies)
        result = []

        while queue:
            item = queue.popleft()

            for recipe in graph[item]:
                indegree[recipe] -= 1

                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)

        return result
        #TIme and space is O(n+m+S) and O(n+M+S) respectively