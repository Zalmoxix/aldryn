from django_auth_ldap.backend import LDAPBackend
import cms
from cms import api
from cms.models.pagemodel import Page
from filer.models.imagemodels import Image

alumno='staff'
titulo='prueba5'
namespaceblog='blogprueba'

ldap=LDAPBackend()
login=ldap.populate_user(alumno)
#ya creado en aldryn, no volver a ejecutar

new=NewsBlogConfig(namespace='BlogPrueba',app_title='BlogPrueba')
new.save_base()
new.create_translation(language_code='en')
padre=Page.objects.filter(title_set__title='Alumnos')[0]
pagina=cms.api.create_page(title=titulo,template='fullwidth.html',language='en',apphook='NewsBlogApp',apphook_namespace=new.namespace,parent=padre,published=True,in_navigation=True)
#
pag=Page.objects.filter(title_set__title=titulo)[0]
owner=cms.api.assign_user_to_page(page=pagina, user=login, grant_all=True)
pagina.publish(language='en')

place=pagina.placeholders.get(slot='feature')
plugin1=cms.api.add_plugin(placeholder=place,plugin_type='StylePlugin',language='en')
plugin2=cms.api.add_plugin(placeholder=place,plugin_type='StylePlugin',language='en')

#nbc=NewsBlogConfig.objects.filter(namespace=namesp)
#basetop=nbc.placeholder_base_top
img=images.original_filename()
