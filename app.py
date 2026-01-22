from flask import Flask, render_template_string

app = Flask(__name__)

# 👇 請在這裡修改成 M.TIDE 真正的連結
links = [
    {"name": "🛒 7-11 賣貨便 (運費優惠)", "url": "https://myship.7-11.com.tw/seller/profile?id=GM2511258996885", "color": "#E60012"},
    {"name": "🛍️ 蝦皮賣場", "url": "https://shopee.tw/beatrice726?categoryId=100016&entryPoint=ShopByPDP&itemId=58154888029", "color": "#EE4D2D"},
    {"name": "💬 LINE 官方客服", "url": "https://page.line.me/425ijwui", "color": "#06C755"},
    {"name": "🤫 Line 社群", "url": "https://line.me/ti/g2/GoDc73jMMwXiIDyEnlKFYKbHZmH0OJsdUnb_1w?utm_source=invitation&utm_medium=link_copy&utm_campaign=default", "color": "#00B900"}, 
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
            /* 背景設定：夢幻紫粉色漸層 */
            body { 
                font-family: 'Noto Sans TC', sans-serif; 
                background: linear-gradient(to top, #a18cd1 0%, #fbc2eb 100%); 
                min-height: 100vh;
                margin: 0;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            /* 卡片設定：毛玻璃效果 */
            .container { 
                width: 90%;
                max-width: 400px; 
                background: rgba(255, 255, 255, 0.25); 
                backdrop-filter: blur(10px); 
                -webkit-backdrop-filter: blur(10px);
                padding: 40px 30px; 
                border-radius: 25px; 
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15); 
                text-align: center;
                border: 1px solid rgba(255, 255, 255, 0.18);
            }

            /* 👇【標題改這裡】變大、變粗 */
            h1 { 
                color: #fff; 
                margin-bottom: 10px; 
                letter-spacing: 2px; 
                text-shadow: 0 2px 5px rgba(0,0,0,0.2); /* 增加陰影讓字更清楚 */
                font-size: 42px;  /* 字體放大 */
                font-weight: 900; /* 特粗體 */
            }
            
            /* 👇【Slogan 改這裡】變大、變粗 */
            p { 
                color: #fff; 
                margin-bottom: 40px; 
                font-size: 20px;  /* 字體放大 */
                font-weight: 700; /* 加粗 */
                opacity: 1;
                text-shadow: 0 1px 3px rgba(0,0,0,0.2); /* 增加陰影 */
                line-height: 1.5;
            }

            /* 按鈕樣式 */
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
                font-size: 18px; /* 按鈕文字也稍微放大 */
                letter-spacing: 0.5px;
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
