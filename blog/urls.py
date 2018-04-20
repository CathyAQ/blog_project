from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^article_list/$',views.article_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail),
    url(r'^archive/$',views.archive),
    url(r'^category/$',views.category)
]