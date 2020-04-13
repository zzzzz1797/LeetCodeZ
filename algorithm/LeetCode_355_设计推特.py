"""
    设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。
    你的设计需要支持以下的几个功能：
        postTweet(userId, tweetId): 创建一条新的推文
        getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
        follow(followerId, followeeId): 关注一个用户
        unfollow(followerId, followeeId): 取消关注一个用户
"""
from collections import defaultdict
from typing import List

new_id = 0


class News:
    def __init__(self, item=None):
        global new_id
        self.next = None
        self.item = item
        self.timestamp = new_id
        new_id += 1


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 存放用户 以及用户对应的粉丝ID
        self.user_mapping = defaultdict(dict)
        self.user_news = defaultdict(News)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.user_mapping:
            self.user_mapping[userId] = {userId: userId}
        self.__create_feed(self.user_news[userId], tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = []
        for fans_id in self.user_mapping.get(userId, []):
            fans_news = self.user_news[fans_id]
            fans_news = fans_news.next
            while fans_news:
                res.append((fans_news.item, fans_news.timestamp))
                fans_news = fans_news.next
        res.sort(reverse=True, key=lambda i: i[1])
        return [i[0] for i in res[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """

        followee_dict = self.user_mapping.setdefault(followerId, {followerId: followerId})
        followee_dict[followeeId] = followeeId

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId != followerId:
            followee_dict = self.user_mapping.get(followerId)
            if followee_dict and followeeId in followee_dict:
                del followee_dict[followeeId]

    @classmethod
    def __create_feed(cls, news: News, tweet_id: int):
        root = news
        while root.next:
            root = root.next
        root.next = News(tweet_id)
