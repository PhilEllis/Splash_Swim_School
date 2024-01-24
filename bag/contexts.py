from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Course


def bag_contents(request):
    """
    Context processor for shopping bag contents.
    Gathers the items added to the shopping bag stored in the session.
    Calculates the total cost and the total number of items. 
    It builds a list of bag items with detailed info about each course.
    Returns a context dictionary that contains the bag items, total cost, total item count,
    and grand total which can be used in templates.
    """
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for course_id, quantity in bag.items():
        course = get_object_or_404(Course, pk=course_id)
        total += course.price * quantity  # Calculate total for each item
        product_count += quantity  # Update product count

        bag_items.append({
            'course_id': course_id,
            'name': course.name,
            'level': course.get_level_display(),
            'start_date': course.start_date,
            'location_name': course.location.name,
            'quantity': quantity,
            'product': course,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
