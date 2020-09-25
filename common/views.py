from django.urls import reverse_lazy
from django.views import generic
from .models import UserProfile


class EditUserProfile(generic.UpdateView):
    model = UserProfile
    fields = ['photo', 'age', ]
    template_name = 'profile-edit.html'
    success_url = reverse_lazy('p_library:account')
