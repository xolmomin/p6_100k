from random import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, UpdateView, ListView

from apps.forms import ProfileModelForm, FavoriteModelForm
from apps.models import User, Contact, Region, District


class LogInView(LoginView):
    template_name = 'apps/auth/login.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    context_object_name = 'profile'
    form_class = ProfileModelForm
    queryset = User.objects.all()
    redirect_authenticated_user = True
    template_name = 'apps/auth/profile.html'
    success_url = reverse_lazy('main_page_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regions'] = Region.objects.all()
        context['districts'] = District.objects.all()
        return context

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        print()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FavoriteFormView(LoginRequiredMixin, FormView):
    template_name = 'apps/favorite.html'
    form_class = FavoriteModelForm


def SendSms(request):
    code = int(random() * 10 ** 5)
    print(code)
    return HttpResponseRedirect(reverse('login'))
