from django.db.models import F
from django.shortcuts import redirect
from django.views.generic import ListView

from apps.models import Order


class OperatorPageView(ListView):
    template_name = 'apps/operator/main_page.html'
    queryset = Order.objects.filter(status=Order.Status.NEW)
    context_object_name = 'orders'


class MyOrderPageView(ListView):
    template_name = 'apps/operator/my_order.html'
    queryset = Order.objects.all()
    context_object_name = 'orders'

    def post(self, request, *args, **kwargs):
        order_id = self.request.POST['order_id']
        Order.objects.filter(pk=order_id).update(operator=self.request.user, status=Order.Status.ACCEPTED)
        return redirect('my_order')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(operator=self.request.user.pk)
