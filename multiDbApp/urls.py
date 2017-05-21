"""multiDbApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.models import TestData

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

using =None

class MultiDBModelAdminCommon(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        global using
        setDatabaseToFetchQuery(request)
        obj.save(using=using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        global using
        setDatabaseToFetchQuery(request)
        obj.delete(using=using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        global using
        setDatabaseToFetchQuery(request)
        return super(MultiDBModelAdminCommon, self).get_queryset(request).using(using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        global using
        setDatabaseToFetchQuery(request)
        return super(MultiDBModelAdminCommon, self).formfield_for_foreignkey(db_field, request, using=using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        global using
        setDatabaseToFetchQuery(request)
        return super(MultiDBModelAdminCommon, self).formfield_for_manytomany(db_field, request, using=using, **kwargs)

def setDatabaseToFetchQuery(request):
    if request.session['database']:
        global using
        using=request.session['database']
        #del request.session['database']

def setDatabases():
    """function to return the database name"""
    databases=[
        {'site_id':'testdb1'},
        {'site_id':'testdb2'},
        {'site_id':'testdb3'},
        {'site_id':'testdb4'},
        {'site_id':'testdb5'},
    ]
    databases_l={}
    for d in databases:
        databases_l.update({
            'ENGINE': 'django.db.backends.mysql',
            'NAME': str(d.get('site_id')),
            'USER':"root",
            'PASSWORD':"root",
            'PORT':'3306'
        })
    DATABASES=databases_l
    global urlpatterns
    for d1 in databases:
        global using
        using = d1.get('site_id')
        site_id=admin.AdminSite(d1.get('site_id'))
        site_id.register(TestData,MultiDBModelAdminCommon)
        #register complaint management models
        name_local=d1.get('site_id')+'_admin/'
        local_list=list()
        local_list.append(url(r'^'+name_local, site_id.urls))
        urlpatterns = urlpatterns + local_list


setDatabases()
