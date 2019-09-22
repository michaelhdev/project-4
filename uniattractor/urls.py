"""uniattractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import get_homepage
from users import urls as users_urls
from bugs import urls as bug_urls
from cart import urls as cart_urls
from features import urls as feature_urls
from checkout import urls as checkout_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_homepage, name="index"),
    url(r'^accounts/', include(users_urls)),
    url(r'^bugs/', include(bug_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^cart/', include(cart_urls)),
    url(r'^features/', include(feature_urls)),
]
