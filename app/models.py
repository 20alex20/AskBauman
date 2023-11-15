from django.db import models
from django.contrib.auth.models import User


class ProfileManager(models.Manager):
    def leaders(self):
        return self.order_by('-points').values('user')[:10]

    def get_user_by_qobj(self, qobj):
        return qobj.author.annotate(type=Rating.objects.get_rating(models.F('points')))

    def get_user_by_id(self, id):
        return self.get(id=id)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.CharField(max_length=32, null=True)
    points = models.IntegerField(default=0)

    objects = ProfileManager()


class TagManger(models.Manager):
    def popular(self):
        return self.annotate(count=Question.objects.filter(Tags__id=models.F('id')).count()
                             ).order_by('-count')[:10].values_list('name', flat=True)


class Tag(models.Model):
    name = models.CharField(max_length=32)
    mentions = models.IntegerField(default=0)

    objects = TagManger()

    def __str__(self):
        return str(self.name)


class QuestionManager(models.Manager):
    def sorted_by_date(self):
        return self.order_by("-date_time")

    def sorted_by_likes(self):
        return self.order_by("-likes", "-date_time")

    def with_tag(self, name):
        tag_id = Tag.objects.get(name=name).id
        return self.annotate(tag_id=tag_id).filter(tag_id__in=models.F("tags")).order_by("-date_time")

    def get_question(self, qid):
        return self.get(id=qid)

    def of_user(self, id):
        return self.filter(author=Profile.objects.get_user_by_id(id)).order_by("-date_time")


class Question(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="Tags")
    date_time = models.DateTimeField()
    title = models.CharField(max_length=512)
    text = models.TextField(null=True)
    num_likes = models.IntegerField(default=0)
    likes = models.ManyToManyField(Profile, related_name="Likes")
    num_dislikes = models.IntegerField(default=0)
    dislikes = models.ManyToManyField(Profile, related_name="Dislikes")
    num_answers = models.IntegerField(default=0)
    solved = models.BooleanField(default=False)

    objects = QuestionManager()


class AnswerManager(models.Manager):
    def of_question(self, qobj):
        return self.filter(question=qobj).annotate(user=models.F("author").user).order_by("-date_time")


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    text = models.TextField()
    is_solving = models.BooleanField(default=False)

    objects = AnswerManager()


class RatingManager(models.Manager):
    def get_rating(self, points):
        return self.filter(minimum__gt=points).order_by('-minimum')[0].name


class Rating(models.Model):
    minimum = models.IntegerField()
    name = models.CharField(max_length=32)

    objects = RatingManager()
