# 📓 AdolNote

AdolNote, Linux kullanıcıları için geliştirilen minimalist ve hızlı bir not alma uygulamasıdır. Hem terminal (CLI) hem de basit bir grafik arayüz (GUI) sunar. Python ile yazılmış açık kaynaklı bir projedir.

---

## 🚀 Özellikler

- ✅ Not ekleme, silme, listeleme (CLI ve GUI)
- ✅ Kopyalama, anlık bildirim (GUI)
- ✅ Temiz ve sade arayüz
- ✅ Tkinter ile GUI desteği
- ✅ Python ile geliştirildi
- ✅ Açık kaynak (MIT lisanslı)

---

## 📦 Kurulum

### Gereksinimler

- Python 3.8+
- Tkinter (`sudo pacman -S tk` – Arch Linux için)

### Kurulum Adımları

```bash
# 1. Depoyu klonlayın
git clone https://github.com/Aybarssafak/AdolNote.git
cd AdolNote

# 2. Bağımlılıkları yükleyin
pip install -r requirements.txt

##🖥️ Kullanım
###🔸 CLI (Terminal) Kullanımı

 Not ekle
python cli/main.py --add "Bugün çalışmalıyım"

 Notları listele
python cli/main.py --list

 Not sil (ID ile)
python cli/main.py --delete 1

###🔹 GUI (Grafik Arayüz) Kullanımı

python gui/main.py
```

##🗂️ Proje Yapısı
```bash

AdolNote/
├── cli/              # Komut satırı arayüzü
│   └── main.py
├── gui/              # Grafik arayüz
│   └── main.py
├── utils/            # Not kayıt/silme işlevleri
│   └── storage.py
├── requirements.txt  # Python bağımlılıkları
├── LICENSE           # MIT lisans dosyası
├── README.md         # Bu dosya
```

###🧑‍💻 Geliştirici

Aybarssafak
📍 Türkiye

###📄 Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Detaylı bilgi için LICENSE dosyasına göz atabilirsiniz.

###🌟 Destek Ol

Projeyi beğendiyseniz ⭐ vererek destek olabilirsiniz.
Arkadaşlarınızla paylaşmak da motivasyon kaynağı olur 🙌
