from flask import Flask, render_template_string

app = Flask(__name__)

# ==========================================
# 區域一：資料設定區 (最常改這裡)
# ==========================================
# 這裡控制你的按鈕要連去哪裡、顯示什麼字、什麼顏色
# 格式：{"name": "顯示文字", "url": "網址", "color": "按鈕背景色", "text_color": "文字顏色"},
links = [
    # 👇 第 1 顆按鈕：7-11 賣貨便
    {
        "name": "🛒 7-11 賣貨便 (運費優惠)", 
        "url": "https://myship.7-11.com.tw/seller/profile?id=GM2511258996885", 
        "color": "#fff",       # 白色背景
        "text_color": "#D87093" # 乾燥玫瑰紅文字
    },
    # 👇 第 2 顆按鈕：蝦皮
    {
        "name": "🛍️ 蝦皮賣場", 
        "url": "https://shopee.tw/beatrice726?categoryId=100016&entryPoint=ShopByPDP&itemId=58154888029", 
        "color": "#fff", 
        "text_color": "#EE4D2D" # 蝦皮橘紅文字
    },
    # 👇 第 3 顆按鈕：LINE 官方
    {
        "name": "💬 LINE 官方客服", 
        "url": "https://page.line.me/425ijwui", 
        "color": "#fff", 
        "text_color": "#06C755" # LINE 綠色文字
    },
    # 👇 第 4 顆按鈕：LINE 社群
    {
        "name": "🤫 Line 社群", 
        "url": "https://line.me/ti/g2/GoDc73jMMwXiIDyEnlKFYKbHZmH0OJsdUnb_1w?utm_source=invitation&utm_medium=link_copy&utm_campaign=default", 
        "color": "#fff", 
        "text_color": "#00B900" # 深綠色文字
    }, 
]

@app.route('/')
def home():
    # ==========================================
    # 區域二：網頁設計區 (CSS樣式)
    # ==========================================
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>M.TIDE 🌊 妳的自信浪潮</title> <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700;900&display=swap" rel="stylesheet">
        
        <style>
            /* 1. 整個網頁的背景 */
            body { 
                font-family: 'Noto Sans TC', sans-serif; /* 設定字體 */
                /* 👇 背景漸層色：如果要改顏色，改這裡的色碼 */
                background: linear-gradient(to top, #a18cd1 0%, #fbc2eb 100%); 
                min-height: 100vh;
                margin: 0;
                display: flex;             /* 讓內容物置中 */
                align-items: center;       /* 垂直置中 */
                justify-content: center;   /* 水平置中 */
            }

            /* 2. 中間那個毛玻璃卡片 */
            .container { 
                width: 90%;               /* 寬度佔螢幕 90% */
                max-width: 400px;         /* 最大不超過 400px (手機版剛好) */
                background: rgba(255, 255, 255, 0.25); /* 背景半透明白 */
                backdrop-filter: blur(10px);           /* 背景模糊特效 */
                -webkit-backdrop-filter: blur(10px);   /* 蘋果手機的模糊支援 */
                padding: 40px 30px;       /* 卡片內部的留白空間 */
                border-radius: 25px;      /* 卡片圓角程度 */
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15); /* 卡片陰影 */
                text-align: center;       /* 文字置中 */
                border: 1px solid rgba(255, 255, 255, 0.18); /* 卡片邊框線 */
            }

            /* 3. 主標題 (M.TIDE) */
            h1 { 
                color: #fff;              /* 文字白色 */
                margin-bottom: 10px;      /* 與下方文字的距離 */
                letter-spacing: 2px;      /* 字距 */
                text-shadow: 0 2px 5px rgba(0,0,0,0.2); /* 文字陰影 */
                font-size: 42px;          /* 👇 字體大小 (想要更大改這個數字) */
                font-weight: 900;         /* 字體粗細 (900是最粗) */
            }
            
            /* 4. 副標題/Slogan (妳的自信...) */
            p { 
                color: #fff; 
                margin-bottom: 40px;      /* 與下方按鈕的距離 */
                font-size: 20px;          /* 👇 字體大小 */
                font-weight: 700;         /* 粗體 */
                opacity: 1;
                text-shadow: 0 1px 3px rgba(0,0,0,0.2);
                line-height: 1.5;         /* 行高 */
            }

            /* 5. 按鈕樣式 (重點在這裡！) */
            .btn { 
                display: block; 
                width: 100%;              /* 按鈕寬度填滿卡片 */
                
                /* 👇👇👇【這裡控制按鈕大小】👇👇👇 */
                /* padding 代表「內距」，數字越大，按鈕越肥 */
                /* 18px 是上下高度，0 是左右寬度 */
                padding: 25px 0;          /* 建議把 18px 改成 25px 或 30px */

                margin: 15px 0;           /* 按鈕之間的距離 */
                text-decoration: none;    /* 去除超連結底線 */
                border-radius: 50px;      /* 按鈕圓角 (改成 0 就會變直角長方形) */
                font-weight: bold; 
                transition: 0.3s;         /* 動畫過渡時間 */
                box-shadow: 0 4px 15px rgba(0,0,0,0.1); /* 按鈕陰影 */
                
                /* 👇 按鈕內的文字大小 */
                font-size: 20px;          /* 建議配合 padding 一起放大，原本是 18px */
                letter-spacing: 0.5px;
            }
            
            /* 滑鼠移過去的特效 */
            .btn:hover { 
                transform: translateY(-3px); /* 往上浮起 */
                box-shadow: 0 6px 20px rgba(0,0,0,0.2); /* 陰影變深 */
            }
        </style>
    </head>
    
    <body>
        <div class="container">
            <h1>M.TIDE 🌊</h1>
            <p>妳的自信，隨浪潮而來。</p>
            
            {% for link in links %}
                <a href="{{ link.url }}" class="btn" style="background-color: {{ link.color }}; color: {{ link.text_color }};">
                    {{ link.name }}
                </a>
            {% endfor %}
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, links=links)

if __name__ == '__main__':
    app.run(debug=True)
