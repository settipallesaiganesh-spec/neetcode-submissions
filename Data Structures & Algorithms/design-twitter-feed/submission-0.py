from typing import List
import heapq

class Twitter:

    def __init__(self):
        self.time=0
        self.tweets={}
        self.following={}


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId]=[]
        self.tweets[userId].append((self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following.get(userId, set()).copy()
        users.add(userId)

        for uid in users:
            if uid in self.tweets and self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][idx]
                heapq.heappush(heap, (-time, tweetId, uid, idx))

        feed = []

        while heap and len(feed) < 10:
            time, tweetId, uid, idx = heapq.heappop(heap)
            feed.append(tweetId)

            idx -= 1
            if idx >= 0:
                next_time, next_tweet = self.tweets[uid][idx]
                heapq.heappush(
                    heap, (-next_time, next_tweet, uid, idx)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)

        #Time and space is O(1) and O(U+m) respectively
