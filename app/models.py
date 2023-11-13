from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.CharField(max_length=32, null=True, default=None)
    points = models.IntegerField(default=0)


class Tag(models.Model):
    name = models.CharField(max_length=32)
    mentions = models.IntegerField(default=0)


class Question(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tagquestion = models.ManyToManyField(Tag, related_name="TagQuestion")
    date_time = models.DateTimeField()
    title = models.CharField(max_length=512)
    text = models.TextField(null=True)
    num_likes = models.IntegerField(default=0)
    likes = models.ManyToManyField(Profile, related_name="Likes")
    num_dislikes = models.IntegerField(default=0)
    dislikes = models.ManyToManyField(Profile, related_name="Dislikes")
    solve = models.BooleanField(default=False)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    text = models.TextField()
    is_solving = models.BooleanField(default=False)


class Rating(models.Model):
    minimum = models.IntegerField()
    name = models.CharField(max_length=32)
