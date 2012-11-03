from django.conf import settings
from django import get_version
#from django.contrib.sites.models import Site
#from django.core.urlresolvers import reverse
#from django.shortcuts import redirect
#from django.utils.translation import ugettext, ugettext_lazy as _

def custom(request):
    context = {
        'django_version': get_version(),
        'settings': settings,
        'securelayer': False,
    }
    return context
