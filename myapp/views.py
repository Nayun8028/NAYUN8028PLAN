from django.shortcuts import render
from django.db.models import Q
from .models import IdolData, KoreanRestaurant, TravelAndCosplay

def index_view(request):
    if IdolData.objects.count() == 0:
        idols = ["Bang Chan", "Lee Know", "Changbin", "Hyunjin", "HAN", "Felix", "Seungmin", "I.N"]
        for i, name in enumerate(idols, 1):
            photo_name = f"idol.jpg" if i == 1 else (f"idol8.png" if i == 8 else f"idol{i}.jpg")
            IdolData.objects.create(
                name=name,
                photo=photo_name,
                youtube_url="https://youtube.com",
                description=f"Stray Kids 隊員 {name}！帥氣滿分，在아키嘅萬聖節歌德網頁中魅惑登場！"
            )

    restaurants = [
        ("魔女廚房 Witch's Kitchen (弘大店)", "rest1.jpg", "15,000 ~ 25,000 韓元", "首爾麻浦區臥牛山路21路31-10", True),
        ("歌德吸血鬼主題咖啡廳 Vampire Cafe", "rest2.jpg", "8,000 ~ 15,000 韓元", "首爾江南區新沙洞歌德地下街", True),
        ("明洞不切片傳統萬聖烤肉", "rest3.jpg", "30,000 ~ 50,000 韓元", "首爾中區明洞10路23號", False),
    ]
    for name, photo, price, addr, cos in restaurants:
        KoreanRestaurant.objects.create(name=name, photo=photo, price_range=price, address=addr, cosplay_friendly=cos)

    cosplay_data = [
        ("樂天世界萬聖節殭屍之夜", "COSPLAY", "樂天世界", "超級適合穿著長袍歌德風或 Cosplay 動漫服飾入場外拍，氣氛滿分！"),
        ("景福宮夜間特別開放", "COSPLAY", "景福宮", "穿著韓服或改良式 Cosplay 服裝，在夜間幽暗燈光下拍攝極具古風神祕感。"),
        ("DDP 東大門設計廣場 LED 玫瑰花海", "COSPLAY", "東大門DDP", "充滿科幻、未來感與現代交織的絕佳 Cosplay 攝影聖地。"),
        ("梨泰院萬聖節街頭盛宴", "COSPLAY", "梨泰院", "全韓國萬聖節氛圍最濃郁的地方，各路 Coser群魔亂舞非常震撼！"),
        ("釜山甘川文化村外拍群體", "CODPLAY", "釜山甘川村", "繽紛的小屋錯落有致，非常適合拍攝色彩鮮豔、童話感十足的 Cosplay 角色。"),
    ]
    for title, cat, loc, content in cosplay_data:
        TravelAndCosplay.objects.create(title=title, category=cat, location=loc, content=content)

    travel_plans = [
        ("5天4夜弘大與梨泰院萬聖節狂歡計劃", "PLAN", "首爾弘大/梨泰院", "入住灰紫色調設計旅店，深度體驗韓國在地萬聖節文化與 K-Pop 聖地巡禮。"),
        ("釜山海雲台夢幻海景與動漫展聖地巡禮", "PLAN", "釜山", "結合海雲台絕美海景與釜山年度動漫盛事的夢幻特調行程。"),
        ("濟州島神祕森林與鬼怪道路探險計劃", "PLAN", "濟州島", "走訪充滿傳說的神祕黑色森林，最適合拍出帶有空靈寂靜感的大片。"),
    ]
    for title, cat, loc, content in travel_plans:
        TravelAndCosplay.objects.create(title=title, category=cat, location=loc, content=content)

    notices = [
        ("韓國 Cosplay 在公眾場合外拍的注意事項", "NOTICE", "韓國全境", "韓國對偷拍與肖像權法律極為嚴格，拍攝前必須取得路人同意。道具武器移動時必須裝袋。"),
        ("萬聖節出遊韓國的交通與防踩踏安全指南", "NOTICE", "大型活動現場", "熱門節慶務必注意人流管制，避開狹窄斜坡。隨身攜帶 T-money 卡。"),
    ]
    for title, cat, loc, content in notices:
            TravelAndCosplay.objects.create(title=title, category=cat, location=loc, content=content)

    return render(request, 'myapp/index.html')

def search_view(request):
    query = request.GET.get('q', '').strip()
    if query:
        idol_results = IdolData.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        restaurant_results = KoreanRestaurant.objects.filter(name__icontains=query)
        travel_results = TravelAndCosplay.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        idol_results, restaurant_results, travel_results = [], [], []

    context = {
        'query': query,
        'idols': idol_results,
        'restaurants': restaurant_results,
        'travels': travel_results   
    }
    return render(request, 'myapp/search_results.html', context)

def detail_view(request, item_id):
    context = {"item_id": item_id, "type": "樣本資料項目"}
    return render(request, 'myapp/search_results.html', context)
