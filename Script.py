class script(object):
    START_TXT = """๐๐ข๐ช ๐๐ฅ๐ ๐ฌ๐ข๐จ {},๐๐จ๐๐ ๐คฉ,๐ก๐ถ๐ฐ๐ฒ ๐ง๐ผ ๐ ๐ฒ๐ฒ๐ ๐ฌ๐ผ๐๐

๐จ'๐ ๐๐๐๐ ๐บ ๐๐๐๐๐๐พ ๐๐๐พ - ๐ฟ๐๐๐ผ๐๐๐๐๐พ๐ฝ ๐บ๐๐๐๐ฟ๐๐๐๐พ๐ ๐ป๐๐
๐๐๐ ๐ฆ๐ถ๐บ๐ฝ๐น๐ฒ ๐ง๐ผ ๐จ๐๐ฒ ๐ ๐ฒ..โบ๏ธ,๐๐๐๐ ๐๐ฑ๐ฑ ๐ ๐ฒ ๐ง๐ผ ๐ฌ๐ผ๐๐ฟ ๐๐ฟ๐ผ๐๐ฝ ๐๐ ๐๐ฑ๐บ๐ถ๐ป,๐ง๐ต๐ฎ๐๐ ๐๐น๐น ๐ ๐ช๐ถ๐น๐น ๐ฃ๐ฟ๐ผ๐๐ถ๐ฑ๐ฒ ๐ ๐ผ๐๐ถ๐ฒ๐ ๐ง๐ต๐ฒ๐ฟ๐ฒ..๐ฅฐ

ยฉ๏ธMแดษชษดแดแดษชษดแดD Bส: <a href=https://t.me/MagnusTG>๐ดagnus TG ๐ฎ๐ณ</a>"""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐๐ท๐ด ๐ท๐ด๐ป๐ฟ ๐ต๐พ๐ ๐ผ๐ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """โช ๐ด๐ ๐๐๐๐ : {}
โช ๐ช๐๐๐๐๐๐ : <a href=https://t.me/MagnusTG>๐ดagnus TG ๐ฎ๐ณ</a>
โช ๐ณ๐๐๐๐๐๐ : <a href=https://docs.pyrogram.org/>๐ท๐๐๐พ๐ถ๐๐ฐ๐ผ ๐</a>
โช ๐บ๐๐๐๐๐ ๐ช๐๐๐ : <a href=https://t.me/MyGithubSorceCode> ๐ช๐ป๐ธ๐ฒ๐บ ๐ฏ๐ด๐๐ด</a>
โช ๐ช๐๐๐๐๐๐ :<code> ๐ด๐๐๐๐ข๐๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐ข </code>
โช ๐ณ๐๐๐๐๐๐๐ : ๐ท๐๐๐ท๐พ๐ฝ ๐น
โช ๐ซ๐๐๐ ๐๐๐๐ : <a href=https://www.mongodb.com>๐ด๐พ๐ฝ๐ถ๐พ ๐ณ๐ฑ</a>
โช ๐ฉ๐๐ ๐๐๐๐๐๐ : <a href=https://dashboard.heroku.com/>๐ฏ๐ด๐๐พ๐บ๐</a>
โช ๐ฉ๐๐๐๐ ๐บ๐๐๐๐๐ : <code> v2.0.1 [ ๐ฑ๐ด๐๐ฐ ] </code>

๐ ๐ธ๐๐๐๐: เดเดฐเตเด เดชเตเดเดฟเดเตเดเตเดฃเตเด เดเดฒเตเดฒเดพเดตเตผเดเตเดเตเด เดเดฟเดเตเดเตเด"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://t.me/MyGithubSorceCode 

<b>DEVS:</b>
- <a href=https://t.me/MagnusTG>Magnus TG ๐ฎ๐ณ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    CORONA_TXT ="""<b>Here is the help for the coron information module</b>
  /covid <code>(countryname)</code> <b>you can find a corona information of every country</b>

  <b>example</b> : - /covid India"""
    STICKER_TXT ="""<b>COMMAND /stickerid\n๐จ๐ฟ ๐ธ๐๐ ๐ญ๐พ๐พ๐ฝ ๐ณ๐พ๐๐พ๐๐๐บ๐ ๐ฒ๐๐๐ผ๐๐พ๐ ๐จ๐ฝ ๐ข๐๐๐ผ๐ /stickerid ๐ณ๐ ๐ฆ๐พ๐ ๐ฒ๐๐๐ผ๐๐พ๐ ๐จ๐ฝ (๐ฑ๐พ๐๐๐ ๐ถ๐๐๐ ๐ฒ๐๐๐ผ๐๐พ๐)</b>"""
    PIN_TXT ="""<b>PIN MODULE</b>

<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>๐ Commands & Usage:</b>

โ /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members

โ /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>๐ฒ NOTHING MUCH JUST SOME FUN THINGS</b>
t๐๐ ๐๐๐๐ ๐ฎ๐๐: 
๐ฃ. /dice - Roll The Dice 
๐ค. /Throw ๐๐ /Dart - ๐ณ๐ ๐ฌ๐บ๐๐พ Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
โข /paste [text] - paste the given text on Pasty
โข /paste [reply] - paste the replied text on Pasty

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
โข /imdb  - get the film information from IMDb source.
โข /search  - get the film information from various sources.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข More search tools can be found on inline.
โข Those commands works on both pm and group."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
โข /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
โข /id - get id of a specifed user.
โข /info  - get information about a user.
โข /json - get the json details of a message.

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
โข /id - <code>get id of a specifed user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code>
โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code>
โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ
โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
