from django.views.generic import FormView, DetailView, ListView

from apps.forms import CreateCommentForm
from apps.models import Product, Comment, Region, Category


class ProductDetailView(FormView, DetailView):
    template_name = 'apps/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'
    form_class = CreateCommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['comment'] = Comment.objects.all()
        context['regions'] = Region.objects.all()
        return context


class CategoryDetail(ListView):
    template_name = 'apps/category_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        qs = self.get_queryset()
        context['categories'] = Category.objects.all()
        context['products'] = qs
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if category := self.request.GET.get('category'):
            return qs.filter(category__slug=category)
        return qs
