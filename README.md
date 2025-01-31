
# zorinos
python3 clident.py
pip install pynput
setxkbmap tr


```bash
import revolt
import asyncio
import ollama

TOKEN = "BURAYA_BOT_TOKENİNİ_YAZ"

class RevoltBot(revolt.Client):
    async def on_ready(self):
        print(f"Bot {self.user.name} olarak giriş yaptı!")

    async def on_message(self, message: revolt.Message):
        if message.author.bot:
            return  # Bot kendi mesajlarına yanıt vermesin

        if message.content.startswith("!chat"):
            user_message = message.content[len("!chat "):]  # Komut kısmını kaldır

            if not user_message:
                await message.reply("Lütfen bir mesaj girin: `!chat Merhaba!`")
                return

            # Moondream 2 modelinden yanıt al
            response = ollama.chat(model="moondream", messages=[{"role": "user", "content": user_message}])
            bot_reply = response['message']['content']

            # Yanıtı gönder
            await message.reply(bot_reply)

# Botu başlat
async def main():
    # Yeni bir session oluştur
    session = revolt.ClientSession()

    # Token ile botu başlat
    bot = RevoltBot(session=session, token=TOKEN)
    
    await bot.start()

asyncio.run(main())
````
_jMfauIoCXZHFdOZXKv3rWvmUdthJkvLUD4d5U65YlfSDn5CJUMuIlusAgNL9Nvt
