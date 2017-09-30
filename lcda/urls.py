from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include
from lcda import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('users.urls', namespace='users')),
    url(r'^load_excel/', include('excel_upload.urls', namespace='excel_upload')),
    url(r'^companies/', include('companies.urls', namespace='companies')),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
    url(r'^files/(?P<path>.*)', views.FileView.as_view(), name='file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

