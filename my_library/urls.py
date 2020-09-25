from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls', namespace='p_library')),
    path('', include('common.urls', namespace='common')),
    path('accounts/', include('allauth.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
