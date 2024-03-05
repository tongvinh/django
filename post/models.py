from django.db import models

# Create your models here.
class PostForm(models.Model):
    title = models.CharField(max_length= 255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
