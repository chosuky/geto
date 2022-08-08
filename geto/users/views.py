from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import SignupForm

def main(request):
    if request.method == 'GET':
        return render(request, 'users/main.html')

    elif request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page. (로그인 성공시 post app으로 redirect)
                return HttpResponseRedirect(reverse('posts:index'))

            else:
                # Return an 'invalid login' error message. (로그인 실패시 다시 main 페이지로)
                return render(request, 'users/main.html')

def signup(request):
    if request.method == 'GET':
        form = SignupForm()

        return render(request, 'users/signup.html', {'form': form})

    elif request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page. (로그인 성공시 post app으로 redirect)
                return HttpResponseRedirect(reverse('posts:index'))

                # Return an 'invalid login' error message. (로그인 실패시 다시 main 페이지로)

        return render(request, 'users/main.html')
