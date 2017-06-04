from django.conf.urls import url
from mia import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'posts/(?P<category_id>\d+)/$', views.posts, name='posts'),
    url(r'posts/(?P<category_id>\d+)/(?P<board_id>\d+)/$', views.postSelect, name='postSelect'),
    url(r'posts/new/$',views.posts_new, name='posts_new'),
    url(r'posts/edit/(?P<pk>\d+)/$',views.posts_edit, name='posts_edit'),
    url(r'posts/delete/(?P<pk>\d+)/$',views.posts_delete, name='posts_delete'),
    url(r'comment/delete/(?P<pk>\d+)/$',views.comment_delete, name='comment_delete'),
    url(r'posts/(?P<category_id>\d+)/(?P<board_id>\d+)/(?P<pk>\d+)/$',views.comment_new,name='post_detail'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)