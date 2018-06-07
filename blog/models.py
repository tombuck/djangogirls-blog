from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    # author
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # title
    title = models.CharField(max_length=200)
    # post body
    text = models.TextField()
    # created date
    created_date = models.DateTimeField(
        default=timezone.now)
    # pubdate
    published_date = models.DateTimeField(
        blank=True, null=True)

    #method for publishing
    def publish(self):
        self_published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
