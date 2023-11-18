from django.shortcuts import render,redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Course

# Create your views here.
def view_bag(request):
    """  view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_course_to_bag(request):
    """ Add a swimming course to the shopping bag """
    course_id = request.POST.get('course_id')
    course = get_object_or_404(Course, pk=course_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # Check if the course is already in the bag
    if course_id in bag:
        messages.info(request, f'{course.name} is already in your bag.')
    else:
        bag.clear()  # Clear the bag to ensure only one course is present
        bag[course_id] = 1

    request.session['bag'] = bag
    return redirect(redirect_url)