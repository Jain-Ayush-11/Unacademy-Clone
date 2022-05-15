# Generated by Django 3.2.10 on 2022-01-28 09:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('educator', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=20)),
                ('birth', models.DateField(blank=True, default='2004-01-01', null=True)),
                ('picture', models.CharField(blank=True, max_length=700, null=True)),
                ('standard', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('bio', models.TextField(blank=True, null=True)),
                ('following', models.ManyToManyField(blank=True, related_name='educator_followers', to='educator.EducatorDetail')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
                ('wishlist', models.ManyToManyField(blank=True, related_name='wishlist', to='educator.Series')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_quiz', to='educator.quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_score', to='student.studentdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Attempted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
                ('is_correct', models.BooleanField(blank=True, default=False, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_attempted', to='educator.question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_attempted', to='student.studentdetail')),
            ],
        ),
    ]