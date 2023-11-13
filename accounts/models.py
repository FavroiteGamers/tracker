from django.db import models

from django.contrib.auth.models import AbstractUser

class TrackerUser(AbstractUser):
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    gender = models.ManyToManyField("Gender", blank=True)
    exercise = models.ForeignKey('app.Exercise', on_delete=models.CASCADE, blank=True, null=True)
    friends = models.ManyToManyField("TrackerUser", blank=True)
    age = models.IntegerField(default=0)

class Gender(models.Model):
      gender = models.TextField(max_length=10)

      def __str__(self):
           return self.gender

class Friend_Request(models.Model):
     from_user = models.ForeignKey(
          TrackerUser, related_name='from_user', on_delete=models.CASCADE)
     to_user = models.ForeignKey(
          TrackerUser, related_name='to_user', on_delete=models.CASCADE)