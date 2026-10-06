#!/bin/bash

clear
echo -e "\e[1;36m====================================================\e[0m"
echo -e "\e[1;32m      M-CODE AUTOMATED APK EXPORTER & DEPLOYER      \e[0m"
echo -e "\e[1;36m====================================================\e[0m"
echo -e "[*] جاري البحث عن ملف الـ APK المجمع داخل مجلد bin..."

# تحديد مسار مجلد المخرجات لـ Buildozer
BIN_DIR="$HOME/MED_App/bin"
TARGET_DIR="/sdcard/Download"

# التحقق من وجود ملفات APK
if [ -d "$BIN_DIR" ] && [ "$(ls -A $BIN_DIR/*.apk 2>/dev/null)" ]; then
    APK_FILE=$(ls -t $BIN_DIR/*.apk | head -n 1)
    echo -e "\e[1;32m[✓] تم العثور على أحدث نسخة مجمعة:\e[0m $(basename "$APK_FILE")"
    
    # نقل الملف وتغيير اسمه ليكون احترافياً وقابلاً للاستخدام الفوري
    echo "[*] جاري نقل الملف وتأمين الصلاحيات إلى مجلد الـ Download للهاتف..."
    cp "$APK_FILE" "$TARGET_DIR/MED_CivilDefense_v1.0.apk"
    
    echo -e "\e[1;32m====================================================\e[0m"
    echo -e "\e[1;36m[✓] نجح النقل! التطبيق جاهز للتثبيت الآن على هاتفك.\e[0m"
    echo -e "\e[1;33m📍 المسار: وحدة التخزين الداخلية ➔ Download ➔ MED_CivilDefense_v1.0.apk\e[0m"
    echo -e "\e[1;32m====================================================\e[0m"
else
    echo -e "\e[1;31m❌ خطأ: لم يتم العثور على ملف APK مجمع بعد.\e[0m"
    echo -e "\e[1;33m💡 يرجى التأكد من انتهاء أمر البناء بنجاح أولاً دون أخطاء.\e[0m"
fi
