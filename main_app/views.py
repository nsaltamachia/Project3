from django.shortcuts import render
# Import restaurant model
from .models import Restaurant

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

#about view
def about(request):
  return render(request, 'about.html')

# restaurants view
def restaurants_index(request):
  restaurants = Restaurant.objects.all()
  return render(request, 'restaurants/index.html', {
    'restaurants': restaurants
  })