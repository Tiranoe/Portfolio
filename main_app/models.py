from django.db import models

# Create your models here.
class Project(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    tool = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    github = models.CharField(max_length=250)
    live = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    company = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.email