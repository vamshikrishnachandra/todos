# tests/test.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from tasks.models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test task
        self.task = Task.objects.create(user=self.user, name='Test Task', description='This is a test task')

    def test_task_list_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Access the task list view
        response = self.client.get(reverse('task_list'))

        # Check if the task is present in the response
        self.assertContains(response, 'Test Task')

    def test_task_detail_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Access the task detail view
        response = self.client.get(reverse('task_detail', args=[self.task.id]))

        # Check if the task details are present in the response
        self.assertContains(response, 'Test Task')
        self.assertContains(response, 'This is a test task')

    # Add more test cases as needed

    def tearDown(self):
        # Clean up after the test
        self.task.delete()
        self.user.delete()
