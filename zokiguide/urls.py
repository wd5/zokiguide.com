from django.conf.urls import patterns, include, url
from django.conf import settings
#from django.views.generic.simple import direct_to_template
from django.views.generic.base import TemplateView
#from filebrowser.sites import site

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns( '', url( r'^$', include( 'main.urls' ) ),)

if 'grappelli' in settings.INSTALLED_APPS:
    urlpatterns += patterns( '', url( r'^grappelli/', include( 'grappelli.urls' ) ),)

urlpatterns += patterns( '',
    # Examples:
    # url(r'^$', 'zokiguide.views.home', name='home'),
    # url(r'^zokiguide/', include('zokiguide.foo.urls')),


#    url( r'^admin/filebrowser/', include( site.urls ) ),
    url( r'^tinymce/', include( 'tinymce.urls' ) ),

    # Uncomment the admin/doc line below to enable admin documentation:
    url( r'^admin/doc/', include( 'django.contrib.admindocs.urls' ) ),

    # Uncomment the next line to enable the admin:
    url( r'^admin/', include( admin.site.urls ) ),

    url( r'^chaining/', include( 'smart_selects.urls' ) ),

#    url( r'^$', include( 'main.urls' ) ),
    url( r'^account/', include( 'account.urls' ) ),
    url( r'^accounts/', include( 'accounts.urls' ) ),
    url( r'^bookmarks/', include( 'bookmarks.urls' ) ),
    url( r'^blogs/', include( 'blogs.urls' ) ),
    url( r'^guidebook/', include( 'guidebook.urls' ) ),
    url( r'^catalog/', include( 'catalog.urls' ) ),
    url( r'^classifieds/', include( 'classifieds.urls' ) ),
    url( r'^forum/', include( 'forum.urls' ) ),
    url( r'^u/', include( 'u.urls' ) ),
    url( r'^search-result/', TemplateView.as_view(
        template_name = 'common/google-search-result.html'
    )),
    (r'^robots.txt$', TemplateView.as_view(
        template_name='common/robots.txt.html'
    )),

 )


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns( '',
        ( r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT} ) )
