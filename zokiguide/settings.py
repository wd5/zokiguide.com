# Django settings for zokiguide project.
#import os

IN_PRODUCTION = True
#comment

try:
    from local_settings import *
except ImportError, e:
    pass

DEBUG = not IN_PRODUCTION
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ( 'Dan Tyan', 'dan.tyan@gmail.com' ),
 )

MANAGERS = ADMINS

if IN_PRODUCTION:
    DOCROOT = '/home/dantyan/webapps/zokiguide/zokiguide/'
    APPPATH = '/home/dantyan/webapps/zokiguide/zokiguide/'
    MEDIA_ROOT = '/home/dantyan/webapps/zokiguide_media/'
    MEDIA_URL = 'http://media.zokiguide.com/'
    STATIC_ROOT = '/home/dantyan/webapps/zokiguide_static/'
    STATIC_URL = 'http://static.zokiguide.com/'
else:
    DOCROOT = '/home/dan/www/django/zokiguide/'
    APPPATH = '/home/dan/www/django/zokiguide/'
    MEDIA_ROOT = '/home/dan/www/django/zokiguide/media/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = APPPATH + 'static/'
    STATIC_URL = '/static/'



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

#ugettext = lambda s: s
#
#LANGUAGES = (
#    ('en', ugettext('English')),
#    ('ru', ugettext('Russian')),
#)

LOCALE_PATHS = (
    APPPATH + 'locale',
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"


# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    APPPATH + 'account/static',
    APPPATH + 'accounts/static',
    APPPATH + 'blogs/static',
	APPPATH + 'bookmarks/static',
	APPPATH + 'catalog/static',
	APPPATH + 'classifieds/static',
	APPPATH + 'events/static',
	APPPATH + 'forum/static',
	APPPATH + 'gallery/static',
	APPPATH + 'guidebook/static',
	APPPATH + 'main/static',
	APPPATH + 'tours/static',
    APPPATH + 'common/static',
	APPPATH + 'zokiguide/static',
 )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
 )



# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
 )

MIDDLEWARE_CLASSES = (
#    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
 )

ROOT_URLCONF = 'zokiguide.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'zokiguide.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	APPPATH + 'account/templates',
	APPPATH + 'accounts/templates',
	APPPATH + 'blogs/templates',
	APPPATH + 'bookmarks/templates',
	APPPATH + 'catalog/templates',
	APPPATH + 'classifieds/templates',
	APPPATH + 'events/templates',
	APPPATH + 'forum/templates',
    APPPATH + 'gallery/templates',
    APPPATH + 'guidebook/templates',
    APPPATH + 'main/templates',
    APPPATH + 'tours/templates',
    APPPATH + 'common/templates',
    APPPATH + 'zokiguide/templates',
 )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    'django.core.context_processors.i18n',
    'zokiguide.context_processors.custom',

#    'blog.context_processors.common',
 )

INSTALLED_APPS = (
#    'django.contrib.auth',
#    'django.contrib.contenttypes',
#    'django.contrib.sessions',
#    'django.contrib.sites',
#    'django.contrib.messages',
#    'django.contrib.staticfiles',
#
#
##    'filebrowser',
#    # Uncomment the next line to enable the admin:
#    'django.contrib.admin',
#    # Uncomment the next line to enable admin documentation:
#    'django.contrib.admindocs',
#    'mptt',
#
#    'slugify',
#    'smart_selects',
#
#
#    'account',
#    'blogs',
#    'catalog',
#    'classifieds',
#    'bookmarks',
#    'guidebook',
#    'main',
#    'forum',
#    'location',
 )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'zoki': {
            'format': '%(levelname)s %(asctime)s [%(module)s:%(lineno)s] --> %(message)s'
        },
        'console': {
            'format': '\n%(name)s: %(levelname)s %(asctime)s [%(module)s:%(lineno)s] --> %(message)s\n'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': APPPATH + "/log/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'zoki',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'zoki':{
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    }
}


#LOGIN_URL = '/account/login/'
#LOGOUT_URL = '/account/logout/'
LOGIN_REDIRECT_URL = '/account/'


#--------------------------------
# debug toolbar
#--------------------------------
if DEBUG:
    MIDDLEWARE_CLASSES += ( 'debug_toolbar.middleware.DebugToolbarMiddleware', )
    INSTALLED_APPS += ( 'debug_toolbar', )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }


#--------------------------------

#--------------------------------
# django tagging
#--------------------------------

INSTALLED_APPS += ( 'tagging', )

#--------------------------------

#--------------------------------
# bootstrap form
#--------------------------------

INSTALLED_APPS += ( 'bootstrapform', )

#--------------------------------


# ## SOUTH: BEGIN
INSTALLED_APPS += ( 'south', )
SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False
# ## SOUTH: END


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
    }
}

# tinymce
# --------------------------------------------------
INSTALLED_APPS += ( 'tinymce', )
TINYMCE_JS_ROOT = STATIC_URL + 'js/tiny_mce/'
TINYMCE_JS_URL = STATIC_URL + 'js/tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace,inlinepopups",
    'theme': "advanced",
    'height':"500px",
    'fix_list_elements' : True,
    'force_p_newlines' : False,
    'force_br_newlines': False,
    'forced_root_block': '',
    'keep_styles':'true',
    'remove_linebreaks' : False,
    'paste_auto_cleanup_on_paste' : True,
    'dialog_type' : 'modal',
#    URL
    'relative_urls' : False,
    'remove_script_host': False,
    'convert_urls' : False,
}

INTERNAL_IPS = ( '127.0.0.1', )


STATUS_CHOICES = (
    ( 'active', 'active' ),
    ( 'inactive', 'inactive' ),
    ( 'draft', 'draft' ),
    ( 'deleted', 'deleted' ),
 )

SEND_BROKEN_LINK_EMAILS = True

DEFAULT_FROM_EMAIL = 'zokiguide@gmail.com'
EMAIL_SUBJECT_PREFIX = '[ Zoki Guide ]'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = "587"
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = 'craZZyDemon'
EMAIL_USE_TLS = True

USE_DJANGO_JQUERY = False


# imagekit
# --------------------------------------------------
INSTALLED_APPS += ( 'imagekit', )

# compressor
# --------------------------------------------------
INSTALLED_APPS += ( 'compressor', )
STATICFILES_FINDERS += ( 'compressor.finders.CompressorFinder', )




# disqus
# --------------------------------------------------
INSTALLED_APPS += ('disqus',)
DISQUS_API_KEY = 'IDH8t5QxVAkXpr2zBp19OZDdRkX3YMJbvPtByEFB7fKzyOASIhgfiSs62tixb6LS'
DISQUS_WEBSITE_SHORTNAME = 'zokiguidecom'


#AUTH_USER_MODEL = 'account.Profile'


# grappelli
# --------------------------------------------------
#INSTALLED_APPS += ('grappelli',)





#end file