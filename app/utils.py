
from accounts.models import TrackerUser
# utils.py
def calculate_bmr(TrackerUser):
    weight = TrackerUser.weight  # Replace with the actual field name in your model
    height = TrackerUser.height  # Replace with the actual field name in your model
    age = TrackerUser.age  # Replace with the actual field name in your model

    if TrackerUser.gender == 'Male':
        # Male Equation
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif TrackerUser.gender == 'Female':
        # Female Equation
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    else:
        # Handle other gender options if needed
        bmr = 0

    return bmr