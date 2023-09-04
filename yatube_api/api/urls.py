from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, GroupViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(
    r'^posts/(?P<post_pk>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    r'posts',
    PostViewSet,
    basename='posts'
)

router.register(
    r'groups',
    GroupViewSet,
    basename='groups'
)


urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('v1/', include(router.urls)),
]
