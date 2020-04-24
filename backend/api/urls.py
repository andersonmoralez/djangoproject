from django.conf.urls import url
from .views import RegisterListView
from .views import RegisterView

urlpatterns = [
    url(r'^records/?$', RegisterListView.as_view(), name='records'),
    url(r'^record/(?P<pk>[0-9]+)/?$', RegisterView.as_view(), name='record'),
]