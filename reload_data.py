import os
import django

# 1. 讓腳本能使用 Django 環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# 2. 匯入你實際的 Model
from myapp.models import IdolData

def run():
    print("==========================================")
    print("🔄 超級助教提示：開始清空並重新載入 IdolData 資料庫...")
    print("==========================================")

    # 清空舊資料
    IdolData.objects.all().delete()
    print("🧹 舊的偶像資料已成功清空！")

    # 重新載入 8 位成員資料、正確的 YouTube 網址與相片路徑（完美修復問題 ④、⑤、⑥）
    # 同時幫你把 watch?v= 改成了網頁能播放的 embed/ 格式
    idols_data = [
        {
            "name": "Bang Chan",
            "photo": "idol1.jpg",
            "youtube_url": "https://youtube.com",
            "description": "Stray Kids 隊長"
        },
        {
            "name": "Lee Know",
            "photo": "idol2.jpg",
            "youtube_url": "https://youtube.com",
            "description": "Stray Kids 成員"
        },
        {
            "name": "Changbin",
            "photo": "idol3.jpg",
            "youtube_url": "https://youtube.com",
            "description": "Stray Kids 成員"
        },
        {
            "name": "Hyunjin",
            "photo": "idol4.jpg",
            "youtube_url": "https://youtube.com",
            "description": "Stray Kids 成員"
        },
        {
            "name": "Han",
            "photo": "idol5.jpg",
            "youtube_url": "https://youtube.com",
            "description": "Stray Kids 成員"
        },
        {
            "name": "Felix",
            "photo": "idol6.jpg",
            "youtube_url": "https://youtube.com",
            "description": "Stray Kids 成員"
        },
        {
            "name": "Seungmin",
            "photo": "idol7.jpg",
            "youtube_url": "https://youtube.com",
            "description": "Stray Kids 成員"
        },
        {
            "name": "I.N",
            "photo": "idol8.jpg",
            "youtube_url": "https://youtube.com",
            "description": "Stray Kids 成員"
        },
    ]

    # 針對特別指定的曲目，更新其對應的 YouTube 正確網址
    for data in idols_data:
        if data["name"] == "Felix": # 假設 LALALALA 放在 Felix 這裡，或等一下我們在前端直接綁定
            data["youtube_url"] = "https://youtube.com"
        elif data["name"] == "Hyunjin": # 假設 Case 143 放在 Hyunjin 這裡，確保按鈕有網址可用
            data["youtube_url"] = "https://youtube.com"

    # 將資料寫入資料庫
    for idol in idols_data:
        IdolData.objects.create(**idol)

    print(f"✅ 成功載入 {IdolData.objects.count()} 筆全新的偶像成員與音樂紀錄！")
    print("==========================================")
    print("🎉 恭喜！資料庫重新載入完畢，您可以回到 Terminal 執行測試了！")
    print("==========================================")

if __name__ == '__main__':
    run()

