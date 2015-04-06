from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ReadMyPaper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


 #user auth urls

 	url(r'^accounts/login/$' , 'ReadMyPaper.views.login') ,
 	url(r'^accounts/auth/$' , 'ReadMyPaper.views.auth_view') ,
 	url(r'^accounts/logout/$' , 'ReadMyPaper.views.logout') , 
 	url(r'^accounts/loggedin/$' , 'ReadMyPaper.views.loggedin') ,
 	url(r'^accounts/invalid/$' , 'ReadMyPaper.views.invalid_login') ,
 	url(r'^accounts/register/$' , 'ReadMyPaper.views.register_user') ,
 	url(r'^accounts/register_success/$' , 'ReadMyPaper.views.register_success') ,

 )