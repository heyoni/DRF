from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views.generic import RedirectView, TemplateView
from django_pydenticon.views import image as pydenticon_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instagram/', include('instagram.urls')),
    path('', RedirectView.as_view(pattern_name='instagram:index'),name='root'),
    # path('', login_required(TemplateView.as_view(template_name='root.html')), name='root'),
    # path('', login_required(pattern_name='instagram:index'), name='root'),

    # 패턴에 매칭되지 않고 모든 경우를 감싸는 view는 re_path 사용
    # re_path('', TemplateView.as_view(template_name='root.html'), name='root'),

    path('accounts/', include('accounts.urls')),
    path('identicon/image/<path:data>/', pydenticon_image, name='pydenticon_image'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)