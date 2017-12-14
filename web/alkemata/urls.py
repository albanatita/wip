from django.conf.urls import url,include,patterns
from django.contrib import admin
admin.autodiscover()
urlpatterns =[ 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls', namespace='news', app_name='news')),
]
