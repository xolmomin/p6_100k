from django.shortcuts import redirect
from django.views.generic import ListView

from apps.models import Order


class OperatorPageView(ListView):
    template_name = 'apps/operator/main_page.html'
    queryset = Order.objects.filter(status=Order.Status.YANGI)
    context_object_name = 'orders'


class MyOrderPageView(ListView):
    template_name = 'apps/operator/my_order.html'
    model = Order

    def post(self, request, *args, **kwargs):
        user = request.POST['user']
        stream = request.POST['stream']
        return redirect('my_order')
