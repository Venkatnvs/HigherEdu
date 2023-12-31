# Generated by Django 4.2.7 on 2023-12-10 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applies', '0006_competitivecourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitiveCourseApplied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(blank=True, to='applies.competitivecourse')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
