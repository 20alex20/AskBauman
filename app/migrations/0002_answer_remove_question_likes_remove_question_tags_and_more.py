# Generated by Django 4.2.7 on 2023-11-13 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('text', models.TextField()),
                ('is_solving', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.AddField(
            model_name='profile',
            name='likes',
            field=models.ManyToManyField(related_name='Likes', to='app.question'),
        ),
        migrations.AddField(
            model_name='tag',
            name='tags',
            field=models.ManyToManyField(related_name='TagQuestion', to='app.question'),
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question'),
        ),
    ]