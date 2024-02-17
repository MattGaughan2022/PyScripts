from django.db import models

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    cooking_time=models.IntegerField()
    difficulty=models.CharField(max_length=50)

    def __str__(self):
        return str(self.name + self.category + self.difficulty)


