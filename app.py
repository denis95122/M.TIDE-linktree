from flask import Flask, render_template_string

app = Flask(__name__)

# ==========================================
# 區域一：資料設定區 (已升級！可個別設定字體大小)
# ==========================================
# 格式：{"name": "文字", "url": "網址", "color": "背景色", "text_color": "文字色", "size": "字體大小"},
links = [
    # 👇 第 1 顆按鈕：7-11 (主打商品，所以我設定 25px 讓它特別大！)
    {
        "name": "🛒 7-11 賣貨便 (運費優惠)", 
        "url": "https://myship.7-11.com.tw/seller/profile?id=GM2511258996885", 
        "color": "#fff", 
        "text_color": "#D87093",
        "size": "25px"  # 👈 這裡控制這顆按鈕的字體大小
    },
    # 👇 第 2 顆按鈕：蝦皮 (設定 19px)
    {
        "name": "🛍️ 蝦皮賣場", 
        "url": "https://shopee.tw/beatrice726?categoryId=100016&entryPoint=ShopByPDP&itemId=58154888029", 
        "color": "#fff", 
        "text_color": "#EE4D2D",
        "size": "28px"
    },
    # 👇 第 3 顆按鈕：LINE 官方 (設定 19px)
    {
        "name": "💬 LINE 官方客服", 
        "url": "https://page.line.me/425ijwui", 
        "color": "#fff", 
        "text_color": "#06C755",
        "size": "25px"
    },
    # 👇 第 4 顆按鈕：LINE 社群 (設定 19px)
    {
        "name": "🤫 Line 社群", 
        "url": "https://line.me/ti/g2/GoDc73jMMwXiIDyEnlKFYKbHZmH0OJsdUnb_1w?utm_source=invitation&utm_medium=link_copy&utm_campaign=default", 
        "color": "#fff", 
        "text_color": "#00B900",
        "size": "25px"
    }, 
]

@app.route('/')
def home():
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>M.TIDE 🌊 妳的自信浪潮</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
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
                max-width: 350px;
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
                padding: 18px 0;   /* 這裡控制按鈕胖瘦 */
                margin: 15px 0;
                text-decoration: none;
                border-radius: 50px;
                font-weight: bold; 
                transition: 0.3s;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                letter-spacing: 0.5px;
                /* 注意：原本這裡有 font-size，現在我拿掉了，改由下面 HTML 個別控制 */
            }
            
            .btn:hover { 
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(0,0,0,0.2);
            }
        </style>
    </head>
    
    <body>
        <div class="container">
            <h1>M.TIDE 🌊</h1>
            <p>妳的自信，隨浪潮而來。</p>
            
            {% for link in links %}
                <a href="{{ link.url }}" class="btn" style="background-color: {{ link.color }}; color: {{ link.text_color }}; font-size: {{ link.size }};">
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
