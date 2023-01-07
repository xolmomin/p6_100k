from django.views.generic import ListView


class MarketListView(ListView):
    template_name = 'apps/market_page.html'
