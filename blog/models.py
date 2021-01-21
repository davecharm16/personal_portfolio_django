from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title