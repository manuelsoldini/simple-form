from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

from common import views as common


urlpatterns = patterns('',
    # Example:
    # (r'^simpleform/', include('simpleform.foo.urls')),

    (r'^$', common.login),
    (r'^login/$', common.login),
    (r'^success/$', common.success),
    (r'^fake/$', common.fake),
    (r'^becomeAJedi/$', common.becomeAJedi),
    (r'^farewell/$', common.farewell),
    (r'^admin/', include(admin.site.urls)),
    #(r'^.*/$', common.login),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns((r'^*(/*)*$', common.login))
