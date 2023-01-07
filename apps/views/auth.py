from django.views.generic import TemplateView


class WithdrawView(TemplateView):
    template_name = 'apps/auth/withdraw.html'
