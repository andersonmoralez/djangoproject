from django.conf.urls import url
from .views import RegisterListView, RegisterView, render_registers

"""
because of file versioning
you must include "/v1" in the browser
to access the URL
"""

urlpatterns = [
    url(r'^records/?$', RegisterListView.as_view(), name='records'),
    url(r'^record/(?P<pk>[0-9]+)/?$', RegisterView.as_view(), name='record'),
    url(r'^ ?$', render_registers, name='template'),
]