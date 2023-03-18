from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import set_language

from news.views import HomePageView, ContactPageView, NewsCreateView, NewsSearchView

urlpatterns = [
    path('auth/', include('accounts.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

]

# Asosiy ilova uchun tilni o'zgartirishni yordam beradigan url
urlpatterns += [
    path('set_language/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('', HomePageView, name='home'),
    path('news/', include('news.urls')),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('create/', NewsCreateView.as_view(), name='create_news'),
    path('search/', NewsSearchView.as_view(), name='search_news'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
