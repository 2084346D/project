from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from tennis import views

urlpatterns = [
    # to show content from simple view
    url(r'^$', views.index, name='index'),
    # map any urls starting with tennis/
    # to be handled with the tennis application
    url(r'^tennis/', include('tennis.urls')),
    url(r'^admin/', admin.site.urls),
]
