from django.conf.urls import url
import rest_framework_jwt.views

from .views import UserProfileView, CreateUserView, MainUserView


urlpatterns = [
    url(r'^$', rest_framework_jwt.views.obtain_jwt_token),
    url(r'^current/', UserProfileView.as_view()),
    url(r'^reg/', CreateUserView.as_view()),
    url(r'^user/', MainUserView.as_view()),
]
