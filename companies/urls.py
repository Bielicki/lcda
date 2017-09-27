from django.conf.urls import url

from companies import views

urlpatterns = [
    url(r'^$', views.CompanyListView.as_view(), name='company_list'),
    url(r'^datatable/$', views.CompaniesDataTableView.as_view(), name='company_list_datatable'),
    url(r'^create/$', views.CompanyCreateView.as_view(), name='company_create'),
    url(r'^update/(?P<pk>(\d)+)/$', views.CompanyUpdateView.as_view(), name='company_update'),
    url(r'^delete/(?P<pk>(\d)+)/$', views.CompanyDeleteView.as_view(), name='company_delete'),

]