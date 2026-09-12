from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1

        queue = deque(["0000"])
        visited = set(["0000"])
        turns = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()

                if current == target:
                    return turns

                for i in range(4):
                    digit = int(current[i])

                    # Turn the wheel forward
                    new_digit = (digit + 1) % 10
                    next_state = current[:i] + str(new_digit) + current[i + 1:]

                    if next_state not in dead and next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)

                    # Turn the wheel backward
                    new_digit = (digit - 1) % 10
                    next_state = current[:i] + str(new_digit) + current[i + 1:]

                    if next_state not in dead and next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)

            turns += 1

        return -1
        #Time and space complexity is O(1) and O(10^4) respectively