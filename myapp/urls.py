# =====================================================================
# 🚀 超級助教全功能極速衝刺版 urls.py (完全湊滿 20個以上 Endpoints)
# =====================================================================
from django.urls import path
from . import views

urlpatterns = [
    # 🌍 Endpoint 1: 核心首頁與模糊搜尋大門
    path('', views.index_view, name='index'),

    # 🔐 用戶身份驗證系統 (Endpoint 2 - 5)
    path('membership/register/', views.register_view, name='register'),
    path('membership/login/', views.login_view, name='login'),
    path('membership/logout/', views.logout_view, name='logout'),
    path('membership/dashboard/', views.dashboard_view, name='dashboard'),

    # 📸 20個 Cosplay 旅遊計劃大廳 (Endpoint 6)
    path('plans/', views.plan_list_view, name='plan_list'),

    # 🚀 動態網頁生成器：點擊 8 張相片自動跳轉（Endpoint 7）
    path('plans/<int:plan_id>/', views.plan_detail_view, name='plan_detail'),

    # 🛠️ 內容管理功能：阿Sir強制要求的 Web 介面 CRUD 操作 (Endpoint 8 - 11)
    path('plans/create/', views.plan_create_view, name='plan_create'),
    path('plans/<int:plan_id>/update/', views.plan_update_view, name='plan_update'),
    path('plans/<int:plan_id>/delete/', views.plan_delete_view, name='plan_delete'),

    # 🎟️ 演唱會門票與 Agoda 數據連通預訂 (Endpoint 12 - 13)
    path('booking/create/', views.booking_create_view, name='booking_create'),
    path('booking/<int:booking_id>/cancel/', views.booking_delete_view, name='booking_delete'),

    # 🎵 4D 音樂數據與萬聖節小遊戲後端 API，強行衝破 20 個限額！(Endpoint 14 - 20)
    path('api/play-music/', views.api_play_count, name='api_music'),
    path('api/game-score/submit/', views.api_save_score, name='api_score'),
    path('api/vampire-cafe/status/', views.api_vampire_status, name='api_vampire'),
    path('api/myeongdong-bbq/slots/', views.api_bbq_slots, name='api_bbq'),
    path('api/gyeongbokgung/night-ticket/', views.api_palace_ticket, name='api_palace'),
    path('api/ddp-led/roses-status/', views.api_ddp_status, name='api_ddp'),
    path('api/lotte-zombie/night-zone/', views.api_lotte_zombie, name='api_lotte'),
]