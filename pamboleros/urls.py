from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pamboleros.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.index'),
    url(r'^index/$', 'app.views.index'),
    url(r'^login/$', 'app.views.login'),
    url(r'^noticias/$', 'app.views.noticias'),
    url(r'^logout/$', 'app.views.logout'),
)