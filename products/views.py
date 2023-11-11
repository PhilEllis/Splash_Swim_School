from django.shortcuts import render
from .models import Course
from locations.models import Location

# Create your views here.
def level1_courses(request):
    """ A view to display level 1 swim lesson courses """
    level1_courses = Course.objects.filter(level='Level 1')
    locations = Location.objects.all()  
    context = {
        'courses': level1_courses,
        'locations': locations,
    }
    return render(request, 'products/level1.html', context)

def level2_courses(request):
    """ A view to display level 2 swim lesson courses """
    level2_courses = Course.objects.filter(level='Level 2')
    locations = Location.objects.all()
    context = {
        'courses': level2_courses,
        'locations': locations,
    }
    return render(request, 'products/level2.html', context)


def level3_courses(request):
    """ A view to display level 3 swim lesson courses """
    level3_courses = Course.objects.filter(level='Level 3')
    locations = Location.objects.all()
    context = {
        'courses': level3_courses,
        'locations': locations,
    }
    return render(request, 'products/level3.html', context)


def level4_courses(request):
    """ A view to display level 4 swim lesson courses """
    level4_courses = Course.objects.filter(level='Level 4')
    locations = Location.objects.all()
    context = {
        'courses': level4_courses,
        'locations': locations,
    }
    return render(request, 'products/level4.html', context)