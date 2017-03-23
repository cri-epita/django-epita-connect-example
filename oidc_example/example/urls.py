from django.conf.urls import url

from .views import home, logged

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^logged/$', logged, name='logged'),
]
