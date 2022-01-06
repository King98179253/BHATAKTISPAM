import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5 ,STRING6 ,STRING7 ,STRING8 ,STRING9 ,STRING10
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RAID
from telegram import ParseMode


a = API_ID
b = API_HASH
smex = STRING
revill = STRING2
revilll = STRING3
revillll = STRING4
revilllll = STRING5
revilop = STRING6
revilopx = STRING7
revilopxx = STRING8
revilopxxx = STRING9
revilbotop = STRING10


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
rdk = ""
mdk = ""
fdk = ""
ldk = ""
xdk = ""


que = {}

SMEX_USERS = []
for x in SUDO:
    SMEX_USERS.append(x)
    
async def start_branded():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global rdk
    global mdk
    global fdk
    global ldk
    global xdk
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "BRANDED"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if revill:
        session_name = str(revill)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if revilll:
        session_name = str(revilll)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if revillll:
        session_name = str(revillll)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if revilllll:
        session_name = str(revilllll)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception as e:
            pass

    if revilop:
        session_name = str(revilop)
        print("String 6 Found")
        rdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await rdk.start()
            botme = await rdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        rdk = TelegramClient(session_name, a, b)
        try:
            await rdk.start()
        except Exception as e:
            pass  

    if revilopx:
        session_name = str(revilopx)
        print("String 7 Found")
        mdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await mdk.start()
            botme = await mdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        mdk = TelegramClient(session_name, a, b)
        try:
            await mdk.start()
        except Exception as e:
            pass  

    if revilopxx:
        session_name = str(revilopxx)
        print("String 8 Found")
        fdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await fdk.start()
            botme = await fdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        fdk = TelegramClient(session_name, a, b)
        try:
            await fdk.start()
        except Exception as e:
            pass 

    if revilopxxx:
        session_name = str(revilopxxx)
        print("String 9 Found")
        xdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await xdk.start()
            botme = await xdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        xdk = TelegramClient(session_name, a, b)
        try:
            await xdk.start()
        except Exception as e:
            pass 

    if revilbotop:
        session_name = str(revilbotop)
        print("String 10 Found")
        ldk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 10")
            await ldk.start()
            botme = await ldk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        ldk = TelegramClient(session_name, a, b)
        try:
            await ldk.start()
        except Exception as e:
            pass                                                                                                                 
    
loop = asyncio.get_event_loop()
loop.run_until_complete(start_revilbot())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass

ATMA_PIC = "https://telegra.ph/file/1892b78bacdeb91e47e94.jpg"
devs = [5043873192, 2126972900, 2132272170]

@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝘽𝙤𝙩 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        revilbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = revilbot[0]
            bc = int(bc)
            text = "YHA CHUTIYE RHETY H NIKLO YHA SE....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("ABB YHA SE NIKL KR JAAN M DAM AAYA")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
                
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝘽𝙤𝙩𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        revilbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(revilbot) == 2:
            message = str(revilbot[1])
            counter = int(revilbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:  
            counter = int(revilbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(revilbot[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@idk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.dspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.dspam <sleep time> <count> <message to spam>\n\n.dspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        smex = await e.get_reply_message()
        revilbot = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        revilbotisop = revilbot[1:]
        if len(revilbotisop) == 2:
            message = str(revilbotisop[1])
            counter = int(revilbotisop[0])
            sleeptime = float(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(revilbotisop[0])
            sleeptime = float(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(revilbotisop[0])
            sleeptime = float(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴 𝗕𝗼𝘁 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        revilbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(revilbot) == 2:
            message = str(revilbot[1])
            counter = int(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(revilbot[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = raid\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        brandedbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(brandedbot) == 2:
            message = str(brandedbot[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            if int(g) in devs:
                text = f"𝙎𝙍𝙔🥺 𝙏𝙃𝙄𝙎 𝙄𝙕 𝙈𝙊𝙄 𝙂𝙊𝘿🤲,𝙄 𝘼𝙈 𝙉𝙊𝙏 𝘼𝘽𝙐𝙎𝙄𝙉𝙂 𝙈𝙊𝙄 𝙂𝙊𝘿🙏."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO:
                text = f"This lodu is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(revilbot[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in devs:
                text = f"𝙎𝙍𝙔🥺 𝙏𝙃𝙄𝙎 𝙄𝙕 𝙈𝙊𝙄 𝙂𝙊𝘿🤲,𝙄 𝘼𝙈 𝙉𝙊𝙏 𝘼𝘽𝙐𝙎𝙄𝙉𝙂 𝙈𝙊𝙄 𝙂𝙊𝘿🙏."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO:
                text = f"This lodu is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(revilbot[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )





@idk.on(events.NewMessage(incoming=True))
@ydk.on(events.NewMessage(incoming=True))
@wdk.on(events.NewMessage(incoming=True))
@hdk.on(events.NewMessage(incoming=True))
@sdk.on(events.NewMessage(incoming=True))
@rdk.on(events.NewMessage(incoming=True))
@mdk.on(events.NewMessage(incoming=True))
@fdk.on(events.NewMessage(incoming=True))
@xdk.on(events.NewMessage(incoming=True))
@ldk.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.brandedraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.brandedraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.brandedraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.brandedraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.brandedraid"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.brandedraid"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.brandedraid"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.brandedraid"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.brandedraid"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.brandedraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 =BRANDED raid\n\nCommand:\n\n.brandedraid <Username of User>\n\n.brandedraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        revilbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(revilbot[0])
            a = await e.client.get_entity(message)
            g = a.id
            if int(g) in devs:
                text = f"𝙎𝙍𝙔🥺 𝙏𝙃𝙄𝙎 𝙄𝙕 𝙈𝙊𝙄 𝙂𝙊𝘿🤲,𝙄 𝘼𝙈 𝙉𝙊𝙏 𝘼𝘽𝙐𝙎𝙄𝙉𝙂 𝙈𝙊𝙄 𝙂𝙊𝘿🙏."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO:
                text = f"This lodu is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                nm = a.first_name
                que[g] = []
                qeue = que.get(g)
                appendable = [g]
                qeue.append(appendable)
                text = f"𝗔𝗕𝗕 𝗗𝗘𝗞𝗛𝗢 {nm} 𝗜𝗦𝗞𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗫𝗛𝗢𝗗 𝗧𝗔 𝗛𝗨"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in devs:
                text = f"𝙎𝙍𝙔🥺 𝙏𝙃𝙄𝙎 𝙄𝙕 𝙈𝙊𝙄 𝙂𝙊𝘿🤲,𝙄 𝘼𝙈 𝙉𝙊𝙏 𝘼𝘽𝙐𝙎𝙄𝙉𝙂 𝙈𝙊𝙄 𝙂𝙊𝘿🙏."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO:
                text = f"This lodu is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                nm = b.first_name
                que[g] = []
                qeue = que.get(g)
                appendable = [g]
                qeue.append(appendable)
                text = f"𝗔𝗕𝗕 𝗗𝗘𝗞𝗛𝗢 {nm} 𝗜𝗦𝗞𝗜 𝗠𝗔𝗔 𝗞𝗢 𝗫𝗛𝗢𝗗 𝗧𝗔 𝗛𝗨"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.bbrandedraid"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.bbrandedraid"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.bbrandedraid"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.bbrandedraid"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.bbrandedraid"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.bbrandedraid"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.bbrandedraid"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.bbrandedraid"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.bbrandedraid"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.bbrandedraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = B BRANDED raid\n\nCommand:\n\n.bbrandedraid <Username of User>\n\n.bbrandedraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        revilbot = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(revilbot[0])
            a = await e.client.get_entity(message)
            g = a.id
            nm = a.first_name
            try:
                queue = que.get(g)
                queue.pop(0)
                text = f"𝗠𝗔𝗖𝗛𝗔𝗥🎋 𝗞𝗜 𝗝𝗔𝗧𝗛 𝗝𝗔𝗞𝗥 😏𝗧𝗘𝗥𝗘 𝗠𝗔𝗔 𝗞𝗘 𝗕𝗢𝗢𝗕𝗦👙 𝗖𝗛𝗔𝗧🤤 {nm}"
                await e.reply(text, parse_mode=None, link_preview=None )
            except Exception as f:
                pass
            text = "𝗡𝗘𝗩𝗘𝗥 𝗔𝗖𝗧𝗜𝗩𝗔𝗧𝗘𝗗 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗥𝗔𝗜𝗗⚜️"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            nm = b.first_name
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
                text = f"𝗠𝗔𝗖𝗛𝗔𝗥🎋 𝗞𝗜 𝗝𝗔𝗧𝗛 𝗝𝗔𝗞𝗥 😏𝗧𝗘𝗥𝗘 𝗠𝗔𝗔 𝗞𝗘 𝗕𝗢𝗢𝗕𝗦👙 𝗖𝗛𝗔𝗧🤤{nm}"
                await e.reply(text, parse_mode=None, link_preview=None )
            except Exception as f:
                pass
            text = "𝗡𝗘𝗩𝗘𝗥 𝗔𝗖𝗧𝗜𝗩𝗔𝗧𝗘𝗗 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗥𝗔𝗜𝗗⚜️"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "ᴋɪsᴋɪ ɢɴᴅ ᴍᴀɪ ᴜɴɢʟɪ ᴅᴀʟɴɪ ʜ..!!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀\n▒█▀▀▄ ▒█░░▒█ ░▒█░░\n▒█▄▄█ ▒█▄▄▄█ ░▒█░░\n\n𝘽𝙍𝘼𝙉𝘿𝙀𝘿 Sᴘᴀᴍ BᴏT {nm} ᴋɪsᴋᴏ ᴘᴇʟᴜ ᴊᴀʟᴅɪ ʙᴏʟᴏ `{ms}` 𝗠𝗦")
    


@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝗥𝗲𝗯𝗼𝗼𝘁𝗲𝗱\n\n𝐏𝐋𝐄𝐀𝐒𝐄 𝐖𝐀𝐈𝐓..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await rdk.disconnect()
        except Exception as e:
            pass
        try:
            await mdk.disconnect()
        except Exception as e:
            pass
        try:
            await fdk.disconnect()
        except Exception as e:
            pass
        try:
            await ldk.disconnect()
        except Exception as e:
            pass   
        try:
            await xdk.disconnect()
        except Exception as e:
            pass                 
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

       
@idk.on(events.NewMessage(incoming=True, pattern=r"\.atma"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.atma"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.atma"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.atma"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.atma"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.atma"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.atma"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.atma"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.atma"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.atma"))
async def alive(event):
    if event.sender_id in SMEX_USERS:
        message_id = event.message.id
        try:
            text = "👅 𝘽𝙍𝘼𝙉𝘿𝙀𝘿 𝐒ᴘᴀ𝐌 𝐁ᴏ𝐓 [👅](https://telegra.ph/file/1892b78bacdeb91e47e94.jpg)\n\n\n ✧ 𝘽𝙃𝘼𝙏𝘼𝙆𝙏𝙄 𝘼𝙏𝙈𝘼 sᴘᴀᴍ BᴏT ɪs ᴀʟɪᴠᴇ ✧\n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➣ 𝗠𝗬 𝗖𝗥𝗘𝗔𝗧𝗘𝗥: 𝗕𝗛𝗔𝗧𝗔𝗞𝗧𝗜 𝗔𝗧𝗠𝗔👿/n ┣➣ 𝗖𝗢𝗪𝗡𝗘𝗥: 𝗕𝗥𝗔𝗡𝗗𝗘𝗗 𝗞𝗔𝗠𝗜𝗡𝗔👿\n ┣➣ sᴜᴘᴘᴏʀᴛ : [JOIN](https://t.me/SUBHI_WORLD)\n ┣➣ ᴄʀᴇᴀᴛᴇʀ : [𝗛𝗔𝗧𝗘𝗥𝗦 𝗖𝗔𝗟𝗟 𝗠𝗘 𝗗𝗔𝗗](https://t.me/zinda_h_tu_mere_liye_heart_hack)\n ┗━━━━━━━━━━━━━━━━━━━\n\n 🖤 [𝐑𝐄𝐏𝐎](https://t.me/zinda_h_tu_mere_liye_heart_hack) 🖤"
            event = await event.client.send_file(event.chat_id, EVIL_PIC, caption = text, reply_to=message_id, link_preview=None )
        except:
            text = "👅 𝘽𝙍𝘼𝙉𝘿𝙀𝘿 𝐒ᴘᴀ𝐌 𝐁ᴏ𝐓 [👅](https://telegra.ph/file/1892b78bacdeb91e47e94.jpg)\n\n\n ✧ 𝘽𝙃𝘼𝙏𝘼𝙆𝙏𝙄 𝘼𝙏𝙈𝘼 sᴘᴀᴍ BᴏT ɪs ᴀʟɪᴠᴇ ✧\n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➣ 𝙈𝙔 𝘾𝙍𝙀𝘼𝙏𝙀𝙍: 𝘽𝙃𝘼𝙏𝘼𝙆𝙏𝙄 𝘼𝙏𝙈𝘼👿/n ┣➣ 𝘾𝙊𝙒𝙉𝙀𝙍: 𝘽𝙍𝘼𝙉𝘿𝙀𝘿 𝙆𝘼𝙈𝙄𝙉𝘼👿\n ┣➣ sᴜᴘᴘᴏʀᴛ : [JOIN](https://t.me/SUBHI_WORLD)\n ┣➣ ᴄʀᴇᴀᴛᴇʀ : [𝗛𝗔𝗧𝗘𝗥𝗦 𝗖𝗔𝗟𝗟 𝗠𝗘 𝗗𝗔𝗗](https://t.me/zinda_h_tu_mere_liye_heart_hack)\n ┗━━━━━━━━━━━━━━━━━━━\n\n 🖤 [𝐑𝐄𝐏𝐎](https://t.me/zinda_h_tu_mere_liye_heart_hack) 🖤"
            event = await event.reply(text, link_preview=None )
        
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@rdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@mdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@fdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@xdk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ldk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
       text = "𝙐𝙎𝙀 𝘾𝙊𝙈𝙈𝙀𝙉𝘿𝙎[👅](https://telegra.ph/file/1892b78bacdeb91e47e94.jpg)\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.atma\n.ping\n.restart\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.spam\n.dspam\n.bigspam\n.raid\n.brandedraid\n.bbrandedraid\n\n\nFor more help regarding usage of plugins type plugins name"
       await e.reply(text, parse_mode=None, link_preview=None )

        

    
        
text = """ ✧══════•❁❀❁•══════✧

 



       """

print(text)
print("")
print("Congrats BHATAKTI ATMA MULTI SPAMBOT STARTED SUCCESSFULLY . TYPE .atma TO CHECK YOUR BOT'S STATUS")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        rdk.disconnect()
    except Exception as e:
        pass 
    try:
        mdk.disconnect()
    except Exception as e:
        pass
    try:
        fdk.disconnect()
    except Exception as e:
        pass 
    try:
        xdk.disconnect()
    except Exception as e:
        pass
    try:
        ldk.disconnect()
    except Exception as e:
        pass                  
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        rdk.run_until_disconnected()
    except Exception as e:
        pass 
    try:
        mdk.run_until_disconnected()
    except Exception as e:
        pass 
    try:
        fdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        xdk.run_until_disconnected()
    except Exception as e:
        pass 
    try:
        ldk.run_until_disconnected()
    except Exception as e:
        pass                 
