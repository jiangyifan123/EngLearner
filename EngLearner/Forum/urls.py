from django.urls import path
from .views import *
urlpatterns = [
    path('', forumView.as_view(), name = 'forum_index'),
    path('detail_page/<int:page_id>', detailView.as_view(), name = 'detail_page'),
    path('new_page/', new_page_View.as_view(), name = 'new_page'),
    path('page_up/', page_up_View, name = 'page_up'),
]