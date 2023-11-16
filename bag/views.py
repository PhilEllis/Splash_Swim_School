from django.shortcuts import render,redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Course

# Create your views here.
def view_bag(request):
    """  view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_course_to_bag(request, course_id):
    """ Add a swimming course to the shopping bag """
    course_id = request.POST.get('course_id')
    course = get_object_or_404(Course, pk=course_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if course_id in bag:
        bag[course_id]['quantity'] += 1
    else:
        bag[course_id] = {
            'description': course.description,
            'name': course.name,
            #'price': course.price,
            #'start_date': course.start_date,
            #'end_date': course.end_date,
            'location': course.location.name,
            'quantity': 1,
        }

    request.session['bag'] = bag
    print(request.session['bag'])
    print(course_id)
    return redirect(redirect_url)