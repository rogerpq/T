import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Jsbot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Jsbot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Jsbot.send_message(
               chat_id=message.chat.id,
               text="""<b>مرحبا صديقي انا بوت تلجراف ميديا 

👻 هذا هو بوت استخراج رابط تلجراف ميديا الخاص في سورس ريبثون اختر ماتريد من الاسفل 
👇 تسطيع استخراج 👇

📽️ فيديوهات قصيره (ان لايتعدا حجمه 5MB).
🎬 فيديوهات مرحليه.
🖼️ صورة.
💥 متحركة.
💟 ملصق.
📜 ملفات نصيه.
📩 صندوق دعم.
👥 مجموعة الدعم.
🚀 الاستخراج السريع .

✍️هذا هو بوت استخراج رابط تلجراف ميديا الخاص ب سورس ريبثون 
ارسل لي اي شئ تريده لاجعله رابط ්😝

هل تحتاج لل المساعدة راسل المطور @ZQ_LO</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🌷Help", callback_data="help"),
                                        InlineKeyboardButton(
                                            "✨قناتنا", url="https://t.me/Repthon"),
                                         InlineKeyboardButton(

                                            "قناتنا على اليوتيوب", url="https://youtube.com/channel/UC-zRRPaD5kTKFXd-Io3mVXw")
                                    ]]
                            ),
            disable_web_page_preview=True,        
            parse_mode="html")

@Jsbot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Jsbot.send_message(
               chat_id=message.chat.id,
               text="""<b>بوت تلجراف ميديا 🙈

فقط ارسل صوره او فيديو قصير او متحركه وسوف احوله الى رابط تلجراف .🎉

☘️ المبرمج : @ZQ_LO

@EITHON1</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙رجوع", callback_data="start"),
                                        InlineKeyboardButton(
                                            "👻حول", callback_data="about"),
                                  ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jsbot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Jsbot.send_message(
               chat_id=message.chat.id,
               text="""<b>حول هذا البوت!</b>

<b>☘️ المبرمج :</b> <a href="https://t.me/TTTLL0">FORM SIYRA🇸🇾</a>

<b>🔆اللغة:</b> <a href="https://www.python.org/">Python 3</a>

<b>♻️اصدار بايروجرام 1.4.16:</b> <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a>

<b>@EITHON1</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "🔙رجوع", callback_data="help"),
                                        InlineKeyboardButton(
                                            "❌اغلاق", callback_data="close")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Jsbot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("جاري استخراج الرابط...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("ارسل صوره حجمها اقل من 5mb!") 
    else:
        await msg.edit_text(f'**تم استخراج رابط تلجراف ميديا بنجاح!\n\n👻https://telegra.ph{response[0]}\n\nJoin  @Repthon**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Jsbot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("جاري استخراج الرابط...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("حجم الفيديو القصير يجب ان يكون اقل من 5mb!") 
    else:
        await msg.edit_text(f'**Your File Is Successfully Uploaded To Telegraph!\n\n👻https://telegra.ph{response[0]}\n\nJoin  @SLDeveloper**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Jsbot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("Uploading To Telegraph...")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("Gif size should be less than 5mb!") 
    else:
        await msg.edit_text(f'**تم استخراج رابط تلجراف ميديا بنجاح!\n\n👻https://telegra.ph{response[0]}\n\nJoin @Repthon**',
            disable_web_page_preview=False,
        )
    finally:
        os.remove(download_location)

@Jsbot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
Bot Started!
Join @Repthon
"""
)

Jsbot.run()
