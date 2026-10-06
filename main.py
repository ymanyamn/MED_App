import sys
import random
import hashlib
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

# الألوان الرسمية المعتمدة للتطبيق
COLOR_BG = "#0d1117"          # الخلفية الداكنة العميقة للأجهزة
COLOR_PRIMARY = "#1b4332"     # الأخضر العسكري الطاغي للدفاع المدني
COLOR_CARD = "#f4f1de"        # الأبيض السكري للبطاقات والقوائم
COLOR_TEXT_DARK = "#2b2b2b"   # لون النصوص داخل البطاقات السكرية
COLOR_ALERT = "#e63946"       # الأحمر التحذيري الحرج للبلاغات

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # واجهة المواطن الرئيسية
        layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        
        # الشعار والاسم العالي
        layout.add_widget(Label(text="MED", font_size='32sp', bold=True, color=get_color_from_hex("#ffffff"), size_hint_y=0.15))
        
        # تأثير الآلة الكاتبة الافتتاحي المطور
        self.lbl_slogan = Label(text="", font_size='14sp', color=get_color_from_hex("#00ffcc"), size_hint_y=0.05)
        layout.add_widget(self.lbl_slogan)
        self.full_text = "رجال الدفاع المدني معك أينما تكون"
        self.index = 0
        Clock.schedule_interval(self.typewriter, 0.08)
        
        # زر الإبلاغ عن حالة طوارئ الكبير المركزي
        btn_alert = Button(text="🚨 إبلاغ عن حالة طوارئ 🚨", font_size='20sp', bold=True,
                           background_color=get_color_from_hex(COLOR_ALERT), size_hint_y=0.25)
        btn_alert.bind(on_press=self.go_citizen)
        layout.add_widget(btn_alert)
        
        # شبكة الخدمات كبطاقات مربعة
        grid = GridLayout(cols=2, spacing=10, size_hint_y=0.45)
        
        btn_guide = Button(text="📋 إرشادات الإسعاف", background_color=get_color_from_hex(COLOR_PRIMARY))
        btn_news = Button(text="📢 أحدث الأخبار", background_color=get_color_from_hex(COLOR_PRIMARY))
        btn_train = Button(text="👥 التدريب المجتمعي", background_color=get_color_from_hex(COLOR_PRIMARY))
        btn_ops = Button(text="⚙️ العمليات والإدارة", background_color=get_color_from_hex("#333333"))
        
        btn_ops.bind(on_press=self.go_gateway)
        
        grid.add_widget(btn_guide)
        grid.add_widget(btn_news)
        grid.add_widget(btn_train)
        grid.add_widget(btn_ops)
        layout.add_widget(grid)
        
        # عبارة معلومات المبرمج بالأسفل (M-Code Terminal)
        btn_mcode = Button(text="ℹ️ معلومات المبرمج M-Code", size_hint_y=0.1, background_color=get_color_from_hex("#121212"))
        btn_mcode.bind(on_press=self.go_mcode)
        layout.add_widget(btn_mcode)
        
        self.add_widget(layout)

    def typewriter(self, dt):
        if self.index < len(self.full_text):
            self.lbl_slogan.text += self.full_text[self.index]
            self.index += 1
            return True
        return False

    def go_citizen(self, instance): self.manager.current = 'citizen'
    def go_gateway(self, instance): self.manager.current = 'gateway'
    def go_mcode(self, instance): self.manager.current = 'mcode'

class GatewayScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        layout.add_widget(Label(text="🔒 بوابة الدخول الآمنة للأنظمة", font_size='22sp', bold=True))
        
        self.txt_email = TextInput(hint_text="أدخل بريدك الإلكتروني المعتمد", multiline=False, size_hint_y=0.15)
        layout.add_widget(self.txt_email)
        
        btn_verify = Button(text="التحقق والدخول للمحطة", background_color=get_color_from_hex(COLOR_PRIMARY), size_hint_y=0.15)
        btn_verify.bind(on_press=self.verify_access)
        layout.add_widget(btn_verify)
        
        self.lbl_error = Label(text="", color=get_color_from_hex(COLOR_ALERT), size_hint_y=0.1)
        layout.add_widget(self.lbl_error)
        
        btn_back = Button(text="عودة للخلف", size_hint_y=0.15, background_color=get_color_from_hex("#444444"))
        btn_back.bind(on_press=self.back)
        layout.add_widget(btn_back)
        self.add_widget(layout)

    def verify_access(self, instance):
        if self.txt_email.text == "redmimhmdov@gmail.com":
            self.lbl_error.text = ""
            self.manager.current = 'admin_dashboard'
        elif "center" in self.txt_email.text:
            self.lbl_error.text = ""
            self.manager.current = 'station_ops'
        else:
            self.lbl_error.text = "❌ البريد غير مسجل بقاعدة عمليات الدفاع المدني!"

    def back(self, instance): self.manager.current = 'menu'

class CitizenScreen(Screen):
    def on_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        layout.add_widget(Label(text="📍 خريطة الطوارئ الحية (سوريا)", font_size='22sp', bold=True, color=get_color_from_hex("#00ffcc"), size_hint_y=0.1))
        
        sim_map = BoxLayout(orientation='vertical', padding=10, size_hint_y=0.6)
        sim_map.add_widget(Label(text="[ 🔴 نقطة حمراء نشطة: موقع البلاغ الحالي الحرج ]\n[ 🔵 نقطة زرقاء: موقع أقرب مركز دفاع مدني متاح ]",
                                 font_size='14sp', color=get_color_from_hex("#ffffff")))
        layout.add_widget(sim_map)
        
        layout.add_widget(Label(text="⏳ تم نقل وإرسال الإحداثيات بالخلفية صامتاً لغرفة العمليات المركزية...", font_size='12sp', color=get_color_from_hex(COLOR_CARD)))
        
        btn_back = Button(text="إغلاق وإلغاء البلاغ", size_hint_y=0.15, background_color=get_color_from_hex(COLOR_ALERT))
        btn_back.bind(on_press=self.back)
        layout.add_widget(btn_back)
        self.add_widget(layout)
    def back(self, instance): self.manager.current = 'menu'

class StationOpsScreen(Screen):
    def on_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        layout.add_widget(Label(text="⚙️ سحابة عمليات المحطة الفرعية", font_size='20sp', bold=True, size_hint_y=0.1))
        
        card = BoxLayout(orientation='vertical', padding=10, spacing=5, size_hint_y=0.7)
        card.add_widget(Label(text="حالة المحطة الحالية: نشطة وجاهزة", font_size='16sp', color=get_color_from_hex("#00ff00"), bold=True))
        card.add_widget(Label(text="• الفرق المناوبة: الفوج الأول (إطفاء + إنقاذ)", font_size='14sp', color=get_color_from_hex(COLOR_CARD)))
        card.add_widget(Label(text="• توافر المعدات والمجنزرات: متوفرة بالكامل", font_size='14sp', color=get_color_from_hex(COLOR_CARD)))
        card.add_widget(Label(text="[المهمة الحالية]: تم الاستلام ➔ جاري التوجه للموقع", font_size='14sp', color=get_color_from_hex("#ffcc00")))
        layout.add_widget(card)
        
        btn_finish = Button(text="اضغط لإنهاء المهمة وإرسال التقرير", background_color=get_color_from_hex(COLOR_PRIMARY), size_hint_y=0.1)
        layout.add_widget(btn_finish)
        
        btn_back = Button(text="خروج وتسجيل مغادرة", size_hint_y=0.1, background_color=get_color_from_hex("#444444"))
        btn_back.bind(on_press=self.back)
        layout.add_widget(btn_back)
        self.add_widget(layout)
    def back(self, instance): self.manager.current = 'menu'

class AdminDashboardScreen(Screen):
    def on_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        layout.add_widget(Label(text="📊 لوحة التحكم الإدارية المركزية", font_size='22sp', bold=True, color=get_color_from_hex("#00ffcc"), size_hint_y=0.1))
        stats_grid = GridLayout(cols=3, spacing=5, size_hint_y=0.2)
        stats_grid.add_widget(Label(text="البلاغات الكلية\n", bold=True, color=get_color_from_hex("#ffffff")))
        stats_grid.add_widget(Label(text="حالة الحوادث\n", bold=True, color=get_color_from_hex("#ffcc00")))
        stats_grid.add_widget(Label(text="مراكز الانتشار\n", bold=True, color=get_color_from_hex("#00ff00")))
        layout.add_widget(stats_grid)
        
        # خيارات التحكم الشاملة بالخريطة والمراكز
        layout.add_widget(Label(text="🔧 صلاحيات الإدارة المتاحة للحساب:", font_size='14sp', size_hint_y=0.05))
        
        ops_grid = GridLayout(cols=2, spacing=10, size_hint_y=0.5)
        ops_grid.add_widget(Button(text="➕ إضافة مركز جديد", background_color=get_color_from_hex(COLOR_PRIMARY)))
        ops_grid.add_widget(Button(text="❌ حذف / تعديل مركز", background_color=get_color_from_hex(COLOR_ALERT)))
        ops_grid.add_widget(Button(text="🗺️ نشر مركز على الخريطة", background_color=get_color_from_hex(COLOR_PRIMARY)))
        ops_grid.add_widget(Button(text="📄 تفاصيل التقارير والمنجز", background_color=get_color_from_hex("#333333")))
        layout.add_widget(ops_grid)
        
        btn_back = Button(text="تسجيل خروج آمن", size_hint_y=0.15, background_color=get_color_from_hex("#444444"))
        btn_back.bind(on_press=self.back)
        layout.add_widget(btn_back)
        self.add_widget(layout)
    def back(self, instance): self.manager.current = 'menu'

class MCodeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # نافذة تيرمكس المنبثقة الشفافة للمبرمج
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        terminal_text = (
            "====================================================\n"
            "       M-CODE TERMINAL BACKDOOR [SECURE LAYER]      \n"
            "====================================================\n"
            "[SYSTEM] DESIGNED & ENGINEERED BY: MOHAMMED AL-HUSSEIN\n"
            "[CONTACT] TELEPHONE: +963 0952725590\n"
            "[FIRM] M-Code Developer Network - Secure Architecture\n"
            "----------------------------------------------------\n"
            "[ARABIC] تم التصميم من قبل محمد الحسين 0952725590\n"
            "مؤسسة مهتمة بالتطويرات البرمجية للأنظمة العسكرية والأمنية.\n"
            "===================================================="
        )
        layout.add_widget(Label(text=terminal_text, font_size='11sp', color=get_color_from_hex("#00ff00")))
        btn_back = Button(text="إغلاق نافذة المبرمج الشفافة", size_hint_y=0.15, background_color=get_color_from_hex("#222222"))
        btn_back.bind(on_press=self.back)
        layout.add_widget(btn_back)
        self.add_widget(layout)
    def back(self, instance): self.manager.current = 'menu'

class MedApp(App):
    def build(self):
        self.title = "MED - نظام الطوارئ المتكامل"
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(GatewayScreen(name='gateway'))
        sm.add_widget(CitizenScreen(name='citizen'))
        sm.add_widget(StationOpsScreen(name='station_ops'))
        sm.add_widget(AdminDashboardScreen(name='admin_dashboard'))
        sm.add_widget(MCodeScreen(name='mcode'))
        return sm

if __name__ == '__main__':
    MedApp().run()
