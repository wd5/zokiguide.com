# Django settings for zokiguide project.
import os

IN_PRODUCTION = True

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
    DOCROOT = '/home/zokisoft/www/zokiguide/'
    APPPATH = '/home/zokisoft/django/zokiguide/'
else:
    DOCROOT = '/home/dan/www/django/zokiguide/'
    APPPATH = '/home/dan/www/django/zokiguide/'



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

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
MEDIA_ROOT = DOCROOT + 'media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = DOCROOT + 'static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = ( 
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    APPPATH + 'account/static',
    APPPATH + 'accounts/static',
    APPPATH + 'blogs/static',
	APPPATH + 'bookmarks/static',
	APPPATH + 'common/static',
	APPPATH + 'catalog/static',
	APPPATH + 'events/static',
	APPPATH + 'forum/static',
	APPPATH + 'gallery/static',
	APPPATH + 'guidebook/static',
	APPPATH + 'main/static',
	APPPATH + 'tours/static',
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
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
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
	APPPATH + 'common/templates',
	APPPATH + 'events/templates',
	APPPATH + 'forum/templates',
	APPPATH + 'gallery/templates',
	APPPATH + 'guidebook/templates',
	APPPATH + 'main/templates',
	APPPATH + 'tours/templates',
	APPPATH + 'zokiguide/templates',
#    os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/'),
 )

TEMPLATE_CONTEXT_PROCESSORS = ( 
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    'zokiguide.context_processors.custom',
#    'blog.context_processors.common',
 )

INSTALLED_APPS = ( 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'grappelli',
#    'filebrowser',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'mptt',
    'tinymce',
    'slugify',
    'smart_selects',


    'account',
    'catalog',
    'bookmarks',
    'main',
    'forum',
    'location',
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
LOGIN_REDIRECT_URL = '/'

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

#--------------------------------
# django categories
#--------------------------------

# INSTALLED_APPS += (
#    'categories',
#    'categories.editor',
# )
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


#_PATH = os.path.abspath( os.path.dirname( __file__ ) )

#MEDIA_ROOT = os.path.join( _PATH, 'files', 'media' )
#MEDIA_URL = '/media/'

#STATIC_ROOT = os.path.join( _PATH, 'files', 'static' )
#STATIC_URL = '/static/'
#STATICFILES_DIRS += (
#    os.path.join( _PATH, 'static' ),
# )

TINYMCE_JS_ROOT = STATIC_URL + 'js/tiny_mce/'
TINYMCE_JS_URL = STATIC_URL + 'js/tiny_mce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'height':"500px",
}
#TINYMCE_COMPRESSOR = True

#ADMIN_MEDIA_PREFIX = '/static/admin/'

INTERNAL_IPS = ( '127.0.0.1', )


STATUS_CHOICES = ( 
    ( 'active', 'active' ),
    ( 'inactive', 'inactive' ),
    ( 'draft', 'draft' ),
    ( 'deleted', 'deleted' ),
 )

SEND_BROKEN_LINK_EMAILS = True

DEFAULT_FROM_EMAIL = 'zokiguide@gmail.com'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = "587"
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = 'craZZyDemon'
EMAIL_USE_TLS = True

#AJAX_LOOKUP_CHANNELS = {
#    #   pass a dict with the model and the field to search against
#    'city'  : {'model':'example.person', 'search_field':'name'}
#}
# magically include jqueryUI/js/css
#AJAX_SELECT_BOOTSTRAP = True
#AJAX_SELECT_INLINES = 'inline'

USE_DJANGO_JQUERY = True

#
#FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
#FILEBROWSER_MEDIA_URL = MEDIA_URL
#FILEBROWSER_DIRECTORY = 'uploads/'
#
#FILEBROWSER_EXTENSIONS = {
#    'Folder': [''],
#    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'],
#    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv'],
#    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
#    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p']
#}
#FILEBROWSER_SELECT_FORMATS = {
#    'file': ['Folder', 'Image', 'Document', 'Video', 'Audio'],
#    'image': ['Image'],
#    'document': ['Document'],
#    'media': ['Video', 'Audio'],
#}
#FILEBROWSER_VERSIONS = {
#    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
#    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
#    'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
#    'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
#    'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
#    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
#}
#FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'big', 'large']
#FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'
#FILEBROWSER_PLACEHOLDER = ''
#FILEBROWSER_SHOW_PLACEHOLDER = ''
#FILEBROWSER_FORCE_PLACEHOLDER = ''
#FILEBROWSER_IMAGE_MAXBLOCK = '1024*1024'
#FILEBROWSER_MAX_UPLOAD_SIZE = 10485760
#FILEBROWSER_CONVERT_FILENAME = True
#FILEBROWSER_LIST_PER_PAGE = 50
#FILEBROWSER_DEFAULT_PERMISSIONS = 0755
