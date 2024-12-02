# # user/meal_utils.py
# import re
# from collections import defaultdict
# from .models import GenAI

# def categorize_and_calculate_meals_from_db():
#     categorized_meals = defaultdict(list)
#     total = {'calories': 0, 'protein': 0, 'carbs': 0}
    
#     # Get all wGenAI instances
#     genai_data = GenAI.objects.all()

#     for genai in genai_data:
#         meal_data = genai.data  # Assuming 'data' contains meal details as a string

#         # Split the meal data based on lines or known meal types (e.g., Breakfast, Lunch, etc.)
#         meal_lines = meal_data.split('\n')

#         meal_type = None
#         for line in meal_lines:
#             # Identify the meal type based on the start of the line (e.g., Breakfast, Lunch, etc.)
#             if line.startswith('Breakfast'|'breakfast'):
#                 meal_type = 'breakfast'
#             elif line.startswith('Lunch'|'lunch'):
#                 meal_type = 'lunch'
#             elif line.startswith('Snack 1'|'snack1'):
#                 meal_type = 'snack1'
#             elif line.startswith('Snack 2'|'snack2'):
#                 meal_type = 'snack2'
#             elif line.startswith('Dinner'|'dinner'):
#                 meal_type = 'dinner'

#             # If a valid meal type is found, process the meal details
#             if meal_type:
#                 # Example: 'Scrambled eggs with whole-wheat toast and avocado (400 calories, 30g protein, 40g carbs)'
#                 meal_details = re.match(r"([A-Za-z ]+)\s\((\d+)\scalories,\s(\d+)g\sprotein,\s(\d+)g\scarbs\)", line)
#                 if meal_details:
#                     name = meal_details.group(1)
#                     calories = int(meal_details.group(2))
#                     protein = int(meal_details.group(3))
#                     carbs = int(meal_details.group(4))

#                     categorized_meals[meal_type].append({
#                         'meal_type': meal_type.capitalize(),
#                         'name': name,
#                         'calories': calories,
#                         'protein': protein,
#                         'carbs': carbs
#                     })

#                     # Accumulate totals
#                     total['calories'] += calories
#                     total['protein'] += protein
#                     total['carbs'] += carbs

#     # Format the response
#     return {
#         'categorized_meals': categorized_meals,
#         'total': total
#     }
