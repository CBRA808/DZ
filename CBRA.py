import importlib

# نستورد الملف المشفّر (اسمه CBRA.cpython-312.so ⇒ يعني الموديول = "CBRA")
cbra = importlib.import_module("CBRA")
cbra.mmk()
