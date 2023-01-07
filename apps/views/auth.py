from django.views.generic import UpdateView

from apps.forms.authform import ProfileForm
from apps.models.users import User


class ProfileView(UpdateView):
    context_object_name = 'profile'
    form_class = ProfileForm
    model = User
    template_name = 'apps/auth/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
