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

    @property
    def username(self):
        return self.user.username

    @classmethod
    def get_by_username(cls, username):
        return cls.objects.get(user__username=username)


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=185)
    screenshot = models.ImageField(upload_to='uploads')
    live_link = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='projects',
    )

    @classmethod
    def search_project(cls, search_term):
        return cls.objects.filter(title__istartswith=search_term)


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
