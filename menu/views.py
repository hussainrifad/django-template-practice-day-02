from django.shortcuts import render
from .static.data.meals import meals

# Create your views here.
def menu(request):
    return render(request, 'menu.html', {'meals' : meals})