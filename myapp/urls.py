from django.urls import path
from . import views

urlpatterns = [
path('', views.index_view, name='index_view'), # 首頁
path('search/', views.search_view, name='search_view'), # 🔍 搜尋功能
path('detail/<int:item_id>/', views.detail_view, name='detail_view'), # 🌟 20個隨機樣本詳情頁
]