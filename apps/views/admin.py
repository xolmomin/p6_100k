from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView

from apps.forms.products import CreateStreamForm
from apps.models import Product, Category, Contact, Stream


class MarketListView(ListView, CreateView, FormView):
    template_name = 'apps/admin/market_page.html'
    paginate_by = 15
    model = Stream
    object = Stream
    form_class = CreateStreamForm
    success_url = reverse_lazy('market')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.order_by('id')

        search_input = self.request.GET.get('search') or ''
        context['search_input'] = search_input
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        search_input = self.request.GET.get('search') or ''
        if search_input:
            return qs.filter(title__icontains=search_input)

        if self.request.GET.get('category') in ('new', 'top'):
            return qs.order_by('-created_at')
        elif category := self.request.GET.get('category'):
            return qs.filter(category__slug=category)
        return qs


class AdminProductDetailView(DetailView):
    template_name = 'apps/admin/product.html'
    queryset = Product.objects.all()
    slug_field = 'pk'


class AdminPageView(DetailView):
    template_name = 'apps/admin/main_page.html'

    def get_object(self, queryset=None):
        return self.request.user


class ContactsView(ListView):
    template_name = 'apps/contacts.html'
    model = Contact


class AdminStatisticsPage(TemplateView):
    template_name = 'apps/admin/statistics_page.html'
