from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    """
    The todo model
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    done = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    date_finished = models.DateField(auto_now=True, null=True)

    def __str__(self):
        """
        object representation
        """
        return self.title
