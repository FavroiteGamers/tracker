from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import TrackerUser
from django import forms 
from django.utils import timezone


class Food(models.Model): 
    name = models.CharField(max_length=100)
    calories = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])
    fat = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])
    carbs = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])
    protein = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000)])
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'foods'

class Exercise(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.name

class Time(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class FoodIntsance(models.Model):
      user = models.ForeignKey(TrackerUser, on_delete=models.CASCADE)
      food = models.ForeignKey(Food, on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      times = models.CharField(max_length=15)
      date = models.DateField(default=timezone.now)
      calories = models.IntegerField() 
      
      def __str__(self):
        return self.times


class ExerciseInstance(models.Model):
    user = models.ForeignKey(TrackerUser, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    times = models.CharField(max_length=15)
    date = models.DateField(default=timezone.now)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.times} - {self.duration}"
     


      