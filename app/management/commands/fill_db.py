from django.core.management import BaseCommand
from faker import Faker
from app.models import *
import datetime as dt


fake = Faker()


def random_choice(arr, length):
    answer = []
    i = fake.random_int(min=0, max=length // 10)
    while i < length:
        answer.append(arr[i])
        i += fake.random_int(min=1, max=length // 10)
    return answer


class Command(BaseCommand):
    help = "Fills database with fake data"

    def add_arguments(self, parser):
        parser.add_argument("num", type=int)

    def handle(self, *args, **kwargs):
        num = kwargs['num']

        users = [
            User(
                username=fake.user_name() + str(i),
                email=fake.email(),
                password=fake.password(),
                last_login=fake.date_time_between(start_date='-1y', end_date='+1y').astimezone(dt.timezone.utc)
            ) for i in range(num)
        ]
        User.objects.bulk_create(users)
        users = User.objects.all()

        profiles = [
            Profile(
                user=users[i],
                avatar=(str(i), None)[fake.random_int(min=0, max=1)]
            ) for i in range(num)
        ]
        Profile.objects.bulk_create(profiles)
        profiles = Profile.objects.all()
        profiles_count = profiles.count()

        tags = [
            Tag(
                name=fake.word()
            ) for _ in range(num)
        ]
        Tag.objects.bulk_create(tags)
        tags = Tag.objects.all()
        tags_count = tags.count()

        questions = [
            Question(
                author=profiles[fake.random_int(min=0, max=profiles_count - 1)],
                date_time=fake.date_time_between(start_date='-3y', end_date='-1y').astimezone(dt.timezone.utc),
                title=fake.sentence().replace('.', ''),
                text=fake.text()
            ) for _ in range(num * 10)
        ]
        Question.objects.bulk_create(questions)
        questions = Question.objects.all()
        for question in questions:
            question.tagquestion.add(*random_choice(tags, tags_count))
            question.likes.add(*random_choice(profiles, profiles_count))
            question.dislikes.add(*random_choice(profiles, profiles_count))
        questions_count = questions.count()

        answers = [
            Answer(
                question=questions[fake.random_int(min=0, max=questions_count - 1)],
                author=profiles[fake.random_int(min=0, max=profiles_count - 1)],
                date_time=fake.date_time_between(start_date='-1y', end_date='+1y').astimezone(dt.timezone.utc),
                text=fake.sentences()
            ) for _ in range(num * 100)
        ]
        Answer.objects.bulk_create(answers)


        # TagQuestion = Tag.rated_by.through
        # tagquestions = [
        #     TagQuestion(
        #         tag=tags[fake.random_int(min=0, max=tags_count - 1)],
        #         question=questions[fake.random_int(min=0, max=questions_count - 1)]
        #     ) for _ in range(num * 20)
        # ]
        # TagQuestion.objects.bulk_create(tagquestions)
        #
        # Likes = Profile.rated_by.through
        # likes = [
        #     Likes(
        #         profile=profiles[fake.random_int(min=0, max=profiles_count - 1)],
        #         question=questions[fake.random_int(min=0, max=questions_count - 1)]
        #     ) for _ in range(num * 100)
        # ]
        # Likes.objects.bulk_create(likes)
        #
        # Dislikes = Question.rated_by.through
        # dislikes = [
        #     Dislikes(
        #         profile=profiles[fake.random_int(min=0, max=profiles_count - 1)],
        #         question=questions[fake.random_int(min=0, max=questions_count - 1)]
        #     ) for _ in range(num * 100)
        # ]
        # Dislikes.objects.bulk_create(dislikes)
