from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bookstore import views


urlpatterns = [

    path('list/', views.bookListView.as_view(),name='list'),
    path('create/',views.bookCreateView.as_view(),name='create'),
    path('createauthor/',views.authorCreateView.as_view(),name='create_author'),
    path('book/<int:pk>/detail/', views.bookRetriveView.as_view(), name='retrieve'),
    path('delete/<int:pk>/',views.bookDeleteView.as_view(),name='delete'),
    path('book/<int:pk>/update/',views.bookUpdateView.as_view(),name='update'),
    path('authordetail/<int:pk>/',views.authordetailsview.as_view(),name='author-detail')
]


urlpatterns = format_suffix_patterns(urlpatterns)