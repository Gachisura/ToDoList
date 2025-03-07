from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):
    OPEN = 'opened'
    CLOSED = 'closed'

    STATUS_CHOICES = [
        (OPEN, 'Открыто'),
        (CLOSED, 'Закрыто'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    tag = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=OPEN)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    class Meta:
        ordering = ['-created_at']

        def __str__(self) -> str:
            return self.title
