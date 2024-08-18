import os
import re
from googletrans import Translator

# Çevirici nesnesi oluştur
translator = Translator()

# Proje dizini
project_path = "/Users/mali/development/gosports/"

# Taranacak dosya türleri (örneğin, .go, .html, .js)
file_extensions = [".go", ".html", ".js", ".vue"]

# Çince karakterleri tespit etmek için regex
chinese_pattern = re.compile("[\u4e00-\u9fff]+")

# Belirtilen dosya türlerine sahip dosyaları taramak için fonksiyon
def scan_and_translate_files(directory):
    print(f"Taranacak dizin: {directory}")  # Log ekleme
    for root, dirs, files in os.walk(directory):
        # 'node_modules' klasörünü hariç tut
        dirs[:] = [d for d in dirs if d != 'node_modules']

        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file)
                print(f"Taranan dosya: {file_path}")  # Log ekleme
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Çince karakterleri bul
                    chinese_matches = chinese_pattern.findall(content)
                    if chinese_matches:
                        print(f"Çince karakterler bulundu: {file_path}")
                        translated_content = content

                        # Çince kelimeleri İngilizceye çevir ve değiştir
                        for match in chinese_matches:
                            print(f"Çeviri yapılıyor: {match}")  # Log ekleme
                            translated_text = translator.translate(match, src='zh-cn', dest='en').text
                            print(f"Çevrilen kelime: {translated_text}")  # Çevrilen kelimeyi yazdır
                            translated_content = translated_content.replace(match, translated_text)

                        # Değişiklikleri kaydet
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(translated_content)
                        print(f"Değişiklikler kaydedildi: {file_path}")
                except Exception as e:
                    print(f"Hata oluştu: {e}")

# Projeyi taramaya başla
scan_and_translate_files(project_path)
print("İşlem tamamlandı!")
