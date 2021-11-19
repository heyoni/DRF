from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
# from tutorial.quickstart import views
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('', include('instagram.urls')),
    path('instagram/', include('instagram.urls')),
    path('accounts/',include('accounts.urls')),
    path('', TemplateView.as_view(template_name='root.html'), name='root'),
    # path('', RedirectView.as_view(template_name='root.html'), name='root'),
    path('quiz/', include('quiz.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns +=[
        path('__debug__/', include(debug_toolbar.urls)),
    ]