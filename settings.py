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
	'analytical',
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

CMS_PERMISSION = True

import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType 

AUTH_LDAP_SERVER_URI = "ldap://172.17.0.2"


AUTH_LDAP_BIND_DN = "cn=admin,dc=example,dc=org"
AUTH_LDAP_BIND_PASSWORD = "admin"

AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=example,dc=org",
    ldap.SCOPE_SUBTREE, "(cn=%(user)s)")


LDAP_APPEND_DOMAIN = "example.org"


AUTH_LDAP_USER_ATTR_MAP = {

}

CAMO_URI = ''

AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=example,dc=org",
    ldap.SCOPE_SUBTREE, "(ObjectClass=PosixGroup)")

AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr='cn')

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
	"is_staff": ["cn=staff,ou=people,dc=example,dc=org", "cn=admin,ou=people,dc=example,dc=org"],
	"is_superuser": ["cn=admin,ou=people,dc=example,dc=org", "cn=staff,ou=people,dc=example,dc=org"]
}

AUTH_LDAP_FIND_GROUP_PERMS= True


PIWIK_DOMAIN_PATH = '0.0.0.0/piwik'
PIWIK_SITE_ID = '1'
PIWIK_ANALYTICAL_INTERNAL_IPS = ['192.168.1.1']
