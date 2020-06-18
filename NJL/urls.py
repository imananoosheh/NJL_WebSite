
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^ckeditor/upload/', include('ckeditor_uploader.urls')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'jet/', include('jet.urls')),
    url(r'admin/', admin.site.urls),
    url(r'^', include('Landing.urls')),
    url(r'^news/',include('newsApp.urls', namespace='news')),
    url(r'^aboutUs/',include('aboutUs.urls')),
    url(r'^adultcourses/',include('adults.urls')),
    url(r'^contactUs/',include('contactUs.urls')),
    url(r'^onlinelearning/',include('E_Learning.urls')),
    url(r'^EPT/',include('EPT.urls')),
    url(r'^IELTS/',include('IELTS.urls')),
    url(r'^TOEFL/',include('TOEFL.urls')),
    url(r'^TTC/',include('TTC.urls')),
    url(r'^kidscourses/',include('kids.urls')),
    url(r'^teenagerscourses/',include('teens.urls')),
    url(r'^resources/',include('references.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)