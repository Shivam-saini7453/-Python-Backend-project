from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Employee

class EmployeeTests(APITestCase):
    def test_create_employee(self):
        url = reverse('employee-list-create')
        data = {'name': 'John Doe', 'email': 'john@example.com'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_employees(self):
        url = reverse('employee-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_employee(self):
        # Assuming there's an employee with ID=1
        url = reverse('employee-detail', args=[1])
        data = {'name': 'Updated Name'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_employee(self):
        # Assuming there's an employee with ID=1
        url = reverse('employee-detail', args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
