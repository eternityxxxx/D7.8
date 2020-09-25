from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from allauth.socialaccount.models import SocialAccount

from .models import Book
from common.models import UserProfile


class BookListPage(ListView):
    model = Book
    template_name = 'books_list.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('common:login'))
        return super(BookListPage, self).get(self, request, *args, **kwargs)


class BookPage(DetailView):
    model = Book
    template_name = 'books_detail.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('common:login'))
        return super(BookPage, self).get(self, request, *args, **kwargs)


def user_account(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse_lazy('common:login'))

    try:
        profile = request.user.profile_user
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    try:
        social_profile = SocialAccount.objects.get(provider='github', user=request.user)
        if social_profile:
            context = {
                "username": request.user.username,
                "firstname": request.user.first_name,
                "lastname": request.user.last_name,
                "github_url": SocialAccount.objects.get(provider='github', user=request.user).extra_data['html_url'],
            }

            return render(request, 'user_account.html', context)
    except SocialAccount.DoesNotExist:
        pass

    context = {
        "profile": profile,
        "username": request.user.username,
        "firstname": request.user.first_name,
        "lastname": request.user.last_name,
        "age": profile.age,
        "photo": profile.photo,
    }

    return render(request, 'user_account.html', context)
