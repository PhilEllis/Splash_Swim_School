from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import UserProfile, GuardianProfile, ChildProfile
from .forms import UserProfileForm, GuardianProfileForm, ChildProfileForm

from checkout.models import Order


def profile(request):
    """ Display the user's profile. """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    guardian_profile, created = GuardianProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user_profile)
        guardian_form = GuardianProfileForm(request.POST, instance=guardian_profile)
        child_form = ChildProfileForm(request.POST)

        if user_form.is_valid() and guardian_form.is_valid():
            user_form.save()
            guardian_form.save()
            messages.success(request, 'Profile updated successfully')
            if child_form.is_valid():
                child = child_form.save(commit=False)
                child.guardian = guardian_profile
                child.save()
                messages.success(request, f'Child {child.name} added successfully')
                return redirect('profile')
        else:
            messages.error(request, 'There was an error with the form submission.')
    else:
        user_form = UserProfileForm(instance=user_profile)
        guardian_form = GuardianProfileForm(instance=guardian_profile)
        child_form = ChildProfileForm()

    orders = user_profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'user_form': user_form,
        'guardian_form': guardian_form,
        'child_form': child_form,
        'orders': orders,
        'on_profile_page': True,
        'children': ChildProfile.objects.filter(guardian=guardian_profile)
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
