from django.db.models import Q
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from common.mixins import LoginSuperuserRequiredMixin
from companies.models import Company
from .forms import CompanySearchForm


class CompanyListView(LoginSuperuserRequiredMixin, TemplateView):
    template_name = 'company_list_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = CompanySearchForm()
        return context


class CompaniesDataTableView(BaseDatatableView):
    raise_exception = True
    model = Company
    columns = ['client', 'name', 'code', 'years', 'urls']
    order_columns = ['client', 'name', 'code', 'years', 'urls']
    max_display_length = 20

    def render_column(self, row, column):
        if column == 'name':
            return row.name
        elif column == 'code':
            return row.code
        elif column == 'years':
            return list(set([year.year for year in row.years.all()]))
        # elif column == 'engagement_specialist':
        #     return row.engagement_specialist
        # elif column == 'contract_type':
        #     return row.contract_type.name
        # elif column == 'survey':
        #     return list(set([survay.name for survay in row.surveys.all()]))
        elif column == 'client':
            return row.client.name

        elif column == 'urls':
            return {
                'update_url': reverse('companies:company_update', args=[row.id]),
                'delete_url': reverse('companies:company_delete', args=[row.id])
            }
        else:
            return super(CompaniesDataTableView, self).render_column(row, column)

    def filter_queryset(self, qs):
        qset = Q()

        name = self.request.POST.get('name')
        if name:
            qset &= Q(name__icontains=name)

        code = self.request.POST.get('code')
        if code:
            qset &= Q(code__icontains=code)

        # email = self.request.POST.get('email')
        # if email:
        #     qset &= Q(engagement_specialist__icontains=email)
        #
        # survey = self.request.POST.get('survey')
        # if survey:
        #     qset &= Q(surveys__name__icontains=survey)

        client = self.request.POST.get('client')
        if client:
            qset &= Q(client__name__contains=client)

        # contract = self.request.POST.get('contract')
        # if contract:
        #     qset &= Q(contract_type__name__icontains=contract)

        return qs.filter(qset).distinct()


class CompanyCreateView(CreateView):
    raise_exception = True
    model = Company
    fields = '__all__'
    template_name = 'company_create_view.html'
    success_url = reverse_lazy('company:company_list')


class CompanyUpdateView(LoginSuperuserRequiredMixin, UpdateView):
    raise_exception = True
    model = Company
    fields = '__all__'
    template_name = 'company_update_view.html'
    success_url = reverse_lazy('companies:company_list')


class CompanyDeleteView(LoginSuperuserRequiredMixin, DeleteView):
    raise_exception = True
    model = Company
    template_name = 'company_delete_view.html'
    success_url = reverse_lazy('companies:company_list')
