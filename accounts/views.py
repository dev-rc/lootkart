# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserForm, LoginForm




def signup_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

            return redirect('/')  # Replace with your desired success URL
    else:
        form = CustomUserForm()

    return render(request, 'accounts/signup/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Replace with your desired success URL
    else:
        form = LoginForm()

    return render(request, 'accounts/login/login.html', {'form': form})


# def view_profile(request):
#     profile = Profile.objects.get(user=request.user)
#     return render(request, 'profile/view_profile.html', {'profile': profile})

# def edit_profile(request):
#     profile = Profile.objects.get(user=request.user)
    
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('view_profile')
#     else:
#         form = ProfileForm(instance=profile)

#     return render(request, 'profile/edit_profile.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to your desired page after logout (replace 'home' with the URL name of your choice)