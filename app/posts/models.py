from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Posts(models.Model):
    user_id = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    image_url = models.TextField(null=True, blank=True)
    price = models.FloatField(null=False, blank=False)
    levels = models.PositiveIntegerField(null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
