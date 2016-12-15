from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from twitter_app.forms import AuthenticateForm, UserCreateForm, TwitterCloneModelForm
from twitter_app.models import TwitterCloneModel

def index(request, auth_form=None, user_form=None):
    # User is logged in
    if request.user.is_authenticated():
        twitter_form = TwitterCloneModelForm()
        user = request.user
       	twitter_self = TwitterCloneModel.objects.filter(user=user.id)
        twitters_buddies = TwitterCloneModel.objects.filter(user__userprofile__in=user.profile.follows.all)
        twitters = twitters_self | twitters_buddies
 
        return render(request,
                      'buddies.html',
                      {'twitter_form': twitter_form, 'user': user,
                       'twitters': twitters,
                       'next_url': '/', })
    else:
        # User is not logged in
        auth_form = auth_form or AuthenticateForm()
        user_form = user_form or UserCreateForm()
 
        return render(request,
                      'home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Success
            return redirect('/')
        else:
            # Failure
            return index(request, auth_form=form)
    return redirect('/')
 
 
def logout_view(request):
    logout(request)
    return redirect('/')

def signup(request):
    user_form = UserCreateForm(data=request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.clean_password2()
            user_form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            login(request, user)
            return redirect('/')
        else:
            return index(request, user_form=user_form)
    return redirect('/')

@login_required
def submit(request):
    if request.method == "POST":
        twitter_form = TwitterCloneModelForm(data=request.POST)
        next_url = request.POST.get("next_url", "/")
        if twitter_form.is_valid():
            twitter = twitter_form.save(commit=False)
            twitter.user = request.user
            twitter.save()
            return redirect(next_url)
        else:
            return public(request, twitter_form)
    return redirect('/')

@login_required
def public(request, twitter_form=None):
    twitter_form = twitter_form or TwitterCloneModelForm()
    twitters = TwitterCloneModel.objects.reverse()[:10]
    return render(request,
                  'public.html',
                  {'twitter_form': twitter_form, 'next_url': '/twitters',
                   'twitters': twitters, 'username': request.user.username})