import random
import os
import logging
import asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config
import random
import pyrogram
from youtubesearchpython import VideosSearch
import youtube_dl
import platform
from telethon.tl import types
from telethon.tl import functions, types

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME
owner_id = Config.OWNER_ID

SUDO_USERS = Config.SUDO_USERS

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []

ozel_list = [1948748468]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("👋🏻 ᴍᴇʀʜᴀʙᴀ, ʙᴇɴ ᴀʜʀɪ! ʙᴀᴢı ᴋᴜʟʟᴀɴışʟı ᴏ̈ᴢᴇʟʟɪᴋʟᴇʀᴇ sᴀʜɪᴘ ᴛᴇʟᴇɢʀᴀᴍ ᴜ̈ʏᴇ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ʙᴏᴛᴜʏᴜᴍ.\n\n📚 sɪᴢᴇ ʏᴀʀᴅɪᴍᴄɪ ᴏʟᴀʙɪʟᴍᴇᴍ ɪᴄ̧ɪɴ ᴀşşᴀɢ̆ɪᴅᴀᴋɪ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ!",
                    buttons=(                  
		                      
                      [Button.url('➕ɢʀᴜʙᴀ ᴇᴋʟᴇ➕', f"https://t.me/{bot_username}?startgroup=a")],
                      [Button.url('📣ᴅᴇsᴛᴇᴋ📣', f"https://t.me/{support}")],
                      [Button.inline("📚ᴋᴏᴍᴜᴛʟᴀʀ📚", data="help")],
                      [Button.url('🛡ᴏᴡɴᴇʀ🛡', f"https://t.me/{owner}")],
		                  
                    ),
                    link_preview=False
                   )

@client.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit(f"⚙️ ᴍᴇʀʜᴀʙᴀ, ɪ̇şᴛᴇ ᴋᴏᴍᴜᴛʟᴀʀıᴍ ⚙️\n\n » /tag \n - 5 ᴋɪşɪʟɪᴋ ᴇᴛɪᴋᴇᴛ ᴏʟᴜşᴛᴜʀᴜʀ. \n » /otag \n - ᴋᴜʟʟᴀɴıᴄıʟᴀʀı sᴏʀᴜʏʟᴀ ᴇᴛɪᴋᴇᴛʟᴇʀ. \n » /ctag \n - ᴋᴜʟʟᴀɴıᴄıʟᴀʀı ʜᴏş sᴏ̈ᴢʟᴇʀʟᴇ ᴇᴛɪᴋᴇᴛʟᴇʀ. \n » /etag \n - ᴇᴍᴏᴊɪ ɪ̇ʟᴇ ᴇᴛɪᴋᴇᴛ ᴀᴛᴀʀ.\n » /tektag \n - ᴜ̈ʏᴇʟᴇʀɪ ᴛᴇᴋᴇʀ ᴛᴇᴋᴇʀ ᴇᴛɪᴋᴇᴛʟᴇʀ.\n » /btag \n - ʙᴀʏʀᴀᴋʟı şᴇᴋɪʟᴅᴇ ᴜ̈ʏᴇʟᴇʀɪ ᴇᴛɪᴋᴇᴛʟᴇʀ.\n » /admins \n - ᴀᴅᴍɪɴʟᴇʀɪ ᴅᴜ̈ᴢᴇɴʟɪ şᴇᴋɪʟᴅᴇ ᴇᴛɪᴋᴇᴛʟᴇʀ.\n » /slap \n - ʙɪ̇ʀ ᴋᴜʟʟᴀɴɪᴄɪʏɪ ᴛʀᴏʟʟᴇʀ.\n » /eros \n - ᴇʀᴏsᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴀʀ.", buttons=(

                   
                  [
                      Button.inline("➡️ ɢᴇʀɪ", data="start")
                    ]
                 ),
               link_preview=False)    


@client.on(events.callbackquery.CallbackQuery(data="start"))
async def start(event):
    await event.edit(f"👋🏻 ᴍᴇʀʜᴀʙᴀ, ʙᴇɴ ᴀʜʀɪ! ʙᴀᴢı ᴋᴜʟʟᴀɴışʟı ᴏ̈ᴢᴇʟʟɪᴋʟᴇʀᴇ sᴀʜɪᴘ ᴛᴇʟᴇɢʀᴀᴍ ᴜ̈ʏᴇ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ʙᴏᴛᴜʏᴜᴍ.\n\n📚 sɪᴢᴇ ʏᴀʀᴅɪᴍᴄɪ ᴏʟᴀʙɪʟᴍᴇᴍ ɪᴄ̧ɪɴ ᴀşşᴀɢ̆ɪᴅᴀᴋɪ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ!", 
                 buttons=(                  
		                      
                      [Button.url('➕ɢʀᴜʙᴀ ᴇᴋʟᴇ➕', f"https://t.me/{bot_username}?startgroup=a")],
                      [Button.url('📣ᴅᴇsᴛᴇᴋ📣', f"https://t.me/{support}")],
                      [Button.inline("📚ᴋᴏᴍᴜᴛʟᴀʀ📚", data="help")],
                      [Button.url('🛡ᴏᴡɴᴇʀ🛡', 'https://t.me/rahmetiNC')],
		                  
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"Etiket işlemi durduruldu!\n\n Etiketlenenlerin Sayısı👤: {rxyzdev_tagTot[event.chat_id]}**")


emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")

bayrak = "🏳️‍🌈 🏳️‍⚧️ 🇺🇳 🇦🇫 🇦🇽 🇦🇱 🇩🇿 🇦🇸 🇦🇩 🇦🇴 🇦🇮 🇦🇶 🇦🇬 🇦🇷 🇦🇲 🇦🇼 🇦🇺 🇦🇹 🇦🇿 🇧🇸 🇧🇭 🇧🇩  🇧🇧 🇧🇾 🇧🇪 🇧🇿 🇧🇯 🇧🇷 🇧🇼 🇧🇦 🇧🇴 🇧🇹 🇧🇲 🇻🇬 🇧🇳 🇧🇬 🇧🇫 🇧🇮 🇰🇭 🇰🇾 🇧🇶 🇨🇻 🇮🇨 🇨🇦 🇨🇲 🇨🇫 🇹🇩 🇮🇴 🇨🇳 🇨🇱 🇨🇽 🇨🇰 🇨🇩 🇨🇬 🇰🇲 🇨🇴 🇨🇨 🇨🇷 🇨🇿 🇪🇬 🇪🇹 🇪🇺 🇸🇻 🇩🇰 🇨🇮 🇭🇷 🇨🇺 🇨🇼 🇨🇾 🇪🇨 🇩🇴 🇩🇲 🇩🇯 🇬🇶 🇪🇷 🇫🇴 🇫🇰 🇫🇯 🇪🇪 🇸🇿 🇫🇮 🇬🇲 🇬🇦 🇹🇫 🇵🇫 🇬🇫 🇫🇷 🇬🇪 🇩🇪 🇬🇭 🇬🇮 🇬🇷 🇬🇱 🇬🇳 🇬🇬 🇬🇹 🇬🇺 🇬🇵 🇬🇩 🇬🇼 🇬🇾 🇭🇹 🇭🇳 🇭🇰 🇭🇺 🎌 🇮🇪 🇮🇶 🇯🇵 🇯🇲 🇮🇷 🇮🇩 🇮🇹 🇮🇱 🇮🇳 🇮🇸 🇮🇲 🇯🇪 🇯🇴 🇰🇬 🇰🇼 🇱🇷 🇱🇾 🇱🇮 🇱🇦 🇰🇿 🇰🇪 🇱🇻 🇱🇹 🇱🇺 🇱🇧 🇰🇮 🇽🇰 🇱🇸 🇲🇴 🇲🇹 🇲🇱 🇲🇻 🇲🇾 🇲🇼 🇲🇬 🇹🇷 🇹🇱 🇸🇪 🇸🇩 🇸🇧 🇸🇴 🇰🇷".split(" ")

#  güzel isimler...!!! 
cumle = ['Üzümlü kekim ✨', 'Nar çiçeği ✨', 'Papatya 🌼', 'Karanfil ✨', 'Gül 🌹', 'Ayıcık 🐻', 'Mutlu pandam 🐼', 'Ay parem ✨', 'Ballı lokmam ✨', 'Bebişim 🥰', 'Lale 🌷', 'Zambak ⚜', 'Nergis ✨', 'Sümbül ☘️', 'Nilüfer ☘️', 'Menekşe ⚜️', 'Lavanta ✨', 'Gül pare ✨', 'Reyhan 🌷', 'Kaktüs ⚜️', 'Böğürtlen ☘️', 'Orkide ☘️', 'Manolya ✨', 'Ayçiçeği ✨', 'Tweety ⚜️', 'Star ✨', 'Yonca 🍀', 'Ateş böceği ✨',]

# sorular cano
soru = ['Naber?', 'Nerelerdesin Aşko?', 'Özledimmmmm', 'İyimisin?', 'Ayıcık seniii', 'Biraz Sohbet edelim?', 'mutlumusun?', 'Nerelisin?', 'Nerdesin Pangoo?', 'Bebişimmmmm', 'Hayvan Severmisin?', 'Çiçek Severmisin?', 'Inst Verde Flowwwlaşakk', 'Ne Zamandır Telegramdasın?', 'Bıcı Bıcıı Yaparım Dalinle', 'Çalışıyormusun?', 'Evlimisin?', 'kebap Severmisin?', 'Günün Nasıl Geçti?', 'Papağan Severmisin?', 'En Sevdiğn Rapçii?', 'Sevgilin Varmı?', 'Açmısın?', 'Okuyormusun?', 'Kaçıncı Sınıfsın?', 'Karamsarmısın?', 'Duygusalmısın?', 'Kışları Severmisin?',]

@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komutu gruplar ve kanallar için geçerli!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bu Komutu Sadece Yöneticiler Kullana Bilir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajları Etiketlemek İçin Kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("İşleme Başlamak İçin Bir Sebep Yok!")
  else:
    return await event.respond("İşleme Başlamam İçin Bir Sebep Yazın!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrak)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("İşlem Başarıyla Durduruldu!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
	
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)	

@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komutu gruplar ve kanallar için geçerli!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bu Komutu Sadece Yöneticiler Kullana Bilir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajları Etiketlemek İçin Kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("İşleme Başlamak İçin Bir Sebep Yok!")
  else:
    return await event.respond("İşleme Başlamak için Mesaj Yazmalısın!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
       await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
       return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""





@client.on(events.NewMessage(pattern="^/ctag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komutu gruplar ve kanallar için geçerli!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bu Komutu Sadece Yöneticiler Kullana Bilir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajları Etiketlemek İçin Kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("İşleme Başlamak İçin Bir Sebep Yok!")
  else:
    return await event.respond("İşleme Başlamak için Mesaj Yazmalısın!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
       await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
       return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern="^/otag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komutu gruplar ve kanallar için geçerli!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bu Komutu Sadece Yöneticiler Kullana Bilir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajları Etiketlemek İçin Kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("İşleme Başlamak İçin Bir Sebep Yok!")
  else:
    return await event.respond("İşleme Başlamak için Mesaj Yazmalısın!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(soru)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
       await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
       return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(soru)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komut gruplar ve kanallar için geçerlidir!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bu Komutu Sadece Yöneticiler Kullana Bilir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki mesajları etiket işlemi için kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("İşleme Başlamak İçin Bir Mesaj Yazmalısın!")
  else:
    return await event.respond("İşleme Başlamak İçin Sebep Yok!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

import random

@client.on(events.NewMessage(pattern="^/eros$"))
async def eros(event):
    # Sadece grup ve kanallarda çalıştır
    if event.is_private:
        await event.respond("Bu komut yalnızca grup ve kanallarda kullanılabilir.")
        return

    # Grup veya kanal katılımcılarını al
    users = await client.get_participants(event.chat_id, limit=200)
    
    users_list = []
    for user in users:
        if user.bot or user.deleted:
            continue  # Silinmiş hesapları veya botları atla
        else:
            users_list.append(user)
    count = len(users_list)
    
    # Rastgele iki kullanıcı seç
    first_user = users_list[random.randint(0, count - 1)]
    second_user = users_list[random.randint(0, count - 1)]
    
    # Belirli kullanıcıları kontrol et
    if (first_user.id == 1550788256 or first_user.id == 5576614947
        or second_user.id == 5375589992 or second_user.id == 5576614947):
        # Belirli kullanıcılar eşleştiğinde özel bir yanıt gönder
        await event.respond("**💌 Eros'un oku atıldı.\n• Aşıklar  :\n\n@[kullanici1](tg://user?id=5053767281) ❤️ @[kullanici2](tg://user?id=5533927130)**")
    else:
        # Rastgele seçilen kullanıcıların adlarını veya kullanıcı adlarını gönder
        percentage = random.randint(1, 100)  # Rastgele bir yüzde hesapla
        await event.respond(f"**💌 Eros'un oku atıldı.\n• Aşıklar  :\n\n@{first_user.username} ❣️ @{second_user.username}\n\n📊 Eşleşme Yüzdesi: {percentage}%**")


@client.on(events.NewMessage(pattern="^/bots$"))
async def list_bots(event):
    # Sadece grup ve kanallarda çalıştır
    if event.is_private:
        await event.respond("Bu komut yalnızca grup ve kanallarda kullanılabilir!")
        return

    # "Bir saniye bekleyin..." mesajını gönder
    message = await event.respond("Bir Saniye..!")

    # 3 saniye bekle
    await asyncio.sleep(3)

    # "Bir saniye bekleyin..." mesajını sil
    await message.delete()

    # Grup veya kanal katılımcılarını al
    users = await client.get_participants(event.chat_id, limit=200)

    bot_list = []
    for user in users:
        if user.bot:
            bot_list.append(user)

    # Bot listesini oluştur ve gönder
    if bot_list:
        bot_names = "\n".join([f"➻ @{user.username}" for user in bot_list])
        await event.respond(f"🤖 Gruptaki Botlar Şunlar:\n\n{bot_names}")
    else:
        await event.respond("🤖 Bu Grupta Hiç Bot Bulamadım!")


@client.on(events.NewMessage(pattern='/slap'))
async def slap(event):
    if event.is_private:
        return await event.respond("Bu komut gruplar ve kanallar için geçerlidir!")

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        user = reply_message.sender
        if user:
            user_name = user.first_name
            slap_phrases = [
                f"{user_name}'nin üzerine pasta fırlattı!",
                f"{user_name}'nin üstüne benzin döktü!",
                f"{user_name}'yi ateşe attı!",
                f"{user_name}'nin üstüne su döktü!",
                f"{user_name}'yi dondurdu!",
                f"{user_name}'nin üzerine pasta fırlattı!",
                f"{user_name}'yi Zencilere Sattı!",
                f"{user_name}'yi Turşu Kavonozuna Soktu!",
                f"{user_name}'nin Üzerine Buz Dolabı Attı!",
                f"{user_name}'nin Kafasını Duvara Sürterek Yaktı!",
                f"{user_name}'yi Ormana Kaçırdı!",
                f"{user_name}'yi Banyoda Sukast Etti!",
            ]
            slap_phrase = random.choice(slap_phrases)
            await event.respond(f"{event.sender.first_name} {slap_phrase}")
        else:
            await event.respond("Üzgünüm, kullanıcıyı bulamıyorum!")
    else:
        await event.respond("Bu komutu kullanabilmek için bir mesaja yanıt vermelisiniz!")


@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("Bu komut gruplar ve kanallar için geçerlidir!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bu Komutu Sadece Yetkililer Kullana Bİlir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki mesajları etiket işlemi için kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlamak için mesaj yazmalısın!")
  else:
    return await event.respond("İşleme başlamam için mesaj yazmalısın!")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("Etiketleme İşlemi Durduruldu!")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("Etiketleme İşlemi Durduruldu!")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def mentionall(tagadmin):

	if tagadmin.pattern_match.group(1):
		seasons = tagadmin.pattern_match.group(1)
	else:
		seasons = ""

	chat = await tagadmin.get_input_chat()
	a_=0
	await tagadmin.delete()
	async for i in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
		if a_ == 500:
			break
		a_+=5
		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))
		sleep(0.5)
	
@client.on(events.NewMessage(pattern='/bot'))
async def bot_group_count(event):
    # Sadece belirli bir kullanıcı kimliğine sahip kullanıcılar tarafından kullanılabilir
    allowed_user_id = 5944841427  # İzin verilen kullanıcının kimliği

    if event.sender_id == allowed_user_id:
        # Botun bulunduğu grup sayısını al
        async for dialog in client.iter_dialogs():
            if dialog.is_group:
                group_count += 1

        await event.respond(f'🤖 Bot {group_count} grupta bulunuyor.')
    else:
        await event.respond('Bu komutu kullanma izniniz yok.')


@client.on(events.NewMessage(pattern='/durum'))
async def handler(event):
    # Sadece belirli bir kullanıcı kimliğine sahip kullanıcılar tarafından kullanılabilir
    allowed_user_id = 5944841427 # İzin verilen kullanıcının kimliği

    if event.sender_id == allowed_user_id:
        user = await event.get_sender()
        user_first_name = user.first_name  # Kullanıcının adını alın

        response_text = (
            f'Hey, {user_first_name} Aktifim! Bilgilerim Aşağıda.\n\n'
            f'⚙️ Versiyon [ V1 ]\n'
            f'💠 Python Versiyon : {platform.python_version()}\n'
            f'💻 Telethon Versiyon : {telethon.__version__}'
        )

        await event.respond(response_text)
    else:
        await event.respond('Bu komutu kullanma izniniz yok!')


from telethon.tl import types
from telethon import Button

@client.on(events.NewMessage(pattern='/grup'))
async def grup_info(event):
    # Sadece grup ve kanallarda çalıştır
    if event.is_private:
        await event.respond("Bu komut yalnızca grup ve kanallarda kullanılabilir.")
        return

    user = await event.get_sender()
    user_first_name = user.first_name

    # İlk yanıtı gönder
    response_text = f'Hey! {user_first_name}, Bilgiler Geliyor Bekle!'
    response = await event.respond(response_text)

    # Bekleme süresi (5 saniye)
    await asyncio.sleep(5)

    # İlk yanıtı sil
    await response.delete()

    # Grup bilgilerini gönder
    chat = await event.get_chat()
    group_name = chat.title
    group_id = chat.id

    # Grup bilgilerini al
    chat_info = await event.client.get_entity(group_id)

    # Diğer bilgileri al
    deleted_count = 0
    active_count = 0
    bot_count = 0
    total_count = 0

    # Katılmış üyelerin listesini al
    async for participant in event.client.iter_participants(chat_info):
        total_count += 1
        if participant.deleted:
            deleted_count += 1
        elif not participant.bot:
            active_count += 1
        elif participant.bot:
            bot_count += 1

    # Özel durumları kontrol et
    special_status = ""
    if deleted_count > 0:
        special_status += f'➻ Delete Hesap: {deleted_count}\n'
    if bot_count > 0:
        special_status += f'➻ Bot Sayısı: {bot_count}\n'

    # Özel durumlar olmadığında "Bulunamadı" mesajı ver
    if not special_status:
        special_status = "Bulunamadı"

    # Owner'ın kullanıcı adını belirtin
    owner_username = "owner"  # Değiştirin

    # Owner butonunu oluşturun
    owner_button = Button.url('🛡ᴏᴡɴᴇʀ🛡', f"https://t.me/{owner}")

    response_text = (
        f'➻ Grup Adı: {group_name}\n'
        f'➻ Grup ID: {group_id}\n'
        f'➻ Aktif Kullanıcıları: {active_count}\n'
        f'➻ Grup Üye Sayısı: {total_count}\n'
        f'{special_status}'
    )

    # Bilgileri yanıt olarak gönder ve Owner butonunu ekleyin
    await event.respond(response_text, buttons=[[owner_button]])


# Sadece izin verilen kullanıcı tarafından kullanılabilen kullanıcı kimliği
allowed_user_id = 5944841427  # İzin verilen kullanıcının kimliği (değiştirin)

# /reklam komutu
@client.on(events.NewMessage(pattern='/reklam (.+)'))
async def reklam(event):
    # Sadece belirtilen kullanıcıya izin ver
    if event.sender_id != allowed_user_id:
        await event.respond('Bu komutu kullanma izniniz yok.')
        return

    # Gönderilen mesajı al
    message = event.pattern_match.group(1)
    
    # İşlem başladı mesajını gönder
    await event.respond('İşlem Başladı!')

    # İşlemi başlat
    sent_to_groups = 0
    sent_to_users = 0

    async for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            try:
                await client.send_message(dialog.id, message)
                sent_to_groups += 1
            except Exception as e:
                pass
        elif dialog.is_user:
            try:
                await client.send_message(dialog.id, message)
                sent_to_users += 1
            except Exception as e:
                pass
    
    # İşlem tamamlandı mesajını gönder
    result_message = (
        'İşlem Biti!\n'
        f'Gönderilen Grup Sayısı: {sent_to_groups}\n'
        f'Gönderilen DM Sayısı: {sent_to_users}'
    )
    await event.respond(result_message)

    # İşlem bittiğinde bekleyen işlemi sonlandırmak için 2 saniye bekleyin
    await asyncio.sleep(2)
    await event.respond('İşlem Tamamlandı!')

    # Hata durumunu kontrol edin
    if sent_to_groups == 0 and sent_to_users == 0:
        await event.respond('Hata: Mesaj gönderilemedi.')

print("Ahri Tagger AKtif, Sağol Sahip! @rahmetiNC ✨")
client.run_until_disconnected()
