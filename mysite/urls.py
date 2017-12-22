from django.conf.urls import url,include
from django.contrib import admin
from blog.views import MainView
from django.contrib.auth.views import LoginView 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/' , include('blog.urls')),
    url(r'^api/'  , include('api.urls')),
    url(r'^$', MainView.as_view() ,name='app_main'),
    url(r'^login/$' ,LoginView.as_view(template_name='blog/login.html') , name='login'),
    url(r'^gitweb/' ,include('gitweb.urls'))
]

urlpatterns += staticfiles_urlpatterns()
