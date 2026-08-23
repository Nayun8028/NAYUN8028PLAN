from django.db import models
from django.contrib.auth.models import User

# 📊 模型 1：會員拓展資料（滿足阿Sir要求的用戶身份驗證系統，對接 pgAdmin）
class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, default="Aki 粉絲")
    favorite_skz_member = models.CharField(max_length=50, default="Felix")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# 📸 模型 2：20個或以上 Cosplay 夢幻旅遊計劃（完美包攬偶像、明洞烤肉餐廳、景福宮、安全管制提示等 20 個心血）
class CosplayPlan(models.Model):
    plan_number = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    character_name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Plan {self.plan_number}: {self.title}"

# 🎟️ 模型 3：K-Pop 演唱會門票與 Agoda 住宿機票預訂數據模型（純功課用途 CRUD）
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_type = models.CharField(max_length=20, default='TICKET')
    details = models.CharField(max_length=255, default='Stray Kids 萬聖節巡迴門票 🎟️')
    booking_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.booking_type}"
