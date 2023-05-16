from django.urls import path

from . import views

urlpatterns = [
#    path('', views.home, name='homePage'),
    path('', views.HomeView.as_view(), name='homePage'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article-detail'),
    #pk is premier key
    path('add_post', views.AddPostView.as_view(), name='post_add'),
    path('article/edit/<int:pk>',views.PostUpdateView.as_view(), name='update-post'),
    path('article/category', views.AddCategoryView.as_view(), name='add-category'),
    path('article/<int:pk>/Delete',views.PostDeleteView.as_view(), name= 'delete-post'),
    
    #category page
    path('category/<str:cats>/',views.CategoryView, name='category'), # cats will get category from index and convert to string cats
    
    path('category-list/',views.CategoryListView, name='category-list'),
    
    path('like/<int:pk>/',views.LikeView, name= "like_post"),
    
    path('article/<int:pk>/comment',views.AddCommentView.as_view(), name= 'comment-section'),
]
