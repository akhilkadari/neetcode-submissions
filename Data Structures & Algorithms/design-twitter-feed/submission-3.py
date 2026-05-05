class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetsByUser = {} # {userId : [(time, tweetId)]}
        self.following = {} # {followerId : set of followeeIds}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.following:
            self.following[userId] = set()
        if userId not in self.tweetsByUser:
            self.tweetsByUser[userId] = []
        
        self.time += 1
        self.tweetsByUser[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId] = set()
        if userId not in self.tweetsByUser:
            self.tweetsByUser[userId] = []

        candidateUsers = set(self.following[userId])
        candidateUsers.add(userId)
        
        heap = []
        for authorId in candidateUsers:
            tweets = self.tweetsByUser.get(authorId, [])
            if not tweets:
                continue
            
            lastIndex = len(tweets)-1
            timePosted, tweetId = tweets[lastIndex]
            heapq.heappush(heap, (-timePosted, tweetId, authorId, lastIndex))
        
        res = []
        while heap and len(res) < 10:
            time, tweetId, authorId, tweetIndex = heapq.heappop(heap)
            res.append(tweetId)

            nextIndex = tweetIndex-1
            if nextIndex >= 0:
                timePosted, nextTweetId = self.tweetsByUser[authorId][nextIndex]
                heapq.heappush(heap,(-timePosted, nextTweetId, authorId, nextIndex))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        if followerId not in self.tweetsByUser:
            self.tweetsByUser[followerId] = []
        if followeeId not in self.following:
            self.following[followeeId] = set()
        if followeeId not in self.tweetsByUser:
            self.tweetsByUser[followeeId] = []

        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        if followerId not in self.tweetsByUser:
            self.tweetsByUser[followerId] = []
        if followeeId not in self.following:
            self.following[followeeId] = set()
        if followeeId not in self.tweetsByUser:
            self.tweetsByUser[followeeId] = []
        
        self.following[followerId].discard(followeeId)
        
