import psycopg2
import json

def aki_pure_psycopg2_export():
    print("🕵️‍♂️ 【Aki 最高權限：開始調用底層 psycopg2 驅動直連 PostgreSQL 資料庫...】")
    try:
        # 🔒 實時建立數據庫握手管線：精準連結 PostgreSQL 核心心臟
        connection = psycopg2.connect(
            user="postgres",
            password="DefaultPassword123!",
            host="127.0.0.1",
            port="5432",
            database="my_secure_zone"
        )
        cursor = connection.cursor()
        
        # 🚀 執行最高硬核純 SQL 密令查詢
        cursor.execute("SELECT username, email FROM auth_user;")
        records = cursor.fetchall()
        
        print(f"💥 成功讀取資料庫數據！總筆數：{len(records)}")
        
        cursor.close()
        connection.close()
        print("📥 【psycopg2 通訊管道關閉，數據大流動完璧歸趙！】")
        
    except Exception as error:
        print(f"❌ 資料庫連線失敗: {error}")

if __name__ == "__main__":
    aki_pure_psycopg2_export()
