from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Post
from .serializers import PostSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_post(title="", content=""):
        if title != "" and content != "":
            Post.objects.create(title=title, content=content)

    def setUp(self):
        #add test data
        self.create_post("title1", "content1")
        self.create_post("title2", "content2")
        self.create_post("title3", "content3")

class GetAllPostsTest(BaseViewTest):

    def test_get_all_posts(self):
        """
        This test ensures that all posts added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(reverse("all-posts"))
        # fetch the data from db
        expected = Post.objects.all()
        print(expected)
        serialized = PostSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

