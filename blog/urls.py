from django.conf.urls import url
from . import views

app_name ='post'

urlpatterns = [
    url(r'^$',views.post_list,name="list"),
    url(r'^create/$',views.create_post,name='create'),
    url(r'^(?P<slug>[\w-]+)/$',views.detail_view,name='detail'),
]


