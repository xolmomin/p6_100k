from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.views.generic import DetailView, FormView, ListView, TemplateView

from apps.forms.base import CreateCommentForm
from apps.models import Product, Comment, Stream, Category, Region, Contact


class MainPageView(ListView):
    template_name = 'apps/index.html'
    queryset = Category.objects.all()
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['products'] = Product.objects.all()[:6]
        return context


class ExploreProductsView(ListView):
    template_name = 'apps/explore.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        if category := self.request.GET.get('sort'):
            return qs.filter(category__slug=category)
        return qs


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


def completed(request, *args, **kwargs):
    stream = Stream.objects.get(id=id)
    stream.is_area = not stream.is_area
    stream.save()

    return JsonResponse({'status': 200})


class StreamPageListView(ListView):
    template_name = 'apps/admin/stream.html'
    model = Stream
    queryset = Stream.objects.all()
    context_object_name = 'streams'
    paginate_by = 9

    def post(self, request, *args, **kwargs):
        stream = Stream.objects.filter(id=int(request.POST['id'])).first()
        stream.is_area = not stream.is_area
        stream.save()
        return super().post(self, request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['url'] = get_current_site(self.request)
        return context


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
        context['category_slug'] = Category.objects.filter(slug=slug).first()
        context['products2'] = Product.objects.all()
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if category := self.request.GET.get('category'):
            return qs.filter(category__slug=category)
        return qs


class AdminProductDetailView(DetailView):
    template_name = 'apps/admin/product.html'
    queryset = Product.objects.all()
    slug_field = Product.pk


class AdminPageView(DetailView):
    template_name = 'apps/admin/main_page.html'

    def get_object(self, queryset=None):
        return self.request.user


class ContactsView(ListView):
    template_name = 'apps/contacts.html'
    model = Contact
