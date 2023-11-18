from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Course

def bag_contents(request):
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
            'product': course,  # Use course directly
        })
    
    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context