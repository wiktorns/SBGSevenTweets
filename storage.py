"""
'In memory' storage for tweets
"""


class Storage(object):
    # Key - tweet id, Value - Dictionary with id, username and message
    _tweets = {}
    # Counter used for ids
    _id_gen = 0

    @classmethod
    def next_id(cls):
        """Generates next valid id"""
        cls._id_gen += 1
        return cls._id_gen

    @classmethod
    def get_tweets(cls):
        """Returns list of all tweets"""
        return list(cls._tweets.values())

    @classmethod
    def get_tweet(cls, tweet_id):
        """Returns tweet object if found else returns None"""
        if tweet_id not in cls._tweets.keys():
            return None

        return cls._tweets[tweet_id]

    @classmethod
    def add_tweet(cls, tweet, username):
        """Creates, stores and returns new tweet object"""
        tweet_id = cls.next_id()
        cls._tweets[tweet_id] = {"id": tweet_id, "name": username, "message": tweet}

        return cls._tweets[tweet_id]

    @classmethod
    def remove_tweet(cls, tweet_id):
        """Deletes a tweet with given id"""
        if tweet_id in cls._tweets.keys():
            del cls._tweets[tweet_id]
