from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=200, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.task
