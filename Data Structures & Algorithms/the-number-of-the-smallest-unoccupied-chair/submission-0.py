
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        import heapq

        friends = sorted(
            (arrival, leaving, i)
            for i, (arrival, leaving) in enumerate(times)
        )

        occupied = []
        available = []
        next_chair = 0

        for arrival, leaving, friend in friends:

            # Release chairs of friends who have left
            while occupied and occupied[0][0] <= arrival:
                leave_time, chair = heapq.heappop(occupied)
                heapq.heappush(available, chair)

            # Assign the smallest available chair
            if available:
                chair = heapq.heappop(available)
            else:
                chair = next_chair
                next_chair += 1

            # Check whether this is the target friend
            if friend == targetFriend:
                return chair

            # Mark the chair as occupied
            heapq.heappush(occupied, (leaving, chair))

        return -1
        #Time and space is O(n*logn) and O(n) respectively
