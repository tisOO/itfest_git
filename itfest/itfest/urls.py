from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout


from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'itfest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^accounts/login/$', login),
	url(r'accounts/logout', logout),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^teams/$', 'itfest.users.views.view_team_list'),
	url(r'^news/(?P<count_news>\d*)/$', 'itfest.info.views.view_news'),
	url(r'^news/$', 'itfest.info.views.view_news'),
	
)
