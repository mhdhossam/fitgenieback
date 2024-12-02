from django.core.mail import send_mail
import random
from django.conf import settings
from graduation.settings.base import *
from.models import CustomUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str,smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from celery import shared_task

@shared_task
def  send_otp_via_email(email):
    subject='Your account verification email'
    otp=random.randint(1000,9999)
    message=f"Dear User,\n\nPlease verify your account by entering the following OTP {otp}"
    email_from= EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj=CustomUser.objects.get(email=email)
    user_obj.otp=otp
    user_obj.save()
    
@shared_task
def send_welcome_email(email):
    subject='welcome to fit genie'
    message=f"Dear User,thanks for signing in our web"
    email_from= EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj=CustomUser.objects.get(email=email)
    user_obj.save()

# from .models import GenAI

# def categorize_and_calculate_meals_from_db():
#     """
#     Retrieve meal data from the database, categorize it into Breakfast, Lunch, 
#     Snack 1, Snack 2, and Dinner, and calculate total calories, protein, and carbs.
    
#     Returns:
#         dict: A dictionary with categorized meals and total nutritional information.
#     """
#     # Query all meals from the database
#     meal_data = GenAI.objects.all()

#     # Initialize categories for meals
#     categorized_meals = {
#         'breakfast': [],
#         'lunch': [],
#         'snack1': [],
#         'snack2': [],
#         'dinner': [],
#         'total': {'calories': 0, 'protein': 0, 'carbs': 0}
#     }

#     # Iterate through each meal and categorize it
#     for meal in meal_data:
#         meal_type = meal.meal_type.lower()
        
#         if meal_type in categorized_meals:
#             categorized_meals[meal_type].append({
#                 'meal_type': meal.meal_type,
#                 'name': meal.name,
#                 'calories': meal.calories,
#                 'protein': meal.protein,
#                 'carbs': meal.carbs
#             })
            
#             # Accumulate totals for calories, protein, and carbs
#             categorized_meals['total']['calories'] += meal.calories
#             categorized_meals['total']['protein'] += meal.protein
#             categorized_meals['total']['carbs'] += meal.carbs

#     return categorized_meals

# # Example usage:
# categorized_meals = categorize_and_calculate_meals_from_db()

# # Print the result
# print(categorized_meals)
