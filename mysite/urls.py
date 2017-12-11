from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/' , include('blog.urls')),
    url(r'^api/'  , include('api.urls')),
    url(r'^$', TemplateView.as_view(template_name="blog/app_main.html") ,name='app_main'),
    url(r'^login/$' ,LoginView.as_view(template_name='blog/login.html') , name='login')
]
