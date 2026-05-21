# =========================================
# FINAL 14 CHANNEL PREMIUM BOT
# PART 1
# =========================================

import sqlite3
import asyncio
from io import BytesIO

from telethon import TelegramClient, events
from telethon.errors.rpcerrorlist import DocumentInvalidError
from telethon.tl.types import (
    MessageEntityBold,
    MessageEntityCustomEmoji
)

# =========================================
# API DETAILS
# =========================================

API_ID = 31870265
API_HASH = "e95092bacee185ce3057f04571add1f4"
PHONE = "+917380846648"

# =========================================
# CHANNELS
# =========================================

ROYAL_CHANNEL = -1003952997125
BATMAN_CHANNEL = -1003547104852
BETTING_CHANNEL = -1003916068282
GAME_CHANNEL = -1003997751744

GUDDU_CHANNEL = -1003881659929
ROCKY_CHANNEL = -1003918338559
JACKY_CHANNEL = -1003918160838
PRIYANSHU_CHANNEL = -1003958352127
TOSSKING_CHANNEL = -1003921501439

# =========================================
# NEW CHANNELS
# =========================================

REDDY_CHANNEL = -1003950810258
SHIVA_CHANNEL = -1003933024704
RAHUL_CHANNEL = -1003971738837
ANGAD_CHANNEL = -1003815705852
KING_CHANNEL = -1003765912375
# =========================================
# ALL CHANNELS
# =========================================

CHANNELS = [

    ROYAL_CHANNEL,
    BATMAN_CHANNEL,
    BETTING_CHANNEL,
    GAME_CHANNEL,

    GUDDU_CHANNEL,
    ROCKY_CHANNEL,
    JACKY_CHANNEL,
    PRIYANSHU_CHANNEL,
    TOSSKING_CHANNEL,

    REDDY_CHANNEL,
    SHIVA_CHANNEL,
    RAHUL_CHANNEL,
    ANGAD_CHANNEL,
    KING_CHANNEL
]

# =========================================
# CLIENT
# =========================================

client = TelegramClient(
    "multi_channel_premium_bot",
    API_ID,
    API_HASH
)

# =========================================
# LEAGUE
# =========================================

CURRENT_LEAGUE = "INDIAN PREMIER LEAGUE 2026"

# =========================================
# MEMORY
# =========================================

toss_posts = []
match_posts = []

# =========================================
# PREMIUM IDS
# =========================================

PREMIUM = {

    "ARROW": 6301041417816901358,
    "DOWN": 5470177992950946662,
    "BOOM": 5276032951342088188,
    "BLUE_TICK": 5350486389806868244,
    "MONEY": 5346123450358444391,
    "ID": 5375452759820619214,
    "SIREN": 6257780484281997093,
    "WINNER": 5972223227055836399,
    "TROPHY": 6307442761628915191,
    "VERSUS": 5821153726718546992,
    "LIGHTNING": 6082621264000719714,
    "CROWN": 6129739490484294910,
    "THUMBS": 5215218645382211332,
    "MAIL": 6269255258212404947,
    "BATMAN": 5972022360025336988,
    "ROYALBLUE": 5976567925778158529,
    "MEDAL": 6269232765468676321,
    "PARTY": 5255706846815077966,

    # GAME
    "GAME_DOWN": 6156513311585211842,
    "GAME_ARROW": 5766887489243451304,
    "GAME_LIGHTNING": 6082621264000719714,
    "GAME_CROWN": 6300763696641607387,
    "GAME_PUNCH": 5470058558500382450,
    "GAME_PIN": 6300675228905244700,
    "GAME_VERSUS": 5348377204382251891,
    "GAME_BOOM_HAND": 5244814255701634298,
    "GAME_SYMBOL": 5458701355004735404,
    "GAME_CASH": 5472030678633684592,

    # GUDDU
    "GUDDU_CROWN": 5222368327116004404,
    "GUDDU_MONEY": 5427107837568360763,
    "GUDDU_CHECK": 6269219060228035378,
    "GUDDU_TICK": 5213287958798410406,

    # ROCKY
    "ROCKY_COIN": 5269254848703902904,
    "ROCKY_ROCKET": 5445284980978621387,
    "ROCKY_FIRE": 6116396139492152939,

    # JACKY
    "JACKY_STAR": 6269048584386122161,
    "JACKY_BOMB": 6084620910579420585,
    "JACKY_TARGET": 5350460637182993292,

    # PRIYANSHU
    "PRI_ARROW": 5253767677670862169,
    "PRI_BAT": 5346089086325130313,
    "PRI_GLOBE": 5231489647946768652,

    # TOSS KING
    "TOSS_MAIL": 5406631276042002796,
    "TOSS_CLOCK": 5215484787325676090,
    "TOSS_PIN": 5463054218459884779,

    # REDDY
    "REDDY_AIR": 6165465711352223465,
    "REDDY_POINT": 6185707729009512236,
    "REDDY_CHECK": 5206607081334906820,
    "REDDY_TICK": 6273749318717412886,
    "REDDY_ROTATE": 5375338737028841420,
    "REDDY_CART": 6300834821300029148,

    # SHIVA
    "SHIVA_COIN": 5269254848703902904,
    "SHIVA_MAIL": 5406631276042002796,
    "SHIVA_ARROW": 5253767677670862169,
    "SHIVA_POLICE": 5972223227055836399,

    # RAHUL
    "RAHUL_KISS": 5350501108659790021,
    "RAHUL_MONEY": 5224257782013769471,

    # ANGAD
    "ANGAD_DIAMOND": 5427168083074628963,
    "ANGAD_RED": 5438280696772711407,

    # KING
    "KING_LIGHTNING": 6082511510406436819,
}
# =========================================
# UTF16
# =========================================

def utf16_index(string, pos):

    return len(
        string[:pos].encode('utf-16-le')
    ) // 2

def utf16_length(string):

    return len(
        string.encode('utf-16-le')
    ) // 2

# =========================================
# PREMIUM ENTITIES
# =========================================

def premium_entities(text):

    entities = []

    entities.append(
        MessageEntityBold(
            offset=0,
            length=utf16_length(text)
        )
    )

    emoji_map = {

        # DEFAULT
        "➡️": PREMIUM["ARROW"],
        "👇": PREMIUM["DOWN"],
        "💥": PREMIUM["BOOM"],
        "☑️": PREMIUM["BLUE_TICK"],
        "🤑": PREMIUM["MONEY"],
        "🆔": PREMIUM["ID"],
        "🚨": PREMIUM["SIREN"],
        "🔻": PREMIUM["WINNER"],
        "🏆": PREMIUM["TROPHY"],
        "🆚": PREMIUM["VERSUS"],
        "⚡️": PREMIUM["LIGHTNING"],
        "👑": PREMIUM["CROWN"],
        "👍": PREMIUM["THUMBS"],
        "✉️": PREMIUM["MAIL"],
        "🔸": PREMIUM["BATMAN"],
        "💠": PREMIUM["ROYALBLUE"],
        "🎖️": PREMIUM["MEDAL"],
        "🥳": PREMIUM["PARTY"],

        # GAME
        "⏬": PREMIUM["GAME_DOWN"],
        "🔣": PREMIUM["GAME_SYMBOL"],
        "📌": PREMIUM["GAME_PIN"],
        "💸": PREMIUM["GAME_CASH"],
        "👉": PREMIUM["GAME_ARROW"],
        "👊": PREMIUM["GAME_PUNCH"],
        "🤜": PREMIUM["GAME_BOOM_HAND"],

        # GUDDU
        "✅": PREMIUM["GUDDU_TICK"],
        "✔️": PREMIUM["GUDDU_CHECK"],

        # ROCKY
        "🪙": PREMIUM["ROCKY_COIN"],
        "🚀": PREMIUM["ROCKY_ROCKET"],
        "🔥": PREMIUM["ROCKY_FIRE"],

        # JACKY
        "🤩": PREMIUM["JACKY_STAR"],
        "💣": PREMIUM["JACKY_BOMB"],
        "🎯": PREMIUM["JACKY_TARGET"],

        # PRIYANSHU
        "🏏": PREMIUM["PRI_BAT"],
        "🌐": PREMIUM["PRI_GLOBE"],

        # TOSS KING
        "🕐": PREMIUM["TOSS_CLOCK"],

        # REDDY
        "✈️": PREMIUM["REDDY_AIR"],
        "✔️": PREMIUM["REDDY_CHECK"],
        "🔄": PREMIUM["REDDY_ROTATE"],
        "🛒": PREMIUM["REDDY_CART"],

        # SHIVA
        "🪙": PREMIUM["SHIVA_COIN"],

        # RAHUL
        "😘": PREMIUM["RAHUL_KISS"],

        # ANGAD
        "🔴": PREMIUM["ANGAD_RED"],

        # KING
        "⚡️": PREMIUM["KING_LIGHTNING"],
    }

    for emoji, document_id in emoji_map.items():

        current = 0

        while True:

            pos = text.find(
                emoji,
                current
            )

            if pos == -1:
                break

            entities.append(

                MessageEntityCustomEmoji(

                    offset=utf16_index(
                        text,
                        pos
                    ),

                    length=utf16_length(
                        emoji
                    ),

                    document_id=document_id
                )
            )

            current = pos + len(emoji)

    return entities

# =========================================
# SAFE MEDIA SEND
# =========================================

async def send_media_safe(
    channel,
    reply_msg,
    caption
):

    entities = premium_entities(
        caption
    )

    try:

        return await client.send_file(

            channel,

            file=reply_msg.media,

            caption=caption,

            formatting_entities=entities,

            parse_mode=None
        )

    except DocumentInvalidError:

        media_stream = BytesIO()

        await reply_msg.download_media(
            file=media_stream
        )

        media_stream.seek(0)

        return await client.send_file(

            channel,

            file=media_stream,

            caption=caption,

            formatting_entities=entities,

            parse_mode=None
        )

# =========================================
# CHANNEL TYPE
# =========================================

def channel_type(channel):

    if channel == BATMAN_CHANNEL:
        return "BATMAN"

    if channel == BETTING_CHANNEL:
        return "BETTING"

    if channel == GAME_CHANNEL:
        return "GAME"

    if channel == GUDDU_CHANNEL:
        return "GUDDU"

    if channel == ROCKY_CHANNEL:
        return "ROCKY"

    if channel == JACKY_CHANNEL:
        return "JACKY"

    if channel == PRIYANSHU_CHANNEL:
        return "PRIYANSHU"

    if channel == TOSSKING_CHANNEL:
        return "TOSSKING"

    if channel == REDDY_CHANNEL:
        return "REDDY"

    if channel == SHIVA_CHANNEL:
        return "SHIVA"

    if channel == RAHUL_CHANNEL:
        return "RAHUL"

    if channel == ANGAD_CHANNEL:
        return "ANGAD"

    if channel == KING_CHANNEL:
        return "KING"

    return "ROYAL"

# =========================================
# LEAGUE CHANGE
# =========================================

@client.on(events.NewMessage(pattern='/league'))
async def league_handler(event):

    global CURRENT_LEAGUE

    CURRENT_LEAGUE = event.raw_text.replace(
        '/league',
        ''
    ).strip().upper()

    await event.reply(
        f"✅ LEAGUE CHANGED:\n{CURRENT_LEAGUE}"
    )
# =========================================
# TOSS POST
# =========================================

@client.on(events.NewMessage(pattern='/toss'))
async def toss_handler(event):

    team = event.raw_text.replace(
        '/toss',
        ''
    ).strip().upper()

    if not event.reply_to_msg_id:

        await event.reply(
            "REPLY TO PHOTO"
        )

        return

    reply_msg = await event.get_reply_message()

    ids = []

    for channel in CHANNELS:

        ctype = channel_type(channel)

        # =====================================
        # ROYAL
        # =====================================

        if ctype == "ROYAL":

            caption = f"""➡️ TOSS ➜ {team}
➡️ TOSS ➜ {team}

➡️ FIXED TOSS .....
➡️ GROUND FIXING TOSS.....
➡️ LIFE TIME LOSS COVER TOSS....
➡️ UNLIMITED LIMIT TOSS PLAY....

🌐𝐎𝐍𝐋𝐘 ➡️ROYALS WIN 💠"""

            promo = f"""Best Betting Site👇🏻

Only One Khelking vip id💯
http://wa.link/khelkingvipho

PLACE YOUR BETS INDIA'S MOST 
TRUSTED BOOK http://Www.Khelking.io 🔜"""

        # =====================================
        # BATMAN
        # =====================================

        elif ctype == "BATMAN":

            caption = f"""✉️ TOSS UPDATE ✉️

➡️TOSS ➜ {team}
➡️TOSS ➜ {team}

🔻 Fixed Toss .....
🔻 Group Fixed Toss.....
🔻 Life Time Cover Toss....
🔻 Unlimited Limit Toss Play....

ONLINE 🔸 BATMAN (Official) 💠"""

            promo = f"""{team} Will Win This Toss..!! 🤑✔️

🆔LELO YAHA SE OR LIMIT RADDY
RAKHO

ONLINE 🔸 BATMAN (Official) 💠"""

        # =====================================
        # GAME
        # =====================================

        elif ctype == "GAME":

            caption = f"""⏬ {CURRENT_LEAGUE} ⏬

TOSS:➡️ {team}
TOSS:➡️ {team}

🔣 100% Fix Report ✔️
🔣 No Limit Fixed Toss ✔️
🔣 Play Double Limit Toss ✔️

👉 GAME CHANGER ( Abhi ) ⚡️"""

            promo = f"""{team} WIN THE TOSS...

WAIT FOR BEST ENTRY

Loss Cut Book Set At 10P 💸💸

👉 GAME CHANGER ( Abhi ) 👑"""

        # =====================================
        # GUDDU
        # =====================================

        elif ctype == "GUDDU":

            caption = f"""👑 {CURRENT_LEAGUE} 👑

TOSS👉 {team}
TOSS👉 {team}

100000% SURE TOSS ✔️

NO LIMIT TOSS ✔️

BIG LIMIT SE PLAY KRO ✔️

Play With :- Guddu Pandit ✅"""

            promo = f"""Jitna Khel Sakte Ho Khelo....
With Max Amount...

{team} Will Win This Toss..!! 🤑✔️

YAHA SE OR LIMIT RADDY
RAKHO

Play With :- GUDDU PANDIT✅"""

        # =====================================
        # ROCKY
        # =====================================

        elif ctype == "ROCKY":

            caption = f"""🪙TOSS UPDATE 2026 🏆 ✉️

TOSS🔻 {team}
TOSS🔻 {team}

1000% TRUSTED TOSS 👮

NO LIMIT TOSS✔️

BIG LIMIT SE PLAY KRO

Rocky bhai (Trending King) ✅"""

            promo = f"""{team} Win This Toss...💯

If Everything Is Yours, Then There Is Only One Side Of The Coin, "Victory"✔️

Rocky bhai (Trending King) ✅"""

        # =====================================
        # JACKY
        # =====================================

        elif ctype == "JACKY":

            caption = f"""🤩 {CURRENT_LEAGUE} 🤩

TOSS👉 {team}
TOSS👉 {team}

100% FIX TOSS

PLAY YOUR MAX LIMIT 💵

MARKET KA BAAP KOUN 👇

𝐎𝐍𝐋𝐘 👉 JACKY FIXER ✅"""

            promo = f"""{team} WIN THE TOSS...

WAIT FOR BEST ENTRY

PLAY YOUR MAX LIMIT 💵

𝐎𝐍𝐋𝐘 👉 JACKY FIXER ✅"""

        # =====================================
        # PRIYANSHU
        # =====================================

        elif ctype == "PRIYANSHU":

            caption = f"""TOSS ➡️ {team}
TOSS ➡️ {team}

◆ Super Fix Toss ✓✓
◆ Ground Se Fix
◆ 100% Sure Toss hai..

ONLY 👉 PRIYANSHU BHAI 🏏 ✅"""

            promo = f"""{team} Win This Toss

100% SURE SHOT REPORT 🛒✔️

MATCH REPORT UPDATE SOON 🔜

ONLY 👉 PRIYANSHU BHAI 🏏 ✅️"""

        # =====================================
        # TOSS KING
        # =====================================

        elif ctype == "TOSSKING":

            caption = f"""✉️ TOSS UPDATE ✉️

TOSS👉 {team}
TOSS👉 {team}

NO LIMIT TOSS ✔️

1000% SURE TOSS ✔️

BIG LIMIT SE PLAY KRO ✔️

CALL 🔻 TOSS KING (Aditya) ✅"""

            promo = f"""{team} 100%WIN THE TOSS

WAIT FOR PERFECT ENTRY 🕐

CALL ➡️TOSS KING(Aditya)✅"""
        # =====================================
        # REDDY
        # =====================================

        elif ctype == "REDDY":

            caption = f"""✈️ Womens Premier League 2026 ✈️

TOSS👉 {team}
TOSS👉 {team}

NO LIMIT TOSS✅
BIG LIMIT SE PLAY ✅
1000% WIN THIS TOSS ✅
PLAY YOUR MAX AMOUNT ✅

OWNER 👉 ( Reddy Anna) ✅"""

            promo = f"""{team} WIN THE TOSS.

UPDATE SOON 🔜

WAIT FOR MATCH REPORT 🛒

OWNER 👉 ( Reddy Anna) ✅"""

        # =====================================
        # SHIVA
        # =====================================

        elif ctype == "SHIVA":

            caption = f"""🪙TOSS UPDATE 2026 🏆

✉️ {CURRENT_LEAGUE} ✉️

TOSS🔻 {team}
TOSS🔻 {team}

1000% TRUSTED TOSS 👮

NO LIMIT TOSS✔️

BIG LIMIT SE PLAY KRO✔️

ONLY🔻SHIVA REDDY ✅"""

            promo = f"""Play Your 50% Amount Every Toss

100% Fix Report ✔️

TOSS 🔻 {team}

Will Win This Toss..!! 🤑

ONLY🔻SHIVA REDDY ✅"""

        # =====================================
        # RAHUL
        # =====================================

        elif ctype == "RAHUL":

            caption = f"""🪙TOSS UPDATE 2026 🏆

✉️ {CURRENT_LEAGUE} ✉️

TOSS🔻 {team}
TOSS🔻 {team}

1000% TRUSTED TOSS 👮

NO LIMIT TOSS✔️

BIG LIMIT SE PLAY KRO✔️

ONLY🔻RAHUL DADA ✅"""

            promo = f"""{team} WIN THE TOSS

WAIT FOR BEST ENTRY 🕐

ONLY🔻RAHUL DADA ✅"""

        # =====================================
        # ANGAD
        # =====================================

        elif ctype == "ANGAD":

            caption = f"""TOSS UPDATE 2026 ✉️

TOSS🔻 {team}
TOSS🔻 {team}

NO LIMIT TOSS✔️

BIG LIMIT SE PLAY KRO✔️

1000% TRUSTED TOSS 👑

ONLY 🔻ANGAD DADA 💠"""

            promo = f"""{team} WILL WIN THIS TOSS ✔️

GROUND FIX REPORT ✉️

All ACTIVE WAIT FOR BEST

SABHI RADDY RAKHO LIMIT 🏆

ONLY 🔻ANGAD DADA 💠"""

        # =====================================
        # KING
        # =====================================

        elif ctype == "KING":

            caption = f"""UPDATED TOSS ✉️

✅{CURRENT_LEAGUE}✅

TOSS 👉 {team}
TOSS 👉 {team}

NO LIMIT TOSS✔️

BIG LIMIT SE PLAY KRO✔️

THE 👑 KING✔️
"""

            promo = f"""{team} WIN THE TOSS

WAIT FOR BEST ENTRY 🕐

THE 👑 KING✔️"""

        # =====================================
        # BETTING
        # =====================================

        else:

            caption = f"""➡️ TOSS UPDATE 2026 🏆

🎖️{CURRENT_LEAGUE}🎖️

TOSS👉 {team}
TOSS👉 {team}

100000% SURE TOSS

NO LIMIT TOSS✔️

BIG LIMIT SE PLAY KRO✔️

ONLY👉 [ BETTING KING ] ☑️"""

            promo = f"""Jitna Khel Sakte Ho Khelo....
With Max Amount...

{team} Win This TOSS..!! 🤑✔️"""

        msg = await send_media_safe(
            channel,
            reply_msg,
            caption
        )

        await client.send_message(
            channel,
            promo,
            reply_to=msg.id,
            formatting_entities=premium_entities(promo),
            parse_mode=None,
            link_preview=False
        )

        ids.append((channel, msg.id))

    toss_posts.append(ids)

    await event.reply("✅ TOSS POSTED")
# =========================================
# TOSS PASS
# =========================================

@client.on(events.NewMessage(pattern='/tpass'))
async def tpass_handler(event):

    if not toss_posts:
        return

    cmd = event.raw_text.split()

    if len(cmd) < 3:
        return

    team = cmd[1].upper()
    choice = cmd[2].upper()

    selected = toss_posts[-1]

    for channel, msg_id in selected:

        ctype = channel_type(channel)

        # =====================================
        # ROYAL
        # =====================================

        if ctype == "ROYAL":

            text = f"""{team} WON THE TOSS AND CALLED TO {choice} ✔️✔️

💥 BOOM 💥 BOOM 💥

TOSS PASS...✔️
PUNTER KHUS...✔️
HUM KHUS...✔️

ROYAL WIN ☑️"""

        # =====================================
        # BATMAN
        # =====================================

        elif ctype == "BATMAN":

            text = f"""{team} WON THE TOSS AND CALLED TO {choice} ✔️✔️

💥 BOOM 💥 BOOM 💥

PREMIUM PASS CONFIRM 🔥

BATMAN (Official) ☑️"""

        # =====================================
        # GAME
        # =====================================

        elif ctype == "GAME":

            text = f"""{team} WON THE TOSS AND DECIDED TO {choice} ✔️✔️

💥 BOOM 💥👊💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅✅
🔣Play Double Limit Toss ✔️

👉 GAME CHANGER ( Abhi ) 👑"""

        # =====================================
        # GUDDU
        # =====================================

        elif ctype == "GUDDU":

            text = f"""{team} WON THE TOSS AND DECIDED TO {choice} ✔️✔️

Back To Back pass 🔻

Back To Back pass 🔻

Play With :- GUDDU PANDIT✅"""

        # =====================================
        # ROCKY
        # =====================================

        elif ctype == "ROCKY":

            text = f"""{team} WON THE TOSS AND CALLED TO {choice} ✔️✔️

💥 BOOM 💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅

Rocky bhai (Trending King) ✔️"""

        # =====================================
        # JACKY
        # =====================================

        elif ctype == "JACKY":

            text = f"""{team} WON THE TOSS AND TO {choice} ✔️✔️

💣 BOOM 💣👍💣 BOOM 💣

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅️✅️
🔤Play Double Limit Toss ✔️

𝐎𝐍𝐋𝐘 👉 JACKY FIXER ✅"""

        # =====================================
        # PRIYANSHU
        # =====================================

        elif ctype == "PRIYANSHU":

            text = f"""{team} HAVE WON THE TOSS & ELECTED TO 🏏 {choice} FIRST ✔️

𝐓𝐎𝐒𝐒 𝐏𝐀𝐒𝐒

𝐁𝐎𝐎𝐌 💥 𝐁𝐎𝐎𝐌 💥 𝐁𝐎𝐎𝐌✔️
𝐁𝐎𝐎𝐌 💥 𝐁𝐎𝐎𝐌 💥 𝐁𝐎𝐎𝐌✔️

ONLY 👉 PRIYANSHU BHAI 🏏 ✅️"""

        # =====================================
        # TOSS KING
        # =====================================

        elif ctype == "TOSSKING":

            text = f"""{team} WON THE TOSS AND TO {choice} FIRST ✔️✔️

💥 BOOM 💥👊💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅✅
WAIT FOR PERFECT ENTRY 🕐

CALL ➡️TOSS KING(Aditya)✅"""
        # =====================================
        # REDDY
        # =====================================

        elif ctype == "REDDY":

            text = f"""🇮🇳 {team} 🇮🇳 WON THE TOSS AND TO {choice} ✔️✔️

💥 BOOM 💥👊💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅✅

WAIT FOR MATCH REPORT 🛒

OWNER 👉 ( Reddy Anna) ✅"""

        # =====================================
        # SHIVA
        # =====================================

        elif ctype == "SHIVA":

            text = f"""💥{team} 💥 WON THE TOSS AND DECIDED TO {choice} ✔️✔️

💥 BOOM 💥👊💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅

➡️Play Double Limit Toss ✔️

ONLY🔻SHIVA REDDY✅"""

        # =====================================
        # RAHUL
        # =====================================

        elif ctype == "RAHUL":

            text = f"""👉 {team} 👈𝗛𝗔𝗩𝗘 𝗪𝗢𝗡 𝗧𝗛𝗘 𝗧𝗢𝗦𝗦 & 𝗘𝗟𝗘𝗖𝗧𝗘𝗗 𝗧𝗢 {choice} 𝗙𝗜𝗥𝗦𝗧 ‼️

𝗧𝗢𝗦𝗦 𝗣𝗔𝗦𝗦🥳
𝗕𝗢𝗢𝗠 𝔹𝕆𝕆𝕄 🥳
𝐵𝑂𝑂𝑀 𝐁𝐎𝐎𝐌🥳

😘 RAHUL DADA 😘"""

        # =====================================
        # ANGAD
        # =====================================

        elif ctype == "ANGAD":

            text = f"""{team} WON THE TOSS AND DECIDED TO {choice} ✔️✔️

💥 BOOM 💥👊💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅✅

🔣Play Double Limit Toss ✔️

ONLY 🔻ANGAD DADA 💠"""

        # =====================================
        # KING
        # =====================================

        elif ctype == "KING":

            text = f"""💥 {team} 💥 WON THE TOSS AND DECIDED TO {choice} ✔️✔️

💥 BOOM 💥👊💥 BOOM 💥

FIX TOSS PASS
SURE TOSS PASS
LIFE TIME TOSS PASS

OPEN WORK TOSS PASS ✅✅

🔣Play Double Limit Toss ✔️

THE 👑 KING✔️"""

        # =====================================
        # BETTING
        # =====================================

        else:

            text = f"""{team} WON THE TOSS AND DECIDED TO {choice} ✔️✔️

BACK TO BACK PASS 💰

BETTING KING HAIN TO PROFIT HAIN ✅"""

        await client.send_message(
            channel,
            text,
            reply_to=msg_id,
            formatting_entities=premium_entities(text),
            parse_mode=None
        )

    await event.reply("✅ TOSS PASS POSTED")

# =========================================
# MATCH POST
# =========================================

@client.on(events.NewMessage(pattern='/match'))
async def match_handler(event):

    raw = event.raw_text.replace(
        '/match',
        ''
    ).strip()

    try:

        parts = raw.split(" w ")

        teams = parts[0]
        winner = parts[1]

        team1 = teams.split(" vs ")[0].upper()
        team2 = teams.split(" vs ")[1].upper()

    except:

        await event.reply(
            "USE:\n/match CSK vs RCB w CSK"
        )

        return

    if not event.reply_to_msg_id:
        return

    reply_msg = await event.get_reply_message()

    ids = []
    for channel in CHANNELS:

        ctype = channel_type(channel)

        # =====================================
        # ROYAL
        # =====================================

        if ctype == "ROYAL":

            text = f"""TODAY MATCH UPDATE 👇

🚨{CURRENT_LEAGUE}🚨

{team1} 🆚 {team2}

WINNER 🔻- {winner}

WAIT FOR BEST TRAINING ENTRY

TRADING KARENGE BAS 👍

ROYAL WIN ☑️"""

            promo1 = f"""{winner} Will Win This Match...!! 🤑✔️

🆔LELO YAHA SE OR LIMIT RADDY
RAKHO 👇

Plat at -- Www.Khelking.io"""

            promo2 = f"""{winner} WIN THE MATCH

For VIP Clients
wa.link/khelkingvipho

WAIT FOR BEST ENTRY

Ragister & Bet
Www.Khelking.io"""

        # =====================================
        # BATMAN
        # =====================================

        elif ctype == "BATMAN":

            text = f"""TODAY MATCH UPDATE 👇

⚡️ {CURRENT_LEAGUE} ⚡️

{team1} 🆚 {team2}

ONLY EXPERT TIPPING ☺️

WINNER 🔻- {winner}

WAIT FOR BEST TRAINING ENTRY

TRADING KARENGE BAS 👍

BATMAN (Official) ☑️"""

            promo1 = f"""{winner} Will Win This Match..!! 🤑✔️

🆔LELO YAHA SE OR LIMIT RADDY
RAKHO

ONLINE 🔸 BATMAN (Official) 💠"""

            promo2 = None

        # =====================================
        # GAME
        # =====================================

        elif ctype == "GAME":

            text = f"""📌 {CURRENT_LEAGUE} 📌

{team1} 🆚 {team2}

TV BAND REPORT....
TELEGRAM TOD REPORT.....

Winner ➡️ {winner}

Loss Cut Book Set At 10P

WAIT FOR BEST TRAINING ENTRY

👉 GAME CHANGER ( Abhi ) ⚡️"""

            promo1 = f"""{winner} WIN THE MATCH

WAIT FOR BEST ENTRY

Loss Cut Book Set At 10P 💸💸

👉 GAME CHANGER ( Abhi ) ⚡️"""

            promo2 = None

        # =====================================
        # GUDDU
        # =====================================

        elif ctype == "GUDDU":

            text = f"""👑 {CURRENT_LEAGUE} 👑

Welcome To Real Profit ✉️

{team1} 🆚 {team2}

Tv Band Report....
Telegram Tod Report....

Winner🏆 - {winner}

Loss Cut Book Set At 10P

WAIT FOR BEST TRAINING ENTRY

BOOK SET CAMPLSRY LOW ODDS ✓

Play With :- GUDDU PANDIIT✅"""

            promo1 = f"""Jitna Khel Sakte Ho Khelo....
With Max Amount...

{winner} Will Win This MATCH..!! 🤑✔️

YAHA SE OR LIMIT RADDY
RAKHO 👇

Play With :- GUDDU PANDIT✅"""

            promo2 = None

        # =====================================
        # ROCKY
        # =====================================

        elif ctype == "ROCKY":

            text = f"""🚀Welcome To Real Profit 🚀

👑 {CURRENT_LEAGUE} 👑

{team1} 🆚 {team2}

Tv Band Report....
Telegram Tod Report....

Winner🏆 - {winner}

Loss Cut Book Set At 10P

WAIT FOR BEST ENTRY

TREDING ENTRY

Rocky bhai (Trending King) 💠"""

            promo1 = f"""{winner} Win This MATCH 💯

If Everything Is Yours, Then There Is Only One Side Of The Coin, "Victory"✔️

Rocky bhai (Trending King) ✅"""

            promo2 = None
        # =====================================
        # JACKY
        # =====================================

        elif ctype == "JACKY":

            text = f"""🆘{CURRENT_LEAGUE}🆘

{team1} 🆚 {team2}

TV BAND REPORT....
TELEGRAM TOD REPORT.....

Winner ➡️ {winner}

Loss Cut Book Set At 10P

WAIT FOR

BEST TRAINING ENTRY

Only 🔻 JACKY FIXER ✔️"""

            promo1 = f"""{winner} THE MATCH

WAIT FOR BEST ENTRY

Loss Cut Book Set

Only 🔻 JACKY FIXER ✔️"""

            promo2 = None

        # =====================================
        # PRIYANSHU
        # =====================================

        elif ctype == "PRIYANSHU":

            text = f"""🌐 {CURRENT_LEAGUE} 🌐

Tv Band Report....

{team1} 🆚 {team2}

Telegram Tod Report....

Winner🏆 - {winner}

Loss Cut Book Set At 10P

WAIT FOR BEST TRAINING ENTRY

BOOK SET CAMPLSRY LOW ODDS ✓

Play With :- PRIYANSHU BHAI ✅"""

            promo1 = f"""Play With Your Max Amount...

{winner} Will Win This MATCH..!! 🤑✔️

YAHA SE OR LIMIT RADDY
RAKHO

Play With :- PRIYANSHU BHAI ✅"""

            promo2 = None

        # =====================================
        # TOSS KING
        # =====================================

        elif ctype == "TOSSKING":

            text = f"""✔️{CURRENT_LEAGUE}✔️

MATCH NUMBER : 15th

{team1} 🆚 {team2}

Match WINNER 🔻 {winner}
Match WINNER 🔻 {winner}

🌡 Sure Match.
Note :- Book Set At Low Rate ✔️

Note :- For Next Update Channel Unmute & Pin To Top 📌

CALL 🔻 TOSS KING (Aditya) ✅"""

            promo1 = f"""{winner} 100%WIN THE MATCH

WAIT FOR PERFECT ENTRY 🕐

CALL ➡️TOSS KING(Aditya)✅"""

            promo2 = None

        # =====================================
        # REDDY
        # =====================================

        elif ctype == "REDDY":

            text = f"""🔄 {CURRENT_LEAGUE} 🔄

Tv Band Report....

{team1} 🆚 {team2}

Telegram Fix Report

Final Match Winner Ready ✔️

Winner🏆 - {winner}

Loss Cut Book Set At 10P

WAIT FOR BEST TRAINING ENTRY

BOOK SET CAMPLSRY LOW ODDS.✓

OWNER 👉 ( Reddy Anna) ✅"""

            promo1 = f"""{winner} This MATCH

100% SURE SHOT REPORT 🛒✔️

MATCH REPORT UPDATE SOON 🔜

ONLY 👉 REDDY ANNA 🏏 ✅️"""

            promo2 = None

        # =====================================
        # SHIVA
        # =====================================

        elif ctype == "SHIVA":

            text = f"""👑 {CURRENT_LEAGUE} 👑

{team1} 🆚 {team2}

Match 🔻 {winner}

100% TRUSTED MATCH ANALYSIS

WAIT FOR NEXT ENTRY 💯

ONLY🔻SHIVA REDDY ✅"""

            promo1 = f"""{winner} WIN THE MATCH

WAIT FOR BEST ENTRY 🕐

ONLY 🔻SHIVA REDDY ✅"""

            promo2 = None

        # =====================================
        # RAHUL
        # =====================================

        elif ctype == "RAHUL":

            text = f"""🏆 MENS UNDER 19 WOULD CUP 2026 🏆

{team1} 🆚 {team2}

Match ✔️- {winner}

India’s No.1 Analyst 🏏

Cricket Analysis & Treding Specialist
Jackpot king Treding Style Best Work

15-20P Bookset Compulsory 💰

WAIT FOR NEXT ENTRY ✅

ONLY RAHUL DADA ✅"""

            promo1 = f"""{winner} THE MATCH

WAIT FOR BEST ENTRY 🕐

ONLY ➡️ RAHUL DADA ✅"""

            promo2 = None
        # =====================================
        # ANGAD
        # =====================================

        elif ctype == "ANGAD":

            text = f"""MATCH UPDATE 🔴

👑 {CURRENT_LEAGUE} 👑

Welcome To Real Profit ✉️

{team1} 🆚 {team2}

Tv Band Report....
Telegram Tod Report....

Winner🏆 - {winner}

Loss Cut Book Set At 10P

WAIT FOR BEST TRAINING ENTRY

BOOK SET CAMPLSRY LOW ODDS.✓

ONLY 🔻ANGAD DADA 💠"""

            promo1 = f"""JITNA KHEL SAKTE HO KHELO....
WITH MAX AMOUNT...

{winner} Will Win This MATCH..!! 🤑✔️

YAHA SE OR LIMIT RADDY
RAKHO 👇

ONLY 🔻 ANGAD DADA 💠"""

            promo2 = None

        # =====================================
        # KING
        # =====================================

        elif ctype == "KING":

            text = f"""🏆 {CURRENT_LEAGUE} 🏆

{team1} 🆚 NEW ZEALAND

Match ✔️- {winner}

India’s No.1 Analyst 🏏

Cricket Analysis & Treding Specialist
Jackpot king Treding Style Best Work

15-20P Bookset Compulsory 💰

WAIT FOR NEXT ENTRY ✅

THE 👑 KING✔️

"""

            promo1 = f""" ⚡️
{winner} WIN THE MATCH

WAIT FOR BEST ENTRY 🕐

THE 👑 KING✔️"""

            promo2 = None

        # =====================================
        # BETTING
        # =====================================

        else:

            text = f"""👑 {CURRENT_LEAGUE} 👑

Tv Band Report....

{team1} 🆚 {team2}

Telegram Tod Report....

Winner🏆 - {winner}

Loss Cut Book Set At 10P

WAIT FOR BEST TRAINING ENTRY

BOOK SET CAMPLSRY LOW ODDS ✓✅

Play With :- @BettingKiings ☑️"""

            promo1 = f"""Jitna Khel Sakte Ho Khelo....
With Max Amount...

{winner} Will Win This Match..!! 🤑✔️

🆔LELO YAHA SE OR LIMIT RADDY
RAKHO

Play With :- @BettingKiings ☑️"""

            promo2 = None

        msg = await send_media_safe(
            channel,
            reply_msg,
            text
        )

        await client.send_message(
            channel,
            promo1,
            reply_to=msg.id,
            formatting_entities=premium_entities(promo1),
            parse_mode=None
        )

        if promo2:

            await client.send_message(
                channel,
                promo2,
                reply_to=msg.id,
                formatting_entities=premium_entities(promo2),
                parse_mode=None
            )

        ids.append((channel, msg.id))

    match_posts.append(ids)

    await event.reply("✅ MATCH POSTED")
# =========================================
# MATCH PASS
# =========================================

@client.on(events.NewMessage(pattern='/mpass'))
async def mpass_handler(event):

    if not match_posts:
        return

    cmd = event.raw_text.split(maxsplit=2)

    if len(cmd) < 3:
        return

    team = cmd[1].upper()
    result = cmd[2].upper()

    selected = match_posts[-1]

    for channel, msg_id in selected:

        ctype = channel_type(channel)

        # =====================================
        # ROYAL
        # =====================================

        if ctype == "ROYAL":

            text = f"""{team} WIN BY {result} 🏆

🤜 B O O M B O O M 🤜

ROYALS WIN KE SATH ONLY PROFIT 🏆

AGEN FUCK ALL MARKET 🤑

ROYALS WIN ☑️"""

        # =====================================
        # BATMAN
        # =====================================

        elif ctype == "BATMAN":

            text = f"""{team} WON BY {result} ✅

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

BATMAN (Official) ☑️"""

        # =====================================
        # GAME
        # =====================================

        elif ctype == "GAME":

            text = f"""{team} WON BY {result} 🏆

🤜B O O M B O O M🤜

GAME CHANGER ABHI KE SATH ONLY PROFIT 🏆

AGEN FUCK ALL MARKET 🤑

GAME CHANGER ABHI ⚡️"""

        # =====================================
        # GUDDU
        # =====================================

        elif ctype == "GUDDU":

            text = f"""{team} won by {result}

ONLY ON PROFIT 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

GUDDU PANDIT ✅"""

        # =====================================
        # ROCKY
        # =====================================

        elif ctype == "ROCKY":

            text = f"""{team} WIN BY {result} ✅

Back-to-Back Match PASS 💥🔥

Market mein sirf naam hi nahi… kaam bhi bolta hai 💯

Poora market ek taraf…
Apka bhai Akele 😎👑

Kyon pade ho chakkaron mein?
Koi nahi hai takkar mein! 💪🔥

Rocky bhai (Trending King) 💠"""

        # =====================================
        # JACKY
        # =====================================

        elif ctype == "JACKY":

            text = f"""{team} WON BY {result} ✅

🎯 Exact Match Prediction Passed 💯

🔥 Another Successful Call 🔥

💵 Profit Done For Premium Members 💵

Only 🔻 JACKY FIXER ✔️"""

        # =====================================
        # PRIYANSHU
        # =====================================

        elif ctype == "PRIYANSHU":

            text = f"""{team} WIN BY {result}

🤜B O O M B O O M🤜

PRIYANSHU BHAI KE SATH ONLY PROFIT 🏆

SUPRE SURE MATCH
ONLY ONE IN MARKET
AGEN FUCK ALL MARKET 🤑

PRIYANSHU BHAI ✅"""

        # =====================================
        # TOSS KING
        # =====================================

        elif ctype == "TOSSKING":

            text = f"""🏏 {team} WON BY {result} ✅️

Match Passed 💯

Another Successful Call 🔥

Profit Done For Premium Members 💵

CALL ➡️TOSS KING(Aditya)✅"""
        # =====================================
        # REDDY
        # =====================================

        elif ctype == "REDDY":

            text = f"""{team} WIN BY {result}

🤜B O O M B O O M🤜

SUPRE SURE MATCH
ONLY ONE IN MARKET
AGEN FUCK ALL MARKET 🤑

REDDY ANNA ✅"""

        # =====================================
        # SHIVA
        # =====================================

        elif ctype == "SHIVA":

            text = f"""{team} WON BY {result}🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🇺🇿 Happy for Win🇺🇿

✅ All Market Fail
✅ Bane raho aur profit karo.....

ONLY🔻SHIVA REDDY ✅"""

        # =====================================
        # RAHUL
        # =====================================

        elif ctype == "RAHUL":

            text = f"""{team} WIN BY {result}

ONLY PROFIT 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

✅ Boom Boom Boom…
✅ Full Market Fail…
✅ Always Profit With Me.....

ONLY ➡️ RAHUL DADA ✅"""

        # =====================================
        # ANGAD
        # =====================================

        elif ctype == "ANGAD":

            text = f"""{team} WON BY {result} 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

✔️ Boom Boom Boom…
✔️ Full Market Fail…
✔️ Always Profit With Me.....

ONLY 🔻ANGAD DADA 💠"""

        # =====================================
        # KING
        # =====================================

        elif ctype == "KING":

            text = f"""{team} WIN BY {result}

ONLY PROFIT 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

✅ Boom Boom Boom…
✅ Full Market Fail…
✅ Always Profit With Me.....

THE 👑 KING✔️"""

        # =====================================
        # BETTING
        # =====================================

        else:

            text = f"""{team} WIN BY {result} 🏆

BETTING KING KE SATH ONLY PROFIT 🏆

AGEN FUCK ALL MARKET🥳

💥 Back to Back Pass 💥

🏆🏆Jeet Mubarak 🏆🏆

✅ Boom Boom Boom…
✅ Full Market Fail…
✅ Always Profit With Me.....

BETTING KING ☑️"""

        await client.send_message(
            channel,
            text,
            reply_to=msg_id,
            formatting_entities=premium_entities(text),
            parse_mode=None
        )

    await event.reply("✅ MATCH PASS POSTED")

# =========================================
# START BOT
# =========================================

async def main():

    attempts = 5

    for attempt in range(attempts):

        try:

            await client.start(
                phone=PHONE
            )

            break

        except sqlite3.OperationalError as exc:

            if 'database is locked' not in str(exc).lower():
                raise

            print("DATABASE LOCKED... RETRYING...")

            await asyncio.sleep(2)

    print("FINAL 14 CHANNEL PREMIUM BOT STARTED ✅")

    await client.run_until_disconnected()

asyncio.run(main())
