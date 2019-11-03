from django.conf.urls import url
from sg_web import views  

urlpatterns = [
    url(r'^signup/', views.SignUp, name='signup'),
    url(r'^register_success/', views.Register_Success, name='register_success'),
    url(r'^about/', views.about, name='about'),
    url(r'^contactus/', views.contactus, name='contactus'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^category/selenium/seleniumbasic', views.seleniumbasic, name='seleniumbasic'),
    url(r'^category/selenium/seleniumxpath', views.seleniumxpath, name='seleniumxpath'),
    url(r'^category/selenium/testng', views.testng, name='testng'),
    url(r'^category/django/djangobasic', views.djangobasic, name='djangobasic'),
    url(r'^', views.index, name='index'),
]
