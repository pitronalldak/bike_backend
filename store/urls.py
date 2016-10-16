from django.conf.urls import url

from .views import FreestyleBmxBikeView, AllItemsView, BikesView


urlpatterns = [
    url(r'^all_items/', AllItemsView.as_view()),
    url(r'^bikes/', BikesView.as_view()),
    url(r'^freestyle_bmx_bike/(?P<id>[0-9]+)?', FreestyleBmxBikeView.as_view())
]
