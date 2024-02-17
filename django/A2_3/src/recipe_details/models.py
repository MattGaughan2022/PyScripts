from django.db import models

# Create your models here.
class Recipe_Details(models.Model):
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    cooking_time=models.IntegerField()
    difficulty=models.CharField(max_length=50)
    instructions=models.TextField()
    nutrition_facts=models.TextField()
    #metrics_for_queries=models.ExpressionList()

    def __str__(self):
        return str(self.name, self.category, self.cooking_time, self.difficulty, self.instructions, self.nutrition_facts)