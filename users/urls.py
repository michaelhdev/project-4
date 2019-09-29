from django.conf.urls import url, include
from users.views import logout, login, registration
from users import url_reset

urlpatterns = [
    url('logout/', logout, name="logout"),
    url('login/', login, name="login"),
    url('register/', registration, name="registration"),
    url(r'^password-reset/', include(url_reset))
]
