from django.conf.urls import url
from .views import ExcelUpload

urlpatterns = [
    url(r'^$', ExcelUpload.as_view(), name='excel'),
    ]