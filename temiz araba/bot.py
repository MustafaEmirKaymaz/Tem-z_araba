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

            # class_name'ı temizle
            class_name = class_name.strip()
            # numarayı ve ismi ayır
            _, real_name = class_name.split(" ", 1)

            messages = {
                #"0 balik": "🐟 Balıklar\n\nBalıklara bakımı kolaydır ve beslemesi de basittir.\n\n",
                #"1 karadees": "🦐 Karides\n\nYenilebilen bir hayvandır, özellikle deniz ürünleri sofralarının vazgeçilmezidir.\n\n",
                #"2 kopek_baligi": "🦈 Köpekbalığı\n\nSeni yiyebilir, görünce bence kaç! 😄\n\n",
                #"3 yunus": "🐬 Yunus\n\nBaya tatlı ve zeki bir hayvandır.\n\n",
                #"4 deniz_ati": "🧜‍♂️ Denizatı\n\nAta benzeyen ilginç bir deniz canlısıdır.\n\n",
                #"5 deniz_kaplumbagasi": "🐢 Deniz Kaplumbağası\n\nUzun yıllar yaşayan huzurlu deniz canlısıdır.\n\n",
            }

            #special_message = messages.get(class_name, "Bu sınıf için özel bir mesaj yok.")

            await ctx.send(f"🔍 Tahmin: `{real_name}` (%{confidence*100:.2f} güven)")

        except Exception as e:
            await ctx.send(f"⚠️ Hata oluştu: {str(e)}")


# Tokenını gizli tut, buraya doğrudan yazma!
bot.run("")