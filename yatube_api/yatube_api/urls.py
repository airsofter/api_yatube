from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
# from rest_framework import routers
# from rest_framework.authtoken import views

# from api.views import PostViewSet, GroupViewSet, CommentViewSet


# router = routers.DefaultRouter()
# router.register(r'api/v1/posts', PostViewSet, basename='posts')
# router.register(r'api/v1/groups', GroupViewSet, basename='groups')
# router.register(r'api/v1/posts/(?P<post_id>\d+)/comments',
#                 CommentViewSet,
#                 basename='comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls', namespace='api'))
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
