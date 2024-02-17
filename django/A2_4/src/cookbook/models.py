from django.db import models

# Create your models here.
# name_choices= (
# ('cake', 'Cake'),
# ('tea', 'Tea'),
# ('brownies', 'Brownies'),
# )

# cooking_time_choices=(
# (50),
# (5),
# (15)
# )
# difficulty_choice=(
# ('hard'),
# ('easy'),
# ('intermediate')
# )

class Cookbook(models.Model):
    name=models.CharField(max_length=50)
    cooking_time=models.IntegerField()
    difficulty=models.CharField(max_length=50)

    def __str__(self):
        return str(self.name, self.cooking_time, self.difficulty)