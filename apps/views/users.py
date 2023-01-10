from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView

from apps.forms import ProfileModelForm, FavoriteModelForm
from apps.models import User


class ProfileView(UpdateView):
    context_object_name = 'profile'
    form_class = ProfileModelForm
    queryset = User.objects.all()
    redirect_authenticated_user = True
    template_name = 'apps/auth/profile.html'
    success_url = reverse_lazy('main_page_view')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class FavoriteFormView(LoginRequiredMixin, FormView):
    template_name = 'apps/favorite.html'
    form_class = FavoriteModelForm
