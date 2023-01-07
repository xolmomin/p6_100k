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
        # coin exchange
        if request.POST.get('coin_exchange'):
            amount = int(request.POST.get('amount'))
            if amount < 50:
                return HttpResponse("Sorov miqdori 50 COIN dan kam bo'lmasligi shart!")
            if user.bonus > amount:
                user.balance = user.balance + (1000 * amount)
                user.save()
            else:
                return HttpResponse("Sizda COIN yetarli emas!")

            # withdraw to card
        if request.POST.get('card_withdraw'):
            amount = int(request.POST.get('amount'))
            if amount > 50000:
                form = PaymentForm(request.POST)
                form.instance.user = user
                if form.is_valid() and user.balance > amount:
                    form.save()
                    user.balance = user.balance - amount
                    user.save()
                else:
                    return HttpResponse("Sizda mablag' yetarli emas!")
            else:
                return HttpResponse("Sorov miqdori 50 000 so'mdan kam bo'lmasligi shart!")
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user
