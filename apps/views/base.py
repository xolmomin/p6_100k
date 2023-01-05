from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView

from apps.forms.base import CreateCommentForm
from apps.models.base import Product, Comment

from django.views.generic import TemplateView


class MainPageView(TemplateView):
    queryset = Product.objects.all()
    template_name = 'apps/main_page.html'


class ProductDetailView(FormView, DetailView):
    template_name = 'apps/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'post'
    form_class = CreateCommentForm

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)

    def product(self, request, *args, **kwargs):  # TODO javlon product name wrong
        slug = kwargs.get('slug')
        if 'comment' in request.POST:
            product = get_object_or_404(Product, slug=slug)
            data = {
                'product': product,
                'text': request.POST.get('message'),
            }
            comment = Comment.objects.create(**data)
            comment.save()
        return redirect('post_form_detail', slug)
