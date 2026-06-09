class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for tweet in self.tweetMap[userId]:
            feed.append(tweet)
        for followee in self.followMap[userId]:
            for tweet in self.tweetMap[followee]:
                feed.append(tweet)
        feed.sort(reverse=True)
        ans = []
        for i in range(min(10, len(feed))):
            ans.append(feed[i][1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
