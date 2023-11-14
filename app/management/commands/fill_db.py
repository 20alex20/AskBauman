from django.core.management import BaseCommand
from faker import Faker
from app.models import *
import datetime as dt


fake = Faker()


def random_choice(arr, length):
    answer = []
    i = fake.random_int(min=0, max=length // 7)
    while i < length:
        answer.append(arr[i])
        i += fake.random_int(min=1, max=length // 7)
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
        print("users")
        User.objects.bulk_create(users)
        users = User.objects.all()
        print("users_bulk")

        profiles = [
            Profile(
                user=users[i],
                avatar=str(i),
                points=fake.random_int(min=0, max=100000)
            ) if fake.boolean() else
            Profile(
                user=users[i],
                points=fake.random_int(min=0, max=100000)
            ) for i in range(num)
        ]
        print("profiles")
        Profile.objects.bulk_create(profiles)
        profiles = Profile.objects.all()
        profiles_count = profiles.count()
        print("profiles_bulk")

        tags = [
            Tag(
                name=fake.word(),
                mentions=fake.random_int(min=0, max=num*10)
            ) for _ in range(num)
        ]
        print("tages")
        Tag.objects.bulk_create(tags)
        tags = Tag.objects.all()
        tags_count = tags.count()
        print("tages_bulk")

        questions = [
            Question(
                author=profiles[fake.random_int(min=0, max=profiles_count - 1)],
                date_time=fake.date_time_between(start_date='-3y', end_date='-1y').astimezone(dt.timezone.utc),
                title=fake.sentence().replace('.', ''),
                text='\n'.join((fake.text(), fake.text(), fake.text())),
                num_likes=fake.random_int(min=0, max=num*100),
                num_dislikes=fake.random_int(min=0, max=num*100),
                solved=fake.boolean()
            ) for _ in range(num * 10)
        ]
        print("questions")
        Question.objects.bulk_create(questions)
        questions = Question.objects.all()
        questions_count = questions.count()
        print("questions_bulk")
        for i, question in enumerate(questions):
            question.tagquestion.add(*random_choice(tags, tags_count))
            question.likes.add(*random_choice(profiles, profiles_count))
            question.dislikes.add(*random_choice(profiles, profiles_count))
            if i % 100 == 0:
                print("questions_" + str(i))

        answers = [
            Answer(
                question=questions[fake.random_int(min=0, max=questions_count - 1)],
                author=profiles[fake.random_int(min=0, max=profiles_count - 1)],
                date_time=fake.date_time_between(start_date='-1y', end_date='+1y').astimezone(dt.timezone.utc),
                text=fake.text(),
                is_solving=fake.boolean()
            ) for _ in range(num * 100)
        ]
        print("answers")
        Answer.objects.bulk_create(answers)
        print("answers_bulk")

        names = ["Высший разум", "Искусственный Интеллект", "Гений", "Оракул", "Просветленный", "Мудрец", "Мыслитель",
                 "Гуру", "Мастер", "Профи", "Знаток", "Ученик", "Новичок"][::-1]
        ratings = [
            Rating(
                minimum=0,
                name=names[0]
            )
        ]
        n = 50.0
        for i in range(1, 13):
            ratings.append(
                Rating(
                    minimum=round(n),
                    name=names[i]
                )
            )
            n *= 1.873818  # максимальное получаемое число 50000
        print("ratings")
        Rating.objects.bulk_create(ratings)
        print("ratings_bulk")
