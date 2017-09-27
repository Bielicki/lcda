from django.conf.urls import url

from contacts import views

urlpatterns = [
    url(r'^$', views.ContactListView.as_view(), name='contact_list'),
    url(r'^datatable/$', views.ContactDataTableView.as_view(), name='contact_list_datatable'),
    url(r'^create/$', views.ContactCreateView.as_view(), name='contact_create'),
    url(r'^update/(?P<pk>(\d)+)/$', views.ContactUpdateView.as_view(), name='contact_update'),
    url(r'^delete/(?P<pk>(\d)+)/$', views.ContactDeleteView.as_view(), name='contact_delete'),

]