from flask import Flask, render_template_string

app = Flask(__name__)

# ==========================================
# 區域一：資料設定區
# ==========================================
links = [
    # 👇 第 1 顆按鈕：7-11 (主打商品)
    {
        "name": "🛒 7-11 賣貨便 (運費優惠)", 
        "url": "https://myship.7-11.com.tw/seller/profile?id=GM2511258996885", 
        "color": "#fff", 
        "text_color": "#D87093",
        "size": "25px",   # 字體大小
        "highlight": True # ✨ 特效開關
    },
    # 👇 第 2 顆按鈕：蝦皮
    {
        "name": "🛍️ 蝦皮賣場", 
        "url": "https://shopee.tw/beatrice726?categoryId=100016&entryPoint=ShopByPDP&itemId=58154888029", 
        "color": "#fff", 
        "text_color": "#EE4D2D",
        "size": "28px",
        "highlight": False
    },
    # 👇 第 3 顆按鈕：LINE 官方
    {
        "name": "💬 LINE 官方客服", 
        "url": "https://page.line.me/425ijwui", 
        "color": "#fff", 
        "text_color": "#06C755",
        "size": "25px",
        "highlight": False
    },
    # 👇 第 4 顆按鈕：LINE 社群
    {
        "name": "🤫 Line 社群", 
        "url": "https://line.me/ti/g2/GoDc73jMMwXiIDyEnlKFYKbHZmH0OJsdUnb_1w?utm_source=invitation&utm_medium=link_copy&utm_campaign=default", 
        "color": "#fff", 
        "text_color": "#00B900",
        "size": "25px",
        "highlight": False
    }, 
]

@app.route('/')
def home():
    html_template = """
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>M.TIDE 🌊 妳的自信浪潮</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        
        <meta property="og:title" content="M.TIDE 🌊 妳的自信浪潮">
        <meta property="og:description" content="專為女性設計的包包品牌，展現妳的自信與優雅。">
        <meta property="og:image" content="">

        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700;900&display=swap" rel="stylesheet">
        
        <style>
            /* 1. 整個網頁的背景 */
            body { 
                font-family: 'Noto Sans TC', sans-serif;
                background: linear-gradient(to top, #a18cd1 0%, #fbc2eb 100%); 
                min-height: 100vh;
                margin: 0;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            /* 2. 中間那個毛玻璃卡片 */
            .container { 
                width: 90%;
                
                /* 👇 修改建議：原本 350px，改為 400px 讓手機視覺更寬敞大器 */
                max-width: 400px;
                
                /* 保持 0.25 微透明質感 */
                background: rgba(255, 255, 255, 0.25);
                
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                padding: 40px 30px;
                border-radius: 25px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
                text-align: center;
                border: 1px solid rgba(255, 255, 255, 0.18);
            }

            /* 3. 主標題 (M.TIDE) */
            h1 { 
                color: #fff;
                margin-bottom: 10px;
                letter-spacing: 2px;
                text-shadow: 0 2px 5px rgba(0,0,0,0.2);
                font-size: 42px;
                font-weight: 900;
            }
            
            /* 4. 副標題/Slogan */
            p { 
                color: #fff; 
                margin-bottom: 40px;
                font-size: 20px;
                font-weight: 700;
                opacity: 1;
                text-shadow: 0 1px 3px rgba(0,0,0,0.2);
                line-height: 1.5;
            }

            /* 5. 按鈕樣式 */
            .btn { 
                display: block; 
                width: 100%;
                padding: 18px 0;   
                margin: 15px 0;
                text-decoration: none;
                border-radius: 50px;
                font-weight: bold; 
                transition: 0.3s;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                letter-spacing: 0.5px;
            }
            
            .btn:hover { 
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(0,0,0,0.2);
            }

            /* ✨ 呼吸燈動畫 */
            @keyframes pulse {
                0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.7); }
                70% { transform: scale(1.02); box-shadow: 0 0 0 10px rgba(255, 255, 255, 0); }
                100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); }
            }

            .btn-highlight {
                animation: pulse 2s infinite;
                border: 2px solid rgba(255,255,255,0.8);
                position: relative;
            }
            
            /* 👇 新增：版權宣告的樣式 */
            .footer {
                margin-top: 50px;           /* 與上方按鈕拉開距離 */
                font-size: 13px;            /* 小一點的字 */
                color: rgba(255,255,255,0.8); /* 半透明白色 */
                letter-spacing: 1px;        /* 字元間距加大，比較有精品感 */
                font-weight: 500;
            }
        </style>
    </head>
    
    <body>
        <div class="container">
            <h1>M.TIDE 🌊</h1>
            <p>妳的自信，隨浪潮而來。</p>
            
            {% for link in links %}
                <a href="{{ link.url }}" 
                   class="btn {% if link.highlight %}btn-highlight{% endif %}" 
                   style="background-color: {{ link.color }}; color: {{ link.text_color }}; font-size: {{ link.size }};">
                    {{ link.name }}
                </a>
            {% endfor %}
            
            <div class="footer">
                © 2026 M.TIDE Official
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, links=links)

if __name__ == '__main__':
    app.run(debug=True)
