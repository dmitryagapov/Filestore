from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'filestore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^list/$', 'file.views.all_files'),

    url(r'^delete/(?P<file_hash>\w+)/$', 'file.views.delete_file'),
    # url(r'^uploaded_files/(?P<file_hash>\w+)/_ctypes - Copy.lib/$', 'file.views.download_file'),
    url(r'^uploaded_files/(?P<file_hash>\w+)/(?P<file_name>.+)/$', 'file.views.download_file'),

    url(r'^user/$', 'file.views.user_files'),

    # r'^articles/get/(?P<article_id>\d+)/$'
    # url(r'^(?P<user_name>)$', 'file.views.all_files'),
    # url(r'^$', 'file.views.all_files'),


)
