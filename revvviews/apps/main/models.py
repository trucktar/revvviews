from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    display_name = models.CharField(max_length=30)
    url = models.URLField()
    description = models.TextField(max_length=150)
    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default-user.png',
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=185)
    screenshot = models.ImageField(upload_to='uploads')
    live_link = models.URLField()

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='projects',
    )


class Review(models.Model):
    design = models.PositiveSmallIntegerField()
    usability = models.PositiveSmallIntegerField()
    content = models.PositiveSmallIntegerField()

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='+',
    )
