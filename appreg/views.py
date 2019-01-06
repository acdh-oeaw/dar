import django_tables2 as tables
from django.conf import settings
from django_tables2.config import RequestConfig
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

from browsing.browsing_utils import GenericListView, BaseCreateView, BaseUpdateView

from . filters import *
from . forms import *
from . tables import *
from . models import WebApp


class WebAppListView(GenericListView):
    model = WebApp
    filter_class = WebAppListFilter
    formhelper_class = WebAppFilterFormHelper
    table_class = WebAppTable
    init_columns = [
        'id',
        'title',
        'author',
        'git_url',
    ]


class WebAppDetailView(DetailView):
    model = WebApp
    template_name = 'appreg/webapp_detail.html'


class WebAppCreate(BaseCreateView):

    model = WebApp
    form_class = WebAppForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WebAppCreate, self).dispatch(*args, **kwargs)


class WebAppUpdate(BaseUpdateView):

    model = WebApp
    form_class = WebAppForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WebAppUpdate, self).dispatch(*args, **kwargs)


class WebAppDelete(DeleteView):
    model = WebApp
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('appreg:webapp_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WebAppDelete, self).dispatch(*args, **kwargs)
