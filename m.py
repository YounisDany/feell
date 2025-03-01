import os

folder = "img/"  # المجلد الذي يحتوي على الصور
images = [f for f in os.listdir(folder) if f.endswith((".svg", ".png", ".jpg", ".jpeg"))]  # جلب جميع الصور
images.sort()  # ترتيب الملفات قبل التسمية

for index, image in enumerate(images, start=1):
    ext = os.path.splitext(image)[1]  # استخراج الامتداد (.svg, .png, ...)
    new_name = f"{index}{ext}"  # اسم الملف الجديد بالأرقام
    old_path = os.path.join(folder, image)
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)
    print(f"تمت إعادة تسمية {image} إلى {new_name}")

print("✅ تم الانتهاء من إعادة التسمية!")
