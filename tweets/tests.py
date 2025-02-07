from rest_framework.test import APITestCase
from .models import Tweet
from users.models import User


class TestTweets(APITestCase):

    test_payload = "Test payload"
    test_username = "elon"
    url = "/api/v1/tweets/"

    def setUp(self):
        user = User.objects.create_user(
            self.test_username,
            "elon@musk.com",
            "1234",
        )
        Tweet.objects.create(
            payload=self.test_payload,
            user=user,
        )
        self.user = user

    def test_all_tweets(self):

        response = self.client.get(self.url)
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["payload"],
            self.test_payload,
        )

    def test_create_tweet(self):
        self.client.force_login(self.user)
        new_tweet_payload = "new tweet payload"
        response = self.client.post(
            self.url,
            data={
                "payload": new_tweet_payload,
            },
        )
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["payload"],
            new_tweet_payload,
        )


class TestTweetDetail(APITestCase):

    test_payload = "Test payload"
    test_username = "elon"
    url = "/api/v1/tweets"

    def setUp(self):
        user = User.objects.create_user(
            self.test_username,
            "elon@musk.com",
            "1234",
        )
        Tweet.objects.create(
            payload=self.test_payload,
            user=user,
        )
        self.user = user

    def test_tweet_not_found(self):

        response = self.client.get(f"{self.url}/9")

        self.assertEqual(
            response.status_code,
            404,
            "Not 404 status code",
        )

    def test_get_tweet(self):

        response = self.client.get(f"{self.url}/1")
        data = response.json()
        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )
        self.assertEqual(
            data["payload"],
            self.test_payload,
        )

    def test_delete_tweet(self):

        response = self.client.delete(f"{self.url}/1")

        self.assertEqual(
            response.status_code,
            403,
            "Not 403 status code",
        )
        self.client.force_login(self.user)

        response = self.client.delete(f"{self.url}/1")

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )

        response = self.client.get(f"{self.url}/1")

        self.assertEqual(
            response.status_code,
            404,
            "Not 404 status code",
        )

    def test_edit_tweet(self):

        new_payload = "new payload"

        response = self.client.put(
            f"{self.url}/1",
            data={"payload": new_payload},
        )

        self.assertEqual(
            response.status_code,
            403,
            "Not 403 status code",
        )
        self.client.force_login(self.user)

        response = self.client.put(
            f"{self.url}/1",
            data={"payload": new_payload},
        )

        self.assertEqual(
            response.status_code,
            200,
            "Not 200 status code",
        )

        data = response.json()

        self.assertEqual(
            data["payload"],
            new_payload,
        )
