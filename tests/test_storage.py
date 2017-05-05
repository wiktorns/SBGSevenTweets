from storage import Storage
import unittest

_test_message = 'storage test'
_test_username = 'user test'


class TestStorage(unittest.TestCase):
    def test_next_id(self):
        first = Storage.next_id()
        sec = Storage.next_id()
        assert first != sec, "Ids must not repeat"

    def test_add_tweet(self):
        tweet = Storage.add_tweet(_test_message, _test_username)
        assert isinstance(tweet, dict), "Tweet should be a dictionary"
        assert tweet['name'] == _test_username, "Name should match given value"
        assert tweet['message'] == _test_message, "Message should match given value"

    def test_get_existing_tweet(self):
        tweet = Storage.add_tweet(_test_message, _test_username)
        tweet = Storage.get_tweet(int(tweet["id"]))
        assert tweet is not None, "Tweet should not be None"

    def test_get_non_existing_tweet(self):
        tweet = Storage.get_tweet(12)
        assert tweet is None, "Tweet should be None"

    def test_get_tweets(self):
        tweets = Storage.get_tweets()
        assert isinstance(tweets, list)
        assert len(tweets) == 2, "There should be two tweets"

    def test_remove_existing_tweet(self):
        tweets = Storage.get_tweets()
        tweets_before_removal = len(tweets)
        tweet_to_remove = int(tweets[0]["id"])
        Storage.remove_tweet(tweet_to_remove)
        tweets_after_removal = len(Storage.get_tweets())
        assert tweets_before_removal > tweets_after_removal, "Tweet should not be one tweet less"

    def test_remove_non_existing_tweet(self):
        tweets_before_removal = len(Storage.get_tweets())
        Storage.remove_tweet(55)
        tweets_after_removal = len(Storage.get_tweets())
        assert tweets_before_removal == tweets_after_removal, "Tweet should be same number of tweets"
