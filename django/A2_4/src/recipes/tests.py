from django.test import TestCase

# Create your tests here.
from django.db import models
from .models import Recipe

# name=models.CharField(max_length=50)
# cooking_time=models.IntegerField()
# difficulty=models.CharField(max_length=50)

# Create your models here.
# % python manage.py test cookbook.tests.myTestclass
# python manage.py test cookbook/tests/

class myTestClass(TestCase):
    def setUpTestData():
        Recipe.objects.create(name='tea',
            cooking_time=5, difficulty='easy',category='beverage')
    def test_name_max_length(self):
           recipe = Recipe.objects.get(id=1)
           max_length = recipe._meta.get_field('name').max_length
           self.assertEqual(max_length, 50)