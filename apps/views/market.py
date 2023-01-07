from django.views.generic import ListView

from apps.models import Product


class MarketListView(ListView):
    template_name = 'apps/market_page.html'
    model = Product
