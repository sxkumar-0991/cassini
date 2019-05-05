from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from .models import Songs
from .serializers import SongsSerializer
from rest_framework.views import status

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title,artist=artist)

    def setUp(self):
        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("jam rock", "metallica")
        self.create_song("unforgiven", "metallica")


class GetAllSongsTest(BaseViewTest):
    def test_all_songs_list(self):
        response = self.client.get(reverse("all-songs", kwargs={"version":"v1"}))

        expected = Songs.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

