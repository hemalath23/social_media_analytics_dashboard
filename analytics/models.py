from django.contrib.auth.models import User
from django.db import models

class SocialMediaPlatform(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

class SocialMediaAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialMediaPlatform, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} on {self.platform.name}"

class Post(models.Model):
    account = models.ForeignKey(SocialMediaAccount, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    def __str__(self):
        return f"Post {self.post_id} by {self.account.username}"

class Analytics(models.Model):
    account = models.ForeignKey(SocialMediaAccount, on_delete=models.CASCADE)
    date = models.DateField()
    followers = models.IntegerField()
    posts = models.IntegerField()
    engagement_rate = models.FloatField()

    class Meta:
        unique_together = ('account', 'date')

    def __str__(self):
        return f"Analytics for {self.account.username} on {self.date}"
