from flask import Flask, render_template, jsonify
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import threading
import time

app = Flask(__name__)

# ======================== موتور HamidCognition ========================
class HamidCognition:
    def __init__(self):
        self.P = 0.88
        self.S = 0.78
        self.T = 0.40
        self.history = []
    
    def step(self, pressure, novelty):
        P_change = 0.05 * pressure * (1 - self.T)
        self.P = min(max(self.P + P_change, 0.1), 0.95)
        
        S_change = 0.04 * novelty * (1 - abs(self.P - self.S))
        self.S = min(max(self.S + S_change, 0.1), 0.95)
        
        T_change = 0.03 * (self.S / (self.P + 1e-9)) * (1 + pressure)
        self.T = min(max(self.T + T_change, 0.1), 0.8)
        
        energy = (self.P * self.S) / (1.1 - self.T + 1e-9) * (1 - self.T / (self.P + self.S + 1e-9))
        
        if abs(self.P - self.S) < 0.15:
            phase = "RUPTURE_IMMINENT"
        elif self.T < 0.45:
            phase = "UNSTABLE_CREATIVITY"
        elif self.P > 0.85 and self.S > 0.8:
            phase = "SYNTHESIS_PEAK"
        else:
            phase = "STEADY_EXPLORATION"
        
        return {
            "P": round(self.P, 3),
            "S": round(self.S, 3),
            "T": round(self.T, 3),
            "energy": round(min(energy, 1.5), 3),
            "phase": phase,
            "jump_risk": round(min(1.0, abs(self.P - self.S) * 2.5), 3)
        }

# ======================== سیستم پیش‌بینی ========================
class HamidPlatform:
    def __init__(self):
        self.cognition = HamidCognition()
        self.latest_data = {
            "current_price": 1.04500,
            "pred_5min": 1.04500,
            "pred_10min": 1.04500,
            "pred_15min": 1.04500,
            "cognitive": self.cognition.step(0.5, 0.5),
            "timestamp": datetime.now().isoformat()
        }
    
    def update(self):
        while True:
            try:
                # دریافت داده واقعی EUR/USD
                ticker = yf.Ticker("EURUSD=X")
                df = ticker.history(period="1d", interval="1m")
                if len(df) > 0:
                    current = df['Close'].iloc[-1]
                else:
                    current = 1.04500 + np.random.normal(0, 0.0002)
                
                # تحلیل بازار
                returns = df['Close'].pct_change().dropna()
                pressure = min(1.0, returns.std() * 20)
                novelty = min(1.0, abs(returns.iloc[-1]) * 100)
                
                # به‌روزرسانی شناخت
                cognitive = self.cognition.step(pressure, novelty)
                
                # پیش‌بینی ساده + تعدیل شناختی
                base_trend = np.mean(returns.iloc[-10:])
                bias = cognitive["energy"] * (1 if base_trend > 0 else -1)
                
                pred_5 = current + bias * 0.0003
                pred_10 = current + bias * 0.0006
                pred_15 = current + bias * 0.0010
                
                self.latest_data = {
                    "current_price": round(current, 5),
                    "pred_5min": round(pred_5, 5),
                    "pred_10min": round(pred_10, 5),
                    "pred_15min": round(pred_15, 5),
                    "cognitive": cognitive,
                    "timestamp": datetime.now().strftime("%H:%M:%S")
                }
                
            except:
                pass
            
            time.sleep(10)  # هر ۱۰ ثانیه آپدیت

# شروع سیستم
platform = HamidPlatform()
threading.Thread(target=platform.update, daemon=True).start()

# ======================== روت‌ها ========================
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/data")
def api_data():
    return jsonify(platform.latest_data)

if __name__ == "__main__":
    print("🚀 پلتفرم HamidCognition فعال شد!")
    print("🌐 برو به: http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
