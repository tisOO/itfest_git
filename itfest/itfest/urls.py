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
	url(r'^main/$', 'itfest.main.views.view_main'),
	url(r'^task/(?P<task_id>\d*)/$','itfest.main.views.view_task'),
	url(r'^rules/$', 'itfest.main.views.view_rules'),
	url(r'^contacts/$', 'itfest.main.views.view_contacts'),
	url(r'^$', 'itfest.main.views.view_main'),
	url(r'^logout/$','itfest.main.views.view_logout'),
	url(r'^login/$', 'itfest.main.views.view_login'),
)
