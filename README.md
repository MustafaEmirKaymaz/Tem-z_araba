
# 🚗 Temiz_Araba Discord Botu

Merhaba! Ben Mustafa Emir Kaymaz.  
Bu proje, çevre dostu bir yaklaşımla geliştirilmiş **Temiz_Araba** adlı Discord botudur. Kullanıcıların yüklediği araç görsellerini analiz ederek, havayı ne kadar kirlettiğini belirler ve eğlenceli bir şekilde kullanıcıya geri bildirir.

---

## 🎯 Amaç

Bu botun amacı, arabaların çevreye olan etkilerini (hava kirliliği açısından) sınıflandırmak ve kullanıcıyı bilinçlendirmektir. Yapay zeka modeli kullanılarak araç temizliği analiz edilir ve sınıfına göre anlamlı mesajlarla geri dönülür.

---

## ⚙️ Özellikler

- 🖼️ Kullanıcı araba fotoğrafı yüklediğinde sınıflandırma yapar.
- 🌫️ Görseldeki aracın havayı ne kadar kirlettiğini tahmin eder.
- 📊 Tahminin doğruluk (güven) oranını gösterir.
- 🤖 Sunucuya ilk eklendiğinde tanıtım mesajı gönderir.
- 💬 Eğlenceli ve bilgilendirici komutlara sahiptir:
  - `$yukle` → Görsel ekleyerek araç temizliğini analiz et.
  - `$hello` → Bot ile selamlaş.
  - `$heh [sayı]` → “he” kelimesini belirtilen sayı kadar tekrar eder.
  - `$tanitim` → Botun tanıtım mesajını yeniden gösterir.

---

## 🛠️ Kurulum

### 1. Depoyu Klonla

```bash
git clone https://github.com/kullaniciadi/temiz-araba-botu.git
cd temiz-araba-botu
```

### 2. Gerekli Python Paketlerini Kur

```bash
pip install tensorflow
pip install -U discord.py
pip install pillow
pip install numpy
pip install python-dotenv
```

### 3. Ortam Değişkenlerini Ayarla

Proje klasörüne `.env` adında bir dosya oluştur ve şu satırı ekle:

```
DISCORD_TOKEN=buraya_token_yaz
```

### 4. Botu Başlat

```bash
python bot.py
```

---

## 📁 Dosya Yapısı

```
temiz-araba-botu/
├── bot.py               # Ana Discord bot kodu
├── model.py             # Yapay zeka modelini çağıran fonksiyon (get_class)
├── keras_model.h5       # Eğitilmiş Keras modeli
├── labels.txt           # Model sınıf etiketleri
├── images/              # Kullanıcı görsellerinin kaydedildiği klasör
├── .env                 # Token bilgisinin bulunduğu dosya
└── requirements.txt     # Proje bağımlılıkları (opsiyonel)
```

---

## 🧠 Yapay Zeka Modeli

Bot, TensorFlow ile eğitilmiş bir modeli (`keras_model.h5`) kullanarak, yüklenen araba görsellerini dört sınıfa ayırır:

- 🚗 Temiz Araba
- ✨ Az Kirli Araba
- 🧼 Kirli Araba
- 🧼🚫 Baya Kirli Araba

Tahmin sonucunda, araç sınıfı ve güven oranı kullanıcıya embed mesajla sunulur. Her sınıf için özel başlık, açıklama ve renk düzeni bulunmaktadır.

---

## 💬 Komutlar

| Komut        | Açıklama |
|--------------|----------|
| `$yukle`     | Fotoğraf yükleyin ve bu komutu yazın, bot temizlik tahmini yapar. |
| `$hello`     | Selamlaşma mesajı gönderir. |
| `$heh [sayı]`| Girilen sayı kadar “he” mesajı tekrar eder. |
| `$tanitim`   | Botun tanıtım mesajını embed olarak yeniden gönderir. |

---

## ✅ Kullanım Örneği

1. Discord’da bir metin kanalına araba görselini yükleyin.
2. Ardından `$yukle` komutunu yazın.
3. Bot size aracın temizlik sınıfını ve güven oranını embed mesaj ile bildirir.

---

## 🔐 Güvenlik Uyarısı

Discord bot token’ınızı asla `bot.py` içerisine doğrudan yazmayın.  
Güvenli kullanım için `.env` dosyası ve `python-dotenv` paketini kullanarak şifreyi saklayın.

```python
from dotenv import load_dotenv
load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))
```

---

## 👨‍💻 Geliştirici

Mustafa Emir Kaymaz  
Discord: mustafakaymaz#0000  
Görüş, öneri ve katkılar için her zaman ulaşabilirsiniz.

---

## ⭐ Destek Ol

Projeyi faydalı bulduysanız GitHub’da yıldız vermeyi unutmayın ⭐  
Katkı sağlamak isterseniz Pull Request gönderebilirsiniz.  
Daha temiz bir gelecek için teknolojiyle harekete geç! 🌍✨
