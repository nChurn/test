import redis

from django.test import TestCase, Client
from django.conf import settings
from .logic import get_emotitoken

client = Client()

class GetEmotitokenTest(TestCase):

    def setUp(self):
        conn = redis.StrictRedis(host=settings.CONF['REDIS_HOST'], port=settings.CONF['REDIS_PORT'], db=0)
        conn.set("test_description.1000.1000", "test_image")

    def test_get_emotitoken(self):
        self.assertEqual(get_emotitoken("test_description", 1000, 1000), "test_image")
