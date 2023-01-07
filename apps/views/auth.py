from django.http import HttpResponse
from django.views.generic import UpdateView

from apps.forms import PaymentForm
from apps.models import User


class WithdrawView(UpdateView):
    template_name = 'apps/auth/withdraw.html'
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
        if request.POST.get('card_withdraw'):
            form = PaymentForm(request.POST)
            form.is_valid()

        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user
