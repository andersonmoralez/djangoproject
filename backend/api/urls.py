from django.conf.urls import url
from .views import RegisterListView, RegisterView, token_request

urlpatterns = [
    url(r'^records/?$', RegisterListView.as_view(), name='records'),
    url(r'^record/(?P<pk>[0-9]+)/?$', RegisterView.as_view(), name='record'),
    url(r'^token/?$', token_request, name='token'),    
]