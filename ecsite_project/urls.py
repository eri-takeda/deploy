from django.contrib import admin
from django.urls import path, include
from . import settings
from allauth import urls as allauth_urls
from django.conf.urls.static import static

# from django.contrib.staticfiles.urls import static
from django.conf.urls.static import static
from allauth.socialaccount.providers.google.urls import urlpatterns as google_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth_accounts/', include('allauth.socialaccount.providers.google.urls')),
    path('', include('accounts.urls')),
    path('stores/',include('stores.urls'), name='stores'),
    path('oauth_accounts/', include(allauth_urls)),
    path('boards/', include('boards.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    