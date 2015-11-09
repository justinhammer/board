from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from main.models import CustomUser, Thread, Post
from main.forms import CustomUserCreationForm, UserLogin, UserEditForm
# Create your views here.


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'user_detail_view.html'
    slug_field = 'username'


class UserListView(ListView):
    model = CustomUser
    template_name = 'user_list_view.html'
    slug_field = 'username'


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'thread_detail_view.html'
    slug_field = 'title'


class ThreadListView(ListView):
    model = Thread
    template_name = 'thread_list_view.html'
    slug_field = 'title'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail_view.html'
    slug_field = 'title'
    #How do I order by something when I'm using a class based view


class PostListView(ListView):
    queryset = Post.objects.all().order_by('-votes')
    model = Post
    template_name = 'post_list_view.html'
    slug_field = 'title'


def user_search(request):

    context = {}

    context['request'] = request

    username = request.GET.get('username', None)

    if username != None:
        usernames = CustomUser.objects.filter(username__icontains=username)

        context['usernames'] = usernames

    return render_to_response('user_search_view.html', context, context_instance=RequestContext(request))


def signup(request):

    context = {}

    form = CustomUserCreationForm()

    context['form'] = form

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            try:
                new_user = CustomUser.objects.create_user(email=email, password=password)
                new_user.username = username
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.save()
                print new_user
                auth_user = authenticate(email=email, password=password)
                print auth_user
                login(request, auth_user)
                return HttpResponseRedirect('/user_detail_view/%s' % new_user.pk)
            except IntegrityError, e:
                context['valid'] = "A User With That Name Already Exists"

        else:
            context['valid'] = form.errors

    return render_to_response('signup.html', context, context_instance=RequestContext(request))


def login_view(request):

    context = {}

    context['form'] = UserLogin()

    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            auth_user = authenticate(email=email, password=password)

            if auth_user is not None:
                login(request, auth_user)

                return HttpResponseRedirect('/user_detail_view/%s' % auth_user.pk)
            else:
                context['valid'] = "Invalid User"

        else:
            context['valid'] = "Please enter a User Name"

    return render_to_response('login.html', context, context_instance=RequestContext(request))


def logout_view(request):

    logout(request)

    return HttpResponseRedirect('/login/')


def user_edit(request, pk):
    if request.user != CustomUser.objects.get(pk=pk):
        return HttpResponseRedirect('/invalid_user/')

    context = {}

    user = CustomUser.objects.get(pk=pk)

    form = UserEditForm(request.POST or None, request.FILES or None, instance=user)

    context['user'] = user
    context['form'] = form
    context['pk'] = pk

    if request.method == 'POST' and form.is_valid():
        form.save()
        print 'valid'
        return HttpResponseRedirect('/user_detail_view/%s' % (user.pk))
    else:
        print form.errors

    return render_to_response('user_edit.html', context, context_instance=RequestContext(request))


def invalid_user(request):

    return render_to_response('invalid_user.html')


def vote(request, pk):

    vote_type = request.GET.get('vote_type', None)

    user = CustomUser.objects.get(pk=request.user.pk)

    post = Post.objects.get(pk=pk)

    print "hit 1"

    if vote_type == 'up':
        if user in post.downvotes.all():
            post.downvotes.remove(user)

        post.upvotes.add(user)

        print post.upvotes.all().count()

        print "hit up"

    if vote_type == 'down':
        if user in post.upvotes.all():
            post.upvotes.remove(user)

        post.downvotes.add(user)

        print post.downvotes.all().count()

        print "hit down"

    return HttpResponseRedirect('/post_list/')
        # 'UpVote: %s, DownVotes: %s' % (post.upvotes.all().count(), post.downvotes.all().count()))