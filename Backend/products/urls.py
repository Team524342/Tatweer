from django.urls import path
from .views import ProductCreateView,ProductListView,ProductRetriveView,ProductDestroyVIew,ProductUpdateView

urlpatterns = [
    path('create/',ProductCreateView.as_view()),
    path('',ProductListView.as_view()),
    path('update/<int:id>/',ProductUpdateView.as_view()),
    path('delete/<int:id>/',ProductDestroyVIew.as_view()),
    path('retrive/<int:id>/',ProductRetriveView.as_view()),
]