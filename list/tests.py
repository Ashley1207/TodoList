from django.test import TestCase
from list.models import Content
from list import views

# Create your tests here.
class ContentTest(TestCase):
    def test_creat(self):
        url = reversed('creatTodoList')
        data = {
            'content':'aaa'
        }
        self.response = self.client.post(url,data)
        #self.assertTrue(Content.objects.exists())

    def test_details(self):
        response = self.client.get('/list/creatTodoList/')
        self.assertEqual(response.status_code, 200)

    def test_index(self):
        response = self.client.get('/list/deleteTodoList/')
        self.assertEqual(response.status_code, 200)

