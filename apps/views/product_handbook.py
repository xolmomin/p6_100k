from django.views.generic import ListView
from apps.models import Product, Category, Contact


class CategoryDetail(ListView):
    template_name = 'apps/category_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        slug = self.request.GET.get('category')
        qs = self.get_queryset()
        context['categories'] = Category.objects.all()
        context['products'] = qs
        # context['category_slug'] = Category.objects.filter(slug=slug).first()
        # context['products2'] = Product.objects.all()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if category := self.request.GET.get('category'):
            return qs.filter(category__slug=category)
        return qs


class ContactsView(ListView):
    template_name = 'apps/contacts.html'
    model = Contact