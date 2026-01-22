from flask import Flask, render_template_string

app = Flask(__name__)

# 👇 請在這裡修改成 M.TIDE 真正的連結
links = [
    {"name": "🛒 7-11 賣貨便 (運費優惠)", "url": "https://myship.7-11.com.tw/seller/profile?id=GM2511258996885", "color": "#E60012"},
    {"name": "🛍️ 蝦皮賣場", "url": "https://shopee.tw/beatrice726?categoryId=100016&entryPoint=ShopByPDP&itemId=58154888029", "color": "#EE4D2D"},
    {"name": "💬 LINE 官方客服", "url": "https://page.line.me/425ijwui", "color": "#06C755"},
    {"name": "🤫 VIP 秘密社群", "url": "https://line.me/ti/g2/GoDc73jMMwXiIDyEnlKFYKbHZmH0OJsdUnb_1w?utm_source=invitation&utm_medium=link_copy&utm_campaign=default", "color": "#00B900"}, 
]

@app.route('/')
def home():
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>M.TIDE 傳送門</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: sans-serif; background-color: #f8f9fa; text-align: center; padding: 20px; color: #333; }
            .container { max-width: 400px; margin: 0 auto; background: white; padding: 40px 30px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); }
            h1 { font-size: 24px; margin-bottom: 5px; letter-spacing: 1px; }
            p { color: #888; margin-bottom: 30px; font-size: 14px; }
            .btn { display: block; width: 100%; padding: 16px 0; margin: 12px 0; color: white; text-decoration: none; border-radius: 50px; font-weight: bold; transition: 0.3s; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            .btn:hover { opacity: 0.9; transform: translateY(-2px); box-shadow: 0 6px 12px rgba(0,0,0,0.15); }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>M.TIDE 🌊</h1>
            <p>妳的自信，隨浪潮而來。</p>
            {% for link in links %}
                <a href="{{ link.url }}" class="btn" style="background-color: {{ link.color }};">
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
