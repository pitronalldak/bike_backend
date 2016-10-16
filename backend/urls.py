from django.conf.urls import url, include


urlpatterns = [
    url(r'^api/auth/', include('my_auth.urls', namespace='auth_urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^s/', include('store.urls', namespace='store_urls'))
]
