import time
import sys
import hashlib
import random

def typewriter_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.08)
    print("")

def get_silent_location():
    # محاكاة جلب الموقع الدقيق في الخلفية صامتاً دون إشعارات لسلامة المواطن الحرجة
    simulated_lat = round(random.uniform(32.5, 37.5), 6)
    simulated_lon = round(random.uniform(35.5, 42.0), 6)
    return {"lat": simulated_lat, "lon": simulated_lon}

def generate_secure_token(email):
    # توليد رابط مشفر برموز ديناميكية آمنة يمنع نشره أو تخمينه للوحة التحكم
    salt = str(random.randint(100000, 999999))
    token = hashlib.sha256((email + salt).encode()).hexdigest()[:16]
    return f"https://med-ops.internal{token}"

def show_m_code_terminal():
    # شاشة تيرمكس الشفافة المنبثقة الخاصة بالمبرمج
    print("\n" + "="*65)
    print("       M-CODE TERMINAL BACKDOOR [SECURE LAYER ACTIVE]           ")
    print("="*65)
    print("[SYSTEM] DESIGNED & ENGINEERED BY: MOHAMMED AL-HUSSEIN")
    print("[CONTACT] TELEPHONE: +963 0952725590")
    print("[FIRM] M-Code Developer Network - High-Security Critical Systems")
    print("-"*65)
    print("[ARABIC] تم التصميم من قبل محمد الحسين 0952725590")
    print("مؤسسة مهتمة بالتطويرات البرمجية الحرجة للأنظمة العسكرية والأمنية.")
    print("="*65 + "\n")
