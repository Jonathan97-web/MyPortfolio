from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile
from .forms import UpdateProfileForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.dispatch import receiver


# Profile for the logged in user
@login_required
def profile(request, id):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect(to='/profile/1')
            # next = request.POST.get('next', '/profile/1')
            # return HttpResponseRedirect(next)
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

# View profile


def view_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile_detail.html', {"user": user})


# Create Profile When New User Signs Up
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
