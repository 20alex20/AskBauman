# Generated by Django 4.2.7 on 2023-11-14 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_profile_tag_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='author',
        ),
        migrations.RemoveField(
            model_name='question',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tagquestion',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
