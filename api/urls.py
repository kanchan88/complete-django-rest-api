from django.urls import path
from .views import ArticleAPIView, ArticleDetailAPIView, GenericAPIView

urlpatterns = [
    # path('article', article_list),
    # path('article/<int:pk>', article_detail),
    path('blog',ArticleAPIView.as_view() ),
    path('blog-detail/<int:id>', ArticleDetailAPIView.as_view()),
    path('article/<int:id>', GenericAPIView.as_view()),
    path('article', GenericAPIView.as_view()),
    
]
