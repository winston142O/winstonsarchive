from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, get_object_or_404

def register(request):
    """ The view responsible for user registration. """
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit= True)
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Tu cuenta se ha creado correctamente, ahora puedes iniciar sesión')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_profile(request, id):
    """ The view responsible for viewing another user's profile. """
    
    user = get_object_or_404(User, id=id)
    return render(request, 'users/user_profile.html', {'profile_user': user, 'logged_user': request.user})

@login_required
def profile(request):
    """ View and update personal user profile. """
    
    # Update user and profile information
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) 
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            messages.success(request, f'Your profile has been succesfully updated!')
            return redirect('profile')

    # Display the user's information
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

def about_me(request):
    """ Winston's about me page. """
    
    return render(request, 'about_me.html', {'winston_user': User.objects.get(username='winston1420')})

@login_required
def confirmLogout(request):
    
    return render(request, 'users/confirm-logout.html')

#TODO: PASSOWRD RESET VIEWS