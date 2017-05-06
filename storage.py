"""
'In memory' storage for tweets
"""
import pg8000
import functools


def uses_db(f):
    @functools.wraps(f)
    def wrapper(cls, *args, **kwargs):
        cursor = cls._conn.cursor()
        res = f(cls, cursor, *args, **kwargs)
        cursor.close()
        cls._conn.commit()
        return res
    return wrapper


class Storage(object):
    _conn = pg8000.connect(
        user="radionica",
        host="localhost",
        database="radionica",
        password="P4ss"
    )

    @classmethod
    @uses_db
    def get_tweets(cls, cursor):
        """Returns list of all tweets"""
        cursor.execute("""SELECT id, name, tweet FROM tweets""")
        tweets = cursor.fetchall()
        return tweets

    @classmethod
    @uses_db
    def get_tweet(cls, cursor, tweet_id):
        """Returns tweet object if found else returns None"""
        cursor.execute("""SELECT id, name, tweet FROM tweets WHERE id=%s""", (tweet_id,))
        tweet = cursor.fetchone()
        return tweet

    @classmethod
    @uses_db
    def add_tweet(cls, cursor, tweet, username):
        """Creates, stores and returns new tweet object"""
        cursor.execute(
            """
            INSERT INTO tweets (name, tweet)
            VALUES ( %s, %s ) RETURNING id, name, tweet
            """,
            (username, tweet)
        )
        new_tweet = cursor.fetchone()
        return new_tweet

    @classmethod
    @uses_db
    def remove_tweet(cls, cursor, tweet_id):
        """Deletes a tweet with given id"""
        cursor.execute(
            """
            DELETE FROM tweets
            WHERE id=%s
            """,
            (tweet_id,)
        )
