from django.conf.urls import url, include
from users.views import logout, login, registration, user_account
from users import url_reset

urlpatterns = [
    url('logout/', logout, name="logout"),
    url('login/', login, name="login"),
    url('register/', registration, name="registration"),
    url('account/', user_account, name="account"),
    url(r'^password-reset/', include(url_reset))
]
