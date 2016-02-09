# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-django-cms',
    'aldryn-devsync',
    'aldryn-bootstrap3',
    'aldryn-common',
    'aldryn-disqus',
    'aldryn-events',
    'aldryn-faq',
    'aldryn-forms',
    'aldryn-jobs',
    'aldryn-newsblog',
    'aldryn-people',
    'aldryn-style',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())


# all django settings can be altered here

INSTALLED_APPS.extend([
	'django_extensions',
    # add you project specific apps here
])

TEMPLATE_CONTEXT_PROCESSORS.extend([
    # add your template context processors here
])

MIDDLEWARE_CLASSES.extend([
    # add your own middlewares here
])

AUTHENTICATION_BACKENDS = (
                 'django_auth_ldap.backend.LDAPBackend',
 #  		 'django.contrib.auth.backends.ModelBackend'

    )

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

AUTH_LDAP_SERVER_URI = "ldap://172.17.0.2"


AUTH_LDAP_BIND_DN = "cn=admin,dc=example,dc=org"
AUTH_LDAP_BIND_PASSWORD = "admin"

AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=example,dc=org",
    ldap.SCOPE_SUBTREE, "(cn=%(user)s)")


LDAP_APPEND_DOMAIN = "example.org"


AUTH_LDAP_USER_ATTR_MAP = {

}

CAMO_URI = ''

