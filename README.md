# 🚗 Temiz_Araba Discord Botu

Merhaba! Ben Mustafa Emir Kaymaz.  
Bu proje, çevre dostu bir yaklaşım ile yazılmış **Temiz_Araba** adlı Discord botudur. Bot, kullanıcıların yüklediği araba fotoğraflarını analiz ederek havayı ne kadar kirlettiğini belirler.

---

## 🎯 Amaç

Bu botun amacı, arabaların çevreye olan etkilerini (hava kirliliği açısından) sınıflandırmak ve kullanıcıyı bilgilendirmektir.

---

## ⚙️ Özellikler

- Kullanıcı araba fotoğrafı yüklediğinde sınıflandırma yapar.
- Görseldeki aracın havayı ne kadar kirlettiğini tahmin eder.
- Tahminin doğruluk oranını gösterir.

---

## 🛠️ Kurulum

### 1. Gerekli Python Paketleri:

```bash
pip install tensorflow
pip install -U discord.py
pip install pillow
pip install numpy
```



**Dosya Yapısı**
│

├── bot.py               # Ana Discord bot kodu

├── model.py             # Tahmin modeli işlemleri

├── keras_model.h5       # Eğitimli model dosyası

├── labels.txt           # Sınıf etiketleri

└── images/              # Kullanıcıdan gelen görseller buraya kaydedilir

##Kullanım şekl
```bash
 $yukle
 
