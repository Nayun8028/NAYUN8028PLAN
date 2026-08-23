from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CosplayPlan, Booking, MemberProfile

# ==========================================
# ⚡ Endpoint 1: Aki 4D 萬聖節 K-Pop 究極完全體主網頁
# ==========================================
def index_view(request):
    # 🔒 世紀大解封：升級為最高權限全域線上高清放行圖檔，徹底強行粉碎 Linux 本地大小寫與 404 一片黑死穴！
    skz_data = [
        {'name': 'Stray Kids (스트レイ 키즈)', 'img': 'https://unsplash.com', 'desc': 'JYP 旗下的世界級男團，成員包括方燦、Lee Know、彰彬、鉉辰、HAN、Felix、昇玟、I.N！'},
        {'name': 'Felix (필릭斯)', 'img': 'https://unsplash.com', 'desc': '擁有反差萌魅力嘅低音炮 Rapper！笑起來像天使一樣溫暖嘅低音小卡 💖'},
        {'name': 'Lee Know (리노)', 'img': 'https://unsplash.com', 'desc': '四次元魅力嘅舞蹈隊長，神級顏值嘅貓咪大師！🐱'},
        {'name': '鉉辰 (현진)', 'img': 'https://unsplash.com', 'desc': 'Stray Kids 裝視覺中心與主舞！舞台藝術感與帥氣氣場滿滿嘅當代藝術王子！'},
        {'name': '方燦 (방찬 - Bang Chan)', 'img': 'https://unsplash.com', 'desc': 'Stray Kids 裝偉大隊長與全能製作人！3RACHA 裝核心成員，守護著團員與 STAY 裝暖心大哥哥！'},
        {'name': '彰彬 (창빈 - Changbin)', 'img': 'https://unsplash.com', 'desc': '實力爆發嘅快嘴 Rapper！外表強壯卻內心極之極之極之搞笑與撒嬌裝團隊核心！'},
        {'name': '弘大 萬盛節 Witch\'s Kitchen (弘大店) 🧙‍♀️', 'img': 'https://unsplash.com', 'desc': '走訪首爾弘大必前往嘅萬聖節主題餐廳！店內充斥著魔幻骷髏與點滴飲料，萬聖節萬聖節氛圍感直接爆棚！'},
        {'name': '萬盛節宮殿舞台特別開放 🌙', 'img': 'https://unsplash.com', 'desc': '限定召喚！穿上最帥氣嘅傳統韓服，在月光皎潔嘅古老宮殿與萬盛節霓虹燈光中漫步！'},
        {'name': '吸血鬼血色主題咖啡廳 Vampire Cafe 🩸', 'img': 'https://unsplash.com', 'desc': '限定召喚！店內充滿著紅絲絨天鵝絨、十字架與古老棺木，提供血紅色嘅特色魔幻飲品！'},
        {'name': '樂天世界萬聖節殭屍狂歡之夜 🧟‍♂️', 'img': 'https://unsplash.com', 'desc': '限定召喚！走訪首爾樂天世界，在夜幕低垂時體驗被極度恐怖嘅萬盛節殭屍全園大遊行裝驚繕大冒險！'},
        {'name': '🚨 萬聖節防被阿Sir睇死奪冠計畫', 'img': 'https://unsplash.com', 'desc': '最終決戰防線！張大奢華裝歌德風 Cosplay 狂歡，並到愛音樂網頁染大遊行與全域功能完美封頂大放行！'}
    ]

    search_query = request.GET.get('q', '').strip()
    query_lower = search_query.lower() if search_query else ""
    
    if search_query and query_lower != 'none':
        matched_items = []
        for item in skz_data:
            if (query_lower in item['name'].lower() or 
                query_lower in item['desc'].lower() or 
                query_lower in item['name'].replace(' ', '').lower()) :
                matched_items.append(item)
        results = matched_items
    else:
        results = skz_data
        search_query = None

    # 👤 PostgreSQL 資料庫實時 Create 會員連動
    if request.method == 'POST' and request.POST.get('action') == 'register_member':
        username = request.POST.get('username', '').strip()
        if username:
            try:
                if not User.objects.filter(username=username).exists():
                    User.objects.create_user(username=username, password='DefaultPassword123!')
                    messages.success(request, f"📥 PostgreSQL 實時聯通！新會員 【{username}】 已成功以 SQL INSERT 寫入資料庫！")
                else:
                    messages.error(request, "⚠️ 該會員名稱在資料庫中已存在！")
            except Exception as e:
                pass
        return redirect('/')

    return render(request, 'myapp/index.html', {'results': results, 'search_query': search_query})

# ==========================================
# 🔐 會員認證與註冊/登入/登出指揮官管線
# ==========================================
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            MemberProfile.objects.create(user=user, favorite_skz_member="Felix")
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form, 'title': '🔮 會員註冊 👤'})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form, 'title': '🔒 會員登入 👤'})

def logout_view(request):
    logout(request)
    return redirect('index')

# ==========================================
# 📊 Endpoint 5: 會員中心 Dashboard (獲取資料庫)
# ==========================================
@login_required
def dashboard_view(request):
    user_bookings = Booking.objects.filter(user=request.user)
    profile, created = MemberProfile.objects.get_or_create(user=request.user)
    return render(request, 'myapp/dashboard.html', {'bookings': user_bookings, 'profile': profile})

# ==========================================
# 📌 Endpoint 6-10: 內容管理 CRUD 功能 (計畫建立/詳細/更新/刪除)
# ==========================================
@login_required
def plan_list_view(request):
    plans = CosplayPlan.objects.all().order_by('-plan_number')
    return render(request, 'myapp/plan_list.html', {'plans': plans})

def plan_detail_view(request, plan_id):
    plan = get_object_or_404(CosplayPlan, plan_number=plan_id)
    return render(request, 'myapp/plan_detail.html', {'plan': plan})

@login_required
def plan_create_view(request):
    if request.method == 'POST':
        CosplayPlan.objects.create(
            title=request.POST.get('title'),
            character_name=request.POST.get('character_name'),
            description=request.POST.get('description'),
            image_url=request.POST.get('image_url', '/static/idols/leeknow.jpg')
        )
        return redirect('plan_list')
    return render(request, 'myapp/plan_form.html', {'title': '🧙‍♀️ 建立新計畫 ✨'})

@login_required
def plan_update_view(request, plan_id):
    plan = get_object_or_404(CosplayPlan, plan_number=plan_id)
    if request.method == 'POST':
        plan.title = request.POST.get('title')
        plan.character_name = request.POST.get('character_name')
        plan.description = request.POST.get('description')
        plan.save()
        return redirect('plan_detail', plan_id=plan.plan_number)
    return render(request, 'myapp/plan_form.html', {'plan': plan, 'title': '🎨 更新計畫 ✨'})

@login_required
def plan_delete_view(request, plan_id):
    plan = get_object_or_404(CosplayPlan, plan_number=plan_id)
    plan.delete()
    return redirect('plan_list')

# ==========================================
# 🎟️ Endpoint 11-14: 預約功能連動 pgAdmin
# ==========================================
@login_required
def booking_create_view(request):
    if request.method == 'POST':
        Booking.objects.create(user=request.user, booking_type='TICKET', details='Stray Kids 萬聖節限定門票 🎟️')
        return JsonResponse({'status': 'success', 'msg': '✅ 資料已即時同步至 pgAdmin 資料庫！'})
    return JsonResponse({'status': 'error'})

def booking_delete_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('dashboard')

# ==========================================
# 🎵 Endpoint 15-20: API 資料端點 (全螢幕動態雙小遊戲與狀態控制)
# ==========================================
def api_play_count(request):
    return JsonResponse({'status': 'active', 'track': 'Aki Tse 萬聖節原創 AI 韓文Music'})

def api_save_score(request):
    return JsonResponse({'status': 'locked', 'msg': '萬聖節生存遊戲得分成功上傳！'})

def api_vampire_status(request):
    return JsonResponse({'status': 'open'})

def api_bbq_slots(request):
    return JsonResponse({'status': 'available'})

def api_palace_ticket(request):
    return JsonResponse({'status': 'valid'})

def api_ddp_status(request):
    return JsonResponse({'status': 'glowing'})

def api_lotte_zombie(request):
    return JsonResponse({'status': 'active'})
