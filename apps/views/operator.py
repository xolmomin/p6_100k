from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from apps.forms import OrderEditStatus
from apps.models import Order


class OperatorPageView(ListView):
    template_name = 'apps/operator/main_page.html'
    queryset = Order.objects.filter(status=Order.Status.NEW)
    context_object_name = 'orders'

    def post(self, request, *args, **kwargs):
        order_id = self.request.POST['order_id']
        Order.objects.filter(pk=order_id).update(operator=self.request.user, status=Order.Status.ACCEPTED)
        return redirect('operator')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(operator=self.request.user.pk)


class MyOrderPageView(ListView, FormView):
    template_name = 'apps/operator/my_order.html'
    queryset = Order.objects.all()
    context_object_name = 'orders'
    form_class = OrderEditStatus
    success_url = reverse_lazy('my_order')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
