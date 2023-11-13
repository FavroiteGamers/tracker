from django.contrib import admin
from app.models import Exercise, Food, FoodIntsance, Time, ExerciseInstance

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass

@admin.register(Exercise)
class exerciseAdmin(admin.ModelAdmin):
    pass

@admin.register(FoodIntsance)
class foodInstanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Time)
class timesAdmin(admin.ModelAdmin):
    pass

@admin.register(ExerciseInstance)
class exerciseInstanceAdmin(admin.ModelAdmin):
    pass


