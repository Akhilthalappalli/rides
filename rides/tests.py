from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ride

class RideModelTest(TestCase):
    def test_create_ride(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        ride = Ride.objects.create(
            rider=user,
            pickup_location='Point A',
            dropoff_location='Point B',
            status='requested'
        )
        self.assertEqual(ride.status, 'requested')
