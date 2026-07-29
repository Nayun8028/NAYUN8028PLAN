from django.db import models

# 模型 1：Stray Kids 偶像資料模型
class IdolData(models.Model):
    name = models.CharField(max_length=100) # 偶像團員名字
    photo = models.CharField(max_length=200) # 圖片路徑
    youtube_url = models.URLField() # YouTube 歌曲分享連結
    description = models.TextField() # 偶像介紹資料

    def __str__(self):
        return self.name

# 模型 2：韓國特色餐廳模型（滿足你的①要求：圖片，價錢及地址）
class KoreanRestaurant(models.Model):
    name = models.CharField(max_length=150) # 餐廳名稱
    photo = models.CharField(max_length=200) # 餐廳圖片路徑
    price_range = models.CharField(max_length=50) # 價錢範圍 (例如 15,000~30,000 韓元)
    address = models.TextField() # 餐廳地址
    cosplay_friendly = models.BooleanField(default=True) # 是否適合 Cosplay 模式

    def __str__(self):
        return self.name

# 模型 3：韓國夢幻旅遊與 Cosplay 出遊筆記模型（包含注意事項）
class TravelAndCosplay(models.Model):
    CATEGORY_CHOICES = [
    ('COSPLAY', '韓國 CosPlay 地點分享'),
    ('PLAN', '韓國特色夢幻旅遊計劃'),
    ('NOTICE', '韓國旅遊注意事項出遊分享'),
    ]
    title = models.CharField(max_length=200) # 標題
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES) # 分類
    location = models.CharField(max_length=150, blank=True) # 地點
    photo = models.CharField(max_length=200, blank=True) # 相關圖片路徑
    content = models.TextField() # 計劃或注意事項詳細內容

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"