from django.conf.urls import url
from .views import get_bugs, bug_detail, create_or_edit_bug

urlpatterns = [
    url(r'^$', get_bugs, name='get_bugs'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^new/$', create_or_edit_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_bug, name='edit_bug')
]