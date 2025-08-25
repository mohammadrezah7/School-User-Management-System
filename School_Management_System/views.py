from django.shortcuts import render
from django.shortcuts import get_object_or_404

def main_page(request):
    return render(request, 'shared/homepage.html')