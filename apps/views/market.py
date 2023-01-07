from django.views.generic import ListView

from apps.models import Product, Category


class MarketListView(ListView):
    template_name = 'apps/admin/market_page.html'
    model = Product
    paginate_by = 30
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        if category := self.request.GET.get('category'):
            return qs.filter(category__slug=category)
        return qs
