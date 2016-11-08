from django.conf.urls import url
from tennis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
