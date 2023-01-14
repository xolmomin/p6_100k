from json import loads

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView, ListView, TemplateView

from apps.forms import ProfileModelForm, FavoriteModelForm
from apps.models import User, District, Region
from apps.utils import validate_phone
from root import settings
from root.settings import FAKE_VERIFICATION


class ProfileLoginView(TemplateView):
    template_name = 'apps/auth/login.html'

    def post(self, request, *args, **kwargs):
        data: dict = request.POST
        phone: str = data.get('phone')
        code: str = data.get('password')
        validate = validate_phone(phone, code, FAKE_VERIFICATION)
        if validate.get('success'):
            if user := validate.get('user'):
                login(self.request, user)
            else:
                return self.render_to_response(validate)
        else:
            return self.render_to_response(validate)
        return redirect('admin_page')


class ProfileView(LoginRequiredMixin, UpdateView):
    context_object_name = 'profile'
    form_class = ProfileModelForm
    queryset = User.objects.all()
    redirect_authenticated_user = True
    template_name = 'apps/auth/profile.html'
    success_url = reverse_lazy('main_page_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bot_user'] = settings.BOT_USER
        context['regions'] = Region.objects.all().order_by('name')
        return context

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FavoriteFormView(LoginRequiredMixin, FormView):
    template_name = 'apps/favorite.html'
    form_class = FavoriteModelForm


class DistrictsView(ListView):
    def post(self, request, *args, **kwargs):
        data = loads(request.body)
        if region_id := data.get('region'):
            districts = list(District.objects.filter(region__id=region_id).values_list('name', flat=True))
            return JsonResponse(districts, safe=False)
        return JsonResponse({'success': False, 'message': 'region id not found'}, safe=False)
