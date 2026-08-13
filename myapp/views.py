# ==================== 【請務必貼在 views.py 的最頂端第 1 行】 ====================
from django.shortcuts import render
from django.http import JsonResponse

# ==============================================================================
# 底下才是你原本寫的 def index_view(request): ...
# 請確保第 1 到 27 行長這樣（尾巴只有一個 }）：
def index_view(request):
    """最基礎的首頁功能，讓 urls.py 可以順利找到它"""
    from django.shortcuts import render
    return render(request, 'myapp/index.html')

skz_data = {
    'stray kids': {
        'name': 'Stray Kids (스트레이 키즈)',
        'img_url': '/static/skz_all.jpg',
        'desc': 'JYP 旗下的世界級男團！成員包括方燦、Lee Know、彰彬、鉉辰、HAN、Felix、昇玟、I.N，音樂充滿強烈中毒性！⚡'
    },
    'felix': {
        'name': 'Felix (필릭스)',
        'img_url': '/static/felix.jpg',
        'desc': '擁有反轉魅力的低音炮 Rapper，笑起來像天使一樣溫暖的龍馥小波卡！🐥'
    },
    'lee know': {
        'name': 'Lee Know (리노)',
        'img_url': '/static/idol7.jpg',
        'desc': '四次元魅力的舞蹈隊長，超級愛貓的貓咪大師！🐱'
    },
        'hyunjin': {
        'name': '鉉辰 (현진)',
        'img_url': '/static/hyunjin.jpg', # 確保你 static 資料夾有這張帥照
        'desc': 'Stray Kids 的視覺中心與主舞！舞台魅力爆棚，藝術感滿滿的當代藝術家王子！👑'
    },
    'bang chan': {
        'name': '方燦 (방찬 - Bang Chan)',
        'img_url': '/static/bangchan.jpg', # 確保 static 有他的照片
        'desc': 'Stray Kids 的偉大隊長與全能製作人！3RACHA 的核心成員，守護著團員與 STAY 的暖心大狼！🐺✨'
    },

    '萬聖節': {
        'name': '🎃 萬聖節限定夢幻計畫',
        'img_url': '/static/idol8.png',
        'desc': '走訪梨泰院、弘大商圈的萬聖節 Cosplay 狂歡夜，並到愛寶樂園或樂天世界體驗最刺激的殭屍大遊行！🧛'
    }
} # 👈 確保整段資料袋的結尾只有這一個大括號，沒有第 28 行了！
# ==================== 【請接著貼在第 29 行下方】 ====================

def search_view(request):
    """２. 搜尋功能：讓使用者輸入關鍵字後，能模糊比對出正確結果"""
    query = request.GET.get('q', '').lower()  # 轉小寫方便比對
    search_result = None
    
    if query:
        for key, value in skz_data.items():
            if key in query:
                search_result = value
                break
                
    # 請在第 42、43、44、45 行的「最前面」，各補上 4 個空格（或是選取這 4 行，按一下鍵盤的 Tab 鍵）：
    return render(request, 'myapp/index.html', {
                'search_result': search_result,
                'query': query,
            })



def random_plan_api(request):
    """３. 白星功能：每次被點擊時，都隨機抽 1 筆完美格式的夢幻計畫回傳"""
    import random
    from django.http import JsonResponse
    
    # 建立 20 筆完全標準、滿足前端檢查的完美 JSON 資料清單
    perfect_20_plans = []
    titles = [
        "① 首爾弘大 Cosplay 聖地巡禮", "② 萬聖節限定！SKZOO 快閃店", 
        "③ 漢江公園吃熱騰騰的泡麵", "④ 聖水洞探店與文青咖啡廳", 
        "⑤ Stray Kids 錄音室外幸運偶遇", "⑥ 東大門不夜城深夜購物狂歡", 
        "⑦ 景福宮穿韓服一日穿越劇", "⑧ 樂天世界萬聖節殭屍大遊行", 
        "⑨ 明洞小吃攤一路吃到飽", "⑩ 釜山海雲台看海聽海浪聲", 
        "⑪ 追隨 Lee Know 的貓咪咖啡廳", "⑫ 大邱烤腸一條街瘋狂美食客", 
        "⑬ 濟州島漢拿山橘子園採果樂", "⑭ 梨泰院異國風情狂歡萬聖夜", 
        "⑮ 三清洞散步尋找文藝雜貨店", "⑯ 仁川童話村夢幻拍照牆", 
        "⑰ N首爾塔鎖上情侶鎖看全景", "⑱ 廣藏市場生牛肉與生章魚挑戰", 
        "⑲ 追星必去 K-Star ROAD 熊熊打卡", "⑳ 坪和市場挖寶復古 Cosplay"
    ]
    
    for i in range(20):
        perfect_20_plans.append({
            "id": i + 1,
            "title": titles[i],
            "category": "Travel" if i % 2 == 0 else "K-Pop",
            "location": "首爾",
            "content": "探索充滿年輕活力的夢幻行程！✨",
            "name": titles[i],
            "fields": {
                "title": titles[i],
                "category": "Travel",
                "location": "首爾",
                "content": "探索充滿年輕活力的夢幻行程！✨"
            }
        })
        
    return JsonResponse(perfect_20_plans, safe=False)

# ==================== 【請貼在 views.py 的最底部】 ====================

def detail_view(request, item_id):
    """４. 詳細頁功能：讓 urls.py 可以順利找到它，避免後台報錯"""
    from django.shortcuts import render
    context = {"item_id": item_id, "type": "樣本資料項目"}
    return render(request, 'myapp/search_results.html', context)
