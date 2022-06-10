from django.urls import path
from . import views


urlpatterns  = [
    path('',views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name="post_edit"),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name="post_remove"),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('menu/',views.MenuListView.as_view(), name='menu'),
    path('menu/new/', views.CreateItemMenuView.as_view(), name='itemmenu'),
    path('menu/<int:pk>/remove/', views.MenuDeleteView.as_view(), name="menu_remove"),
    path('menu/<int:pk>/update/', views.MenuUpdateView.as_view(), name="menu_update"),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('galeria/', views.galeria, name='galeria'),
]
