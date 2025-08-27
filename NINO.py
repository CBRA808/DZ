import importlib

# استدعاء الملف المشفر NINO.cpython-312.so
NINO = importlib.import_module("NINO")

# شغّل الدالة الرئيسية (بدّل 'main' بالاسم الصحيح داخل الملف المشفر)
try:
    NINO.main()
except AttributeError:
    print("[!] لم أجد الدالة 'main' داخل الملف المشفر NINO")
