from django.conf.urls import patterns, include, url

# (?P<year>\d{4})
urlpatterns = patterns( 'u',
    url( r'^$', 'views.home', name = 'u-home' ),
 )

