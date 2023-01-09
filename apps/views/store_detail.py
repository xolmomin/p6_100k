from django.views.generic import DetailView

from apps.models import Store


class StoreDetailView(DetailView):
    template_name = 'apps/store_detail.html'
    model = Store
    context_object_name = 'store'

