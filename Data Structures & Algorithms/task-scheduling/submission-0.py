from collections import Counter
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        heap=[-freq for freq in count.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0

        while heap or queue:
            time += 1

            # Process the most frequent available task
            if heap:
                freq = heapq.heappop(heap)
                freq += 1

                # If tasks remain, put it into cooldown queue
                if freq != 0:
                    queue.append((freq, time + n))

            # Move tasks whose cooldown is finished back to heap
            if queue and queue[0][1] == time:
                freq, available_time = queue.popleft()
                heapq.heappush(heap, freq)

            # If heap is empty, jump over idle time
            if not heap and queue:
                time = queue[0][1] - 1

        return time
        #TIme and space is O(m) and O(1) respectively