"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
# from django.views.generic import TemplateView
# from django.views import defaults as default_views
# from django.contrib.auth.views import logout
from .router import router
from portfolio import views
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('products/', include("products.urls", namespace="products")),
    # url(r'^$', TemplateView.as_view(template_name='index.html')),
    # frontend urls
    # path('', views.home, name='home'),
    # path('works/', views.works, name='works'),
    # path('work/<str:name>/', views.description, name='description'),
    # path('skills/', views.skills, name='skills'),

] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT,
    # settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
