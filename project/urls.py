from django.contrib import admin
from django.urls import path,include
admin.site.site_title = "E-Market"
admin.site.site_header = 'E-Market Web'
admin.site.index_title = 'E-Market'
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls'))
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

