from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import ExerciseForm, FoodIntsance, ExerciseForm# Import your ExerciseForm
from .forms import FoodForm
from .models import ExerciseInstance
from .models import FoodIntsance
from .utils import calculate_bmr


# views.py
def create_food_instance(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            # Create a FoodInstance instance with the form data
            food_instance = FoodIntsance.objects.create(
                food=form.cleaned_data['food'],
                times=form.cleaned_data['times'],
                user=request.user,
                calories=form.cleaned_data['calories'],  # Make sure calories is provided
                # Add other fields as needed
            )

            # Redirect or do whatever you need after creating the instance
            return redirect('/food')
    else:
        form = FoodForm()

    return render(request, 'food_add.html', {'form': form})


def create_exercise_instance(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise_instance = ExerciseInstance.objects.create(
                user=request.user,
                exercise=form.cleaned_data['exercise'],
                times=form.cleaned_data['times'],
                date=form.cleaned_data['date'],
                duration=form.cleaned_data['duration'],
            )
            return redirect('/exercise/')  # Redirect to success page or another appropriate URL
    else:
        form = ExerciseForm()

    return render(request, 'exercise_add.html', {'form': form})

def food_instance_list(request):
    user_food_instance = FoodIntsance.objects.filter(user=request.user)
    return render(request, 'food.html', {'food_instances': user_food_instance})


def exercise_instance_list(request):
    user_exercise_instance = ExerciseInstance.objects.filter(user=request.user)
    return render(request, 'exercise.html', {'exercise_instances': user_exercise_instance})



def food_list(request):
    food_intsances = FoodIntsance.objects.all()

    # Calculate total calories
    total_calories = sum(food_intsance.calories for food_intsance in food_intsances)

    return render(request, 'food.html', {'food_instances': food_intsances, 'total_calories': total_calories})


def bmrview(request):
    # Get the logged-in user
    user = request.user

    # Calculate BMR
    bmr = calculate_bmr(user)

    # Use the calculated BMR as needed
    # ...

    return render(request, 'daily_burned.html', {'bmr': bmr})
