from django.test import TestCase

# Create your tests here.
from django.db import models
from .models import Recipe_Details

# name=models.CharField(max_length=50)
# cooking_time=models.IntegerField()
# difficulty=models.CharField(max_length=50)

# Create your models here.
# % python manage.py test cookbook.tests.myTestclass
# python manage.py test cookbook/tests/

class myTestClass(TestCase):
    def setUpTestData():
        Recipe_Details.objects.create(name='tea',
            cooking_time=5, difficulty='easy',category='beverage',
            instructions='1. Boil water water. 2. Let tea bag seep in hot water. 3. Add a tablespoon of honey and remove tea bag.',
            nutrition_facts='10 calories, 0 sugar')
    def test_name_max_length(self):
           recipe = Recipe_Details.objects.get(id=1)
           max_length = recipe._meta.get_field('name').max_length
           self.assertEqual(max_length, 50)