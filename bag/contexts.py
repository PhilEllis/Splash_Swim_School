from decimal import Decimal
from django.conf import settings

def bag_contents(request):
    
    course = request.session.get('course')
    
    context = {
        'course': course,  # Pass the course object
    }

    return context