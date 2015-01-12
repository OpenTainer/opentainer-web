from django.conf.urls import patterns, include, url
from django.contrib import admin
from home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opentainer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', include('home.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^about_us/', views.about_us, name='about_us'),
    url(r'^documentation/', views.documentation, name='documentation'),
)
