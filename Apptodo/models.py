from django.db import models

# Create your models here.
class Todoclass(models.Model):
    header = models.CharField(max_length=500)
    main_text = models.TextField(blank=True)

    def __str__(self):
        return f'{self.header}'
