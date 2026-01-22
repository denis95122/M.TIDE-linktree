import json
import os
from datetime import datetime
from flask import Flask, render_template_string, redirect, request

app = Flask(__name__)

# ==========================================
# 💾 核心數據庫設定
# ==========================================
DATA_FILE = 'mtide_analytics.json'

def log_event(event_type, link_id=None):
    data = []
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except:
            data = []
            
    new_record = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": event_type, 
        "id": link_id
    }
    data.append(new_record)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def get_analytics_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def reset_analytics_data():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

# ==========================================
# 區域一：連結設定區 (已修正！把優惠加回來了)
# ==========================================
links = [
    {
        "id": "711", 
        # 👇 修正重點：把 "(運費優惠)" 加回來了！這是吸引點擊的關鍵！
        "name": "🛒 7-11 賣貨便 (運費優惠)", 
        "url": "https://myship.7-11.com.tw/seller/profile?id=GM2511258996885", 
        "color": "#fff", "text_color": "#D87093", "size": "25px", "highlight": True
    },
    {
        "id": "shopee",
        "name": "🛍️ 蝦皮賣場", 
        "url": "https://shopee.tw/beatrice726?categoryId=100016&entryPoint=ShopByPDP&itemId=58154888029", 
        "color": "#fff", "text_color": "#EE4D2D", "size": "28px", "highlight": False
    },
    {
        "id": "line_service",
        "name": "💬 LINE 官方客服", 
        "url": "https://page.line.me/425ijwui", 
        "color": "#fff", "text_color": "#06C755", "size": "25px", "highlight": False
    },
    {
        "id": "line_group",
        "name": "🤫 Line 社群", 
        "url": "https://line.me/ti/g2/GoDc73jMMwXiIDyEnlKFYKbHZmH0OJsdUnb_1w", 
        "color": "#fff", "text_color": "#00B900", "size": "25px", "highlight": False
    }, 
]

link_map = {link['id']: link['url'] for link in links}

# ==========================================
# 區域二：前台路由
# ==========================================
@app.route('/')
def home():
    log_event('view')
    html_template = """
    <!DOCTYPE html>
    <html lang="zh-TW">
    <head>
        <meta charset="UTF-8">
        <title>M.TIDE 🌊 妳的自信浪潮</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta property="og:title" content="M.TIDE 🌊 妳的自信浪潮">
        <meta property="og:description" content="專為女性設計的包包品牌，展現妳的自信與優雅。">
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700;900&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Noto Sans TC', sans-serif; background: linear-gradient(to top, #a18cd1 0%, #fbc2eb 100%); min-height: 100vh; margin: 0; display: flex; align-items: center; justify-content: center; }
            .container { width: 90%; max-width: 400px; background: rgba(255, 255, 255, 0.25); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); padding: 40px 30px; border-radius: 25px; box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15); text-align: center; border: 1px solid rgba(255, 255, 255, 0.18); }
            h1 { color: #fff; margin-bottom: 10px; letter-spacing: 2px; text-shadow: 0 2px 5px rgba(0,0,0,0.2); font-size: 42px; font-weight: 900; }
            p { color: #fff; margin-bottom: 40px; font-size: 20px; font-weight: 700; opacity: 1; text-shadow: 0 1px 3px rgba(0,0,0,0.2); line-height: 1.5; }
            .btn { display: block; width: 100%; padding: 18px 0; margin: 15px 0; text-decoration: none; border-radius: 50px; font-weight: bold; transition: 0.3s; box-shadow: 0 4px 15px rgba(0,0,0,0.1); letter-spacing: 0.5px; }
            .btn:hover { transform: translateY(-3px); box-shadow: 0 6px 20px rgba(0,0,0,0.2); }
            @keyframes pulse { 0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.7); } 70% { transform: scale(1.02); box-shadow: 0 0 0 10px rgba(255, 255, 255, 0); } 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); } }
            .btn-highlight { animation: pulse 2s infinite; border: 2px solid rgba(255,255,255,0.8); position: relative; }
            .footer { margin-top: 50px; font-size: 13px; color: rgba(255,255,255,0.8); letter-spacing: 1px; font-weight: 500; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>M.TIDE 🌊</h1>
            <p>妳的自信，隨浪潮而來。</p>
            {% for link in links %}
                <a href="/go/{{ link.id }}" class="btn {% if link.highlight %}btn-highlight{% endif %}" style="background-color: {{ link.color }}; color: {{ link.text_color }}; font-size: {{ link.size }};">{{ link.name }}</a>
            {% endfor %}
            <div class="footer">© 2026 M.TIDE Official</div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, links=links)

@app.route('/go/<link_id>')
def go(link_id):
    if link_id not in link_map: return redirect('/')
    log_event('click', link_id)
    return redirect(link_map[link_id])

@app.route('/reset', methods=['POST'])
def reset_data():
    reset_analytics_data()
    return redirect('/dashboard')

# ==========================================
# 區域三：數據戰情室
# ==========================================
@app.route('/dashboard')
def dashboard():
    raw_data = get_analytics_data()
    
    total_views = 0
    total_clicks = 0
    click_stats = {link['id']: {'name': link['name'], 'count': 0, 'color': link['text_color']} for link in links}
    hours = [f"{i:02d}:00" for i in range(24)]
    hour_counts = {h: 0 for h in hours}
    
    for record in raw_data:
        if record['type'] == 'view':
            total_views += 1
        elif record['type'] == 'click':
            total_clicks += 1
            if record['id'] in click_stats:
                click_stats[record['id']]['count'] += 1
        try:
            h = record['time'].split(' ')[1].split(':')[0] + ":00"
            if h in hour_counts: hour_counts[h] += 1
        except: pass

    bar_data = [hour_counts[h] for h in hours]
    pie_labels = [stat['name'] for stat in click_stats.values()]
    pie_data = [stat['count'] for stat in click_stats.values()]
    pie_colors = [stat['color'] for stat in click_stats.values()]
    conversion_rate = 0
    if total_views > 0: conversion_rate = round((total_clicks / total_views) * 100, 1)

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>M.TIDE 戰情室</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700;900&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Noto Sans TC', sans-serif; padding: 20px; background: #f0f2f5; color: #333; max-width: 800px; margin: 0 auto; }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { color: #D87093; margin: 0; font-size: 28px; }
            .kpi-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin-bottom: 25px; }
            .kpi-card { background: white; padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
            .kpi-num { font-size: 32px; font-weight: 900; color: #333; margin: 5px 0; }
            .kpi-label { font-size: 14px; color: #888; font-weight: bold; }
            .section-title { font-size: 18px; font-weight: bold; margin: 30px 0 15px; border-left: 5px solid #D87093; padding-left: 10px; }
            .channel-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 15px; margin-bottom: 20px; }
            .channel-card { background: white; padding: 15px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); border-left: 5px solid #ccc; display: flex; flex-direction: column; justify-content: center; }
            .channel-name { font-size: 14px; color: #666; font-weight: bold; margin-bottom: 5px; }
            .channel-count { font-size: 24px; font-weight: 900; color: #333; }
            .chart-box { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); margin-bottom: 20px; }
            .btn-reset { display: block; width: 100%; max-width: 200px; margin: 50px auto 20px; padding: 10px; background: white; color: #ff4d4f; border: 1px solid #ff4d4f; border-radius: 50px; cursor: pointer; font-weight: bold; transition: 0.3s; }
            .btn-reset:hover { background: #ff4d4f; color: white; }
            .btn-back { display: block; text-align: center; margin-top: 20px; color: #888; text-decoration: none; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🌊 M.TIDE 數據中心</h1>
            <p>即時監控品牌流量</p>
        </div>

        <div class="kpi-grid">
            <div class="kpi-card"><div class="kpi-label">👁️ 累積瀏覽</div><div class="kpi-num">{{ total_views }}</div></div>
            <div class="kpi-card"><div class="kpi-label">👆 累積點擊</div><div class="kpi-num">{{ total_clicks }}</div></div>
            <div class="kpi-card"><div class="kpi-label">🔥 轉換率</div><div class="kpi-num" style="color: #D87093;">{{ conversion_rate }}%</div></div>
        </div>

        <div class="section-title">📦 通路點擊排行</div>
        <div class="channel-grid">
            {% for stat in click_stats.values() %}
            <div class="channel-card" style="border-left-color: {{ stat.color }}">
                <div class="channel-name">{{ stat.name }}</div>
                <div class="channel-count">{{ stat.count }} 人</div>
            </div>
            {% endfor %}
        </div>

        <div class="section-title">📊 佔比分析</div>
        <div class="chart-box"><canvas id="pieChart" style="max-height: 250px;"></canvas></div>

        <div class="section-title">🕒 活躍時段</div>
        <div class="chart-box"><canvas id="barChart"></canvas></div>

        <form action="/reset" method="POST" onsubmit="return confirm('確定要清空所有數據嗎？這個動作無法復原喔！');">
            <button type="submit" class="btn-reset">🗑️ 清空所有數據 (重製)</button>
        </form>

        <a href="/" class="btn-back">返回網站首頁</a>

        <script>
            new Chart(document.getElementById('pieChart'), {
                type: 'doughnut',
                data: { labels: {{ pie_labels | tojson }}, datasets: [{ data: {{ pie_data | tojson }}, backgroundColor: {{ pie_colors | tojson }}, borderWidth: 0 }] },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'right' } } }
            });
            new Chart(document.getElementById('barChart'), {
                type: 'bar',
                data: { labels: {{ hours | tojson }}, datasets: [{ label: '活躍人次', data: {{ bar_data | tojson }}, backgroundColor: '#D87093', borderRadius: 4 }] },
                options: { responsive: true, scales: { y: { beginAtZero: true }, x: { grid: { display: false } } }, plugins: { legend: { display: false } } }
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html, 
                                  total_views=total_views, total_clicks=total_clicks, conversion_rate=conversion_rate,
                                  click_stats=click_stats, pie_labels=pie_labels, pie_data=pie_data, pie_colors=pie_colors,
                                  hours=hours, bar_data=bar_data)

if __name__ == '__main__':
    app.run(debug=True)
