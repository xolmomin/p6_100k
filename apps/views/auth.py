from django.views.generic import UpdateView, TemplateView

from apps.forms.authform import ProfileForm
from apps.models import User


class WithdrawView(TemplateView):
    template_name = 'apps/auth/withdraw.html'


class ProfileView(UpdateView):
    context_object_name = 'profile'
    form_class = ProfileForm
    model = User
    template_name = 'apps/auth/profile.html'

    def get_object(self, queryset=None):
        return self.request.user
