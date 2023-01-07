from django.http import HttpResponse
from django.views.generic import TemplateView, UpdateView, ListView

from apps.models import User


class WithdrawView(UpdateView):
    template_name = 'apps/auth/withdraw.html'
    context_object_name = 'user'
    queryset = User.objects.get(id=1)
    model = User
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        user = request.user
        if request.POST.get('coin_exchange'):
            amount = int(request.POST.get('amount'))
            if amount < 50:
                return HttpResponse("Sorov miqdori 50 COIN dan kam bo'lmasligi shart!")

            if user.bonus > amount:
                user.balance = user.balance + (1000 * amount)
                user.save()
            else:
                return HttpResponse("Sizda COIN yetarli emas!")

        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user
