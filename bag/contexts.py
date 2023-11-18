from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Course

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for course_id, quantity in bag.items():
        product = get_object_or_404(Course, pk=course_id)
        total = Decimal('0.00')

        if bag:
            # Assuming the bag contains only one item with its course_id and quantity
            course_id, quantity = list(bag.items())[0]

            product = get_object_or_404(Course, pk=course_id)
            total = product.price * quantity  # Calculate total

            bag_items.append({
                'course_id': course_id,
                'quantity': quantity,
                'product': product,
            })
    
        grand_total = total

        context = {
            'bag_items': bag_items,
            'total': total,
            'product_count': product_count,
            'grand_total': grand_total,
        }

        return context