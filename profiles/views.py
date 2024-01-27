from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, GuardianProfile, ChildProfile
from .forms import UserProfileForm, GuardianProfileForm, ChildProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """
    Display and manage the user's profile page.
    Allows users to update their own profile and guardian information,
    add child profiles, and view their order history.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    guardian_profile, created = GuardianProfile.objects.get_or_create(
        user=request.user
    )
    guardian_form = GuardianProfileForm(instance=guardian_profile)
    child_form = ChildProfileForm()

    if request.method == 'POST':
        if 'update_user' in request.POST:
            user_form = UserProfileForm(request.POST, instance=user_profile)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Profile updated successfully')
            else:
                messages.error(
                    request,
                    'An error has occurred while updating your profile. '
                    'Please check the form.'
                )

        if 'update_guardian' in request.POST:
            guardian_form = GuardianProfileForm(
                request.POST, instance=guardian_profile
            )
            if guardian_form.is_valid():
                guardian_form.save()
                messages.success(
                    request, 'Guardian profile updated successfully'
                )
            else:
                messages.error(
                    request,
                    'An error has occurred while updating the '
                    'guardian profile. Please check the form.'
                )

        if 'add_child' in request.POST:
            child_form = ChildProfileForm(request.POST)
            if child_form.is_valid():
                child = child_form.save(commit=False)
                child.guardian = guardian_profile
                child.save()
                messages.success(
                    request,
                    f'Child profile for {child.name} added successfully'
                )
                return redirect('profile')
            else:
                messages.error(
                    request,
                    'An error has occurred while adding a child profile. '
                    'Please check the form.'
                )

    children = ChildProfile.objects.filter(guardian=guardian_profile)

    context = {
        'user_form': user_form,
        'guardian_form': guardian_form,
        'child_form': child_form,
        'children': children,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def order_history(request, order_number):
    """
    View an individual order's history.
    Only accessible by the user who made the order.
    """
    order = get_object_or_404(
        Order,
        order_number=order_number,
        user_profile=request.user.userprofile
    )

    messages.info(
        request,
        (f'This is a past confirmation for order number '
         f'{order_number}.')
    )

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def delete_guardian(request):
    """
    Delete the guardian profile associated with the current user.
    """
    guardian_profile = GuardianProfile.objects.get(user=request.user)
    guardian_profile.delete()
    messages.success(request, "Guardian profile deleted successfully.")
    return redirect('profile')


@login_required
def update_child_profile(request, child_id):
    """
    Update the profile of a child.
    This view is protected and can only be accessed by the user who is
    the guardian of the child.
    """
    child = get_object_or_404(ChildProfile, id=child_id)
    guardian_profile = child.guardian

    # Check if the logged-in user is the guardian of the child
    if guardian_profile.user != request.user:
        messages.error(
            request, "You are not authorised to update this profile."
        )
        return redirect('login')

    if request.method == 'POST':
        form = ChildProfileForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Child profile for {child.name} updated successfully'
            )
            return redirect('profile')
    else:
        form = ChildProfileForm(instance=child)

    context = {
        'form': form,
        'child': child,
        'guardian': guardian_profile
    }
    return render(request, 'profiles/update_child_profile.html', context)


@login_required
def delete_child_profile(request, child_id):
    """
    Delete a child's profile.
    This view deletes the profile of a child, identified by child_id,
    associated with the logged-in user's guardian profile.
    """
    child = get_object_or_404(ChildProfile, id=child_id)
    guardian_profile = child.guardian

    if guardian_profile.user != request.user:
        messages.error(
            request,
            "You are not authorised to delete this profile."
        )
        return redirect('login')

    if request.method == 'POST':
        child.delete()
        messages.success(request, 'Child profile deleted successfully.')
        return redirect('profile')

    return redirect('profile')
