from django.views.generic import ListView

from apps.models import Product, Category


class MarketListView(ListView):
    template_name = 'apps/market_page.html'
    model = Product
    paginate_by = 30
    context_object_name = 'products'

    def get_context_object_name(self, object_list):
        context = super().get_context_object_name(object_list)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        if category := self.request.GET.get('category'):
            return qs.filter(category__slug=category)
        return qs


