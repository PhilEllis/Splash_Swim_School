from django.shortcuts import render,redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Course  # Import Course from the products app

# Create your views here.
def view_bag(request):
    """  view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_course_to_bag(request, course_id):
    # Retrieve the course object using the course_id
    course = get_object_or_404(Course, pk=course_id)
    
    # Store the course in the session
    request.session['course'] = {
        'id': course.id,
        'name': course.name,
        'description': course.description,
        'price': course.price,
        'start_date': course.start_date,
        'end_date': course.end_date,
        'level': course.level,
        'location': course.location.name,  # Assuming you want to store the location name
        # Add other course details as needed
    }

    # Redirect to the shopping bag or checkout page
    return redirect('bag/bag.html')  # Update the URL name accordingly