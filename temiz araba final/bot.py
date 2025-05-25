import discord
from discord.ext import commands
import os
from model import get_class

# Görsellerin kaydedileceği klasör
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.event
async def on_guild_join(guild):
    # Yazabileceği ilk metin kanalını bul
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            try:
                embed = discord.Embed(
                    title="🤖 Merhaba! Ben Temiz Araba Botuyum!",
                    description=(
                        "Bana araç görselleri göndererek **temizlik durumunu** tahmin edebilirsin!\n\n"
                        "**Komutlar:**\n"
                        "`$yukle` → Bir görsel ekleyip bu komutu yaz, ben tahmin yapayım.\n"
                        "`$hello` → Merhaba demek için 😄\n"
                        "`$heh [sayı]` → 'he' ile dalga geçmek için.\n\n"
                        "Herhangi bir sorunda yardım etmeye hazırım. 🚗✨"
                    ),
                    color=0x00ffcc
                )
                embed.set_footer(text="Temiz_Araba Botu | Mustafa Emir Kaymaz")

                await channel.send(embed=embed)
                break
            except Exception as e:
                print(f"Tanıtım mesajı gönderilemedi: {e}")
@bot.command()
async def tanitim(ctx):
    embed = discord.Embed(
        title="🤖 Merhaba! Ben Temiz Araba Botuyum!",
        description=(
            "Bana araç görselleri göndererek **temizlik durumunu** tahmin edebilirsin!\n\n"
            "**Komutlar:**\n"
            "`$yukle` → Bir görsel ekleyip bu komutu yaz, ben tahmin yapayım.\n"
            "`$hello` → Merhaba demek için 😄\n"
            "`$tanitim` → Bu tanıtımı tekrar görmek için.\n\n"
            "Herhangi bir sorunda yardım etmeye hazırım. 🚗✨"
        ),
        color=0x00ffcc
    )
    embed.set_footer(text="Temiz_Araba Botu | Mustafa Emir Kaymaz")
    await ctx.send(embed=embed)
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def yukle(ctx):
    attachments = ctx.message.attachments

    if not attachments:
        await ctx.send("Herhangi bir görsel bulamadım. Lütfen komutu kullanırken bir görsel ekleyin!")
        return

    for attachment in attachments:
        file_name = attachment.filename
        file_path = os.path.join(IMAGE_DIR, file_name)

        try:
            await attachment.save(file_path)
            
            # Modeli çalıştır
            model_path = "keras_model.h5"
            labels_path = "labels.txt"
            class_name, confidence = get_class(file_path, model_path, labels_path)

            class_name = class_name.strip()
            _, real_name = class_name.split(" ", 1)

            # Genel araç sınıfı mesajları
            messages = {
                "Baya Kirli Araba": {
                    "title": "🧼🚫 Havayı Baya Kirleten Araba",
                    "description": "bu araç kullanılmamalı ki hava mız atmosferimiz temiz olsun",
                    "color": 0x8B0000  # koyu kırmızı
                },
                "Kirli Araba": {
                    "title": "🧼 havayı az kirleten Araba",
                    "description": "kullanlıabilir ama fazla değil",
                    "color": 0xFFA500  # turuncu
                },
                "Az kirli Araba": {
                    "title": "✨ Havayı Az Kirleten Araba",
                    "description": "araç günlük kunnaımlara hazır havayı çok kirletmez",
                    "color": 0xFFFF99  # açık sarı
                },
                "Temiz Araba": {
                    "title": "🚗 havayı kirletmeyen Araba",
                    "description": "araba her zaman kullanılabilir ve ter temiz bir havaya yardım eder",
                    "color": 0x00FF00  # yeşil
                }
            }

            # Embed verisini bul
            message_data = messages.get(real_name, {
                "title": "🚘 Araç Tespit Edildi",
                "description": "Bu araç türü için özel bilgi bulunamadı.",
                "color": 0xffffff
            })

            # Embed mesaj oluştur
            embed = discord.Embed(
                title=message_data["title"],
                description=message_data["description"],
                color=message_data["color"]
            )
            embed.add_field(name="Tahmin", value=real_name, inline=True)
            embed.add_field(name="Güven Oranı", value=f"%{confidence*100:.2f}", inline=True)
            embed.set_footer(text="Temiz_Araba Botu | Mustafa Emir Kaymaz")

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"⚠️ Hata oluştu: {str(e)}")

# Token'ı buraya yazma, .env veya config dosyası kullan
bot.run("")  # Bot token buraya eklenmeli