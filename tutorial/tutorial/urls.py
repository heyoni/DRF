from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from tutorial.quickstart import views
import debug_toolbar

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('instagram.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
