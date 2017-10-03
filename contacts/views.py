from django.db.models import Q
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from common.mixins import LoginSuperuserRequiredMixin
from companies.models import ClientContact
from .forms import ContactSearchForm


class ContactListView(LoginSuperuserRequiredMixin, TemplateView):
    template_name = 'contact_list_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ContactSearchForm()
        return context


class ContactDataTableView(BaseDatatableView):
    raise_exception = True
    model = ClientContact
    columns = ['company', 'first_name', 'last_name', 'email', 'may_contact', 'location', 'urls']
    order_columns = ['company', 'first_name', 'last_name', 'email', 'may_contact', 'location', 'urls']
    max_display_length = 20

    def render_column(self, row, column):
        if column == 'first_name':
            return row.first_name
        elif column == 'last_name':
            return row.last_name
        elif column == 'email':
            return row.email
        elif column == 'may_contact':
            if row.may_contact:
                return 'Yes'
            else:
                return 'No'
        elif column == 'company':
            return row.company.name
        # elif column == 'report_access':
        #     return row.report_access
        # elif column == 'surveys':
        #     return list(set([survey.name for survey in row.surveys.all()]))
        elif column == 'location':
            return row.location
        elif column == 'urls':
            return {
                'update_url': reverse('contacts:contact_update', args=[row.id]),
                'delete_url': reverse('contacts:contact_delete', args=[row.id])
            }
        else:
            return super(ContactDataTableView, self).render_column(row, column)

    def filter_queryset(self, qs):
        qset = Q()

        name = self.request.POST.get('name')
        if name:
            qset &= Q(first_name__icontains=name)

        last_name = self.request.POST.get('surname')
        if last_name:
            qset &= Q(last_name__icontains=last_name)

        email = self.request.POST.get('email')
        if email:
            qset &= Q(email__icontains=email)

        company = self.request.POST.get('company')
        if company:
            qset &= Q(company__name__icontains=company)

        # survey = self.request.POST.get('survey')
        # if survey:
        #     qset &= Q(surveys__name__icontains=survey)

        location = self.request.POST.get('location')
        if location:
            qset &= Q(location__icontains=location)
        return qs.filter(qset).distinct()


class ContactCreateView(CreateView):
    raise_exception = True
    model = ClientContact
    fields = '__all__'
    template_name = 'contact_create_view.html'
    success_url = reverse_lazy('contacts:contact_list')


class ContactUpdateView(LoginSuperuserRequiredMixin, UpdateView):
    raise_exception = True
    model = ClientContact
    fields = '__all__'
    template_name = 'contact_update_view.html'
    success_url = reverse_lazy('contacts:contact_list')


class ContactDeleteView(LoginSuperuserRequiredMixin, DeleteView):
    raise_exception = True
    model = ClientContact
    template_name = 'contact_delete_view.html'
    success_url = reverse_lazy('contacts:contact_list')
