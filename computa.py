import asyncio
from discord.ext import commands
import discord
import sys, time, os
import webbrowser as wb
import pyautogui
from discord import FFmpegPCMAudio
from gtts import gTTS
import requests
import conf

activity = discord.Activity(type=discord.ActivityType.watching, name=f"Lunar's PC||{conf.PREFIX}help")

bot = commands.Bot(command_prefix=conf.PREFIX,
                   activity = activity,
                   help_command=None,
                   case_insensitive=True,
                   intents=discord.Intents.all())

host = conf.HOSTNAME # ex: C:/Users/sajun/Downloads/computa.py

def restart_bot(): 
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.event
async def on_ready():
    print(f"Logged In As {bot.user.name}")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def rickroll(ctx: commands.Context):
    wb.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    await ctx.reply("***Opened a rickroll link***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def msgbox(ctx: commands.Context, * ,text: str):
    await ctx.reply("***Opened a messagebox***")
    pyautogui.alert(text=text, title=f'Message from {ctx.author.display_name}', button='OK')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cmdprompt(ctx: commands.Context):
    await ctx.reply("***Opened Command Prompt***")
    os.startfile("cmd.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def calc(ctx: commands.Context):
    await ctx.reply("***Opened calculator***")
    os.startfile("calc.exe")

@bot.command() 
@commands.cooldown(1, 10, commands.BucketType.user)
async def youtube(ctx: commands.Context):
    wb.open_new("https://www.youtube.com")
    await ctx.reply("***Opened Youtube.com***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def roblox(ctx: commands.Context):
    wb.open_new("https://www.roblox.com")
    await ctx.reply("***Opened roblox.com***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def uselessfacts(ctx: commands.Context):
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    response = requests.get(url)
    await ctx.reply(response.json()["text"])

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def google(ctx: commands.Context, *, text: str):
    wb.open_new(f"https://www.google.com/search?q={text}")
    await ctx.reply("***Searched for {} on Google.***".format(text))

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def translate(ctx: commands.Context, lang1: str, lang2: str, *, text: str):
    wb.open_new(f"https://translate.google.com/?sl={lang1}&tl={lang2}&text={text}&op=translate")
    await ctx.reply("***Opened Google Translate.***")
  
@bot.command(pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def speak(ctx: commands.Context, *, text: str):
    language = 'en'
    tts = gTTS(text=f'{text}', lang=language, slow=False)
    tts.save("tts.mp3")
    source = FFmpegPCMAudio('tts.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("playing audio...")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 15 seconds
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects
        await os.remove("tts.mp3") # deletes tts.mp3

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ytsearch(ctx: commands.Context,*,text: str):
    wb.open_new(f"https://www.youtube.com/results?search_query={text}")
    await ctx.reply("***Opened Youtube Search***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def error(ctx: commands.Context, * ,text: str):
    await ctx.reply("***Opened an Error Window***")
    pyautogui.alert(text=text, title='Error 404', button='OK')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def lunarclient(ctx: commands.Context):
    await ctx.reply("***Opened Lunar Client***")
    os.startfile(f"C:/Users/{host}/Desktop/Lunar Client.lnk")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def autoclicker(ctx: commands.Context):
    await ctx.reply("***Opened AutoClicker***")
    os.startfile(f"C:/Users/{host}/Downloads/AutoClicker.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def edgewindow(ctx: commands.Context):
    await ctx.reply("***Opened new Edge window***")
    os.startfile("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def history(ctx: commands.Context):
    await ctx.reply("***Opened Search History***")
    pyautogui.hotkey("ctrl","h")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def snake(ctx: commands.Context):
    wb.open_new("https://www.google.com/search?q=snake+google")
    await ctx.reply("***Opened Google Snake***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def notepad(ctx: commands.Context, * , text: str):
    await ctx.reply("***Opened NotePad***")
    os.startfile("notepad.exe")
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(f'{text}')



@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def tab(ctx: commands.Context):
    wb.open_new_tab(url="edge://newtab")
    await ctx.reply("***Opened New Tab***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def devtools(ctx: commands.Context):
    pyautogui.hotkey("ctrl","shift","i")
    await ctx.reply("***Opened Dev Tools***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def minecraft(ctx: commands.Context):
    await ctx.reply("***Opened Minecraft Launcher***")
    os.startfile(f"C:/Users/{host}/Downloads/Minecraft Installer.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def screenshot(ctx: commands.Context):
    pyautogui.screenshot()
    pyautogui.screenshot('screenshot.png')
    file = discord.File("screenshot.png")
    await ctx.send(file=file, content=f"{ctx.author.mention}'s Screenshot of Wextra's PC")
    time.sleep(1)
    await os.remove("screenshot.png")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def robloxsearch(ctx: commands.Context, ID: str):
    wb.open_new(f"https://www.roblox.com/users/{ID}/profile")
    await ctx.reply("***Opened Roblox Search***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def maps(ctx: commands.Context):
    await ctx.reply("***removed due to potential privacy issues (might come back in future update)***")
    #wb.open_new(f"https://www.google.com/maps/dir///{address}")
    # await ctx.reply("***Opened Google Maps***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def url(ctx: commands.Context, page_url: str):
    wb.open_new(url=page_url)
    await ctx.reply(f"***Opened {page_url}***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def vup(ctx: commands.Context, *, amount: int):
    for _ in range(amount / 2):
        pyautogui.hotkey("volumeup")
    await ctx.reply("***Increased Volume by {}***".format(amount))

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def vdown(ctx: commands.Context, *, amount: int):
    for _ in range(amount / 2):
        pyautogui.hotkey("volumedown")
    await ctx.reply("***Decreased Volume by {}***".format(amount))

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def downloads(ctx: commands.Context):
    pyautogui.hotkey("ctrl","j")
    await ctx.reply("***Opened Downloads***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def pcdownloads(ctx: commands.Context):
    os.startfile(f"C:/Users/{host}/Downloads")
    await ctx.reply("***Opened Downloads***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def bup(ctx: commands.Context, *, amount: int):
    for _ in range(amount / 2):
        pyautogui.hotkey("f3")
    await ctx.reply("***Increased Brightness by {}***".format(amount))

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def bdown(ctx: commands.Context, *, amount: int):
    for _ in range(amount / 2):
        pyautogui.hotkey("f2")
    await ctx.reply("***Decreased Brightness by {}***".format(amount))

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def taskmanager(ctx: commands.Context):
    await ctx.reply("***Opened Task Manager***")
    os.startfile("taskmgr.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def robloxlauncher(ctx: commands.Context):
    await ctx.reply("***Opened Roblox Launcher***")
    os.startfile("RobloxPlayerLauncher.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def bcalc(ctx: commands.Context, * , firstnumber: str, secondnumber: str):
    await ctx.reply("***Opened Browser Calculator***")
    wb.open_new(f"https://www.google.com/search?q={firstnumber}+{secondnumber}")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def close(ctx: commands.Context):
    await ctx.reply("***Closed the current window***")
    pyautogui.hotkey("alt","f4")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def hotkey(ctx: commands.Context,*,k1: str, k2: str):
    await ctx.reply(f"***Successfully Clicked {k1} + {k2}***")
    pyautogui.hotkey(f"{k1}",f"{k2}")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def usertype(ctx: commands.Context, *, text: str):
    pyautogui.write(text)
    pyautogui.hotkey("enter")
    await ctx.reply(f"***Made The Host Type {text}***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ngrams(ctx: commands.Context, * , text: str):
    wb.open_new(f"https://books.google.com/ngrams/graph?content={text}")
    await ctx.reply("***Opened Google Ngrams***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def timer(ctx: commands.Context):
    await ctx.reply("***Opened Timer***")
    os.startfile("timer.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def restart(ctx: commands.Context):
    id = str(ctx.author.id)
    if id == conf.USER_ID:
        await ctx.reply('Restarting...')
        restart_bot()
    else:
        await ctx.send("You arent the owner of the bot silly dumbass!")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ytvideo(ctx: commands.Context, id: str):
    wb.open_new(f"https://www.youtube.com/watch?v={id}")
    await ctx.reply("***Opened A Youtube Video***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def rule34(ctx: commands.Context, *, tag: str):
    wb.open_new(f"https://rule34.xxx/index.php?page=post&s=list&tags={tag}")
    await ctx.reply(f"***Searched {tag} on rule34.xxx***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def pornhub(ctx: commands.Context, *, query: str):
    wb.open_new(f"https://www.pornhub.com/video/search?search={query}")
    await ctx.reply(f"***Searched {query} On pornhub.com***")

@bot.command()
async def help(ctx: commands.Context):

    embed = discord.Embed(color=0x0BA8B4, title="Help")
    embed.add_field(name="help", value="shows this page", inline=True)


    embed1 = discord.Embed(color=0x0BA8B4, title="App Commands")
    embed1.add_field(name="autoclicker", value="opens autoclicker", inline=True)
    embed1.add_field(name="cmdprompt", value="opens command prompt", inline=True)
    embed1.add_field(name="devtools", value="opens devtools", inline=True)
    embed1.add_field(name="error", value="opens a error window", inline=True)
    embed1.add_field(name="minecraft", value="opens minecraft", inline=True)
    embed1.add_field(name="roblox launcher", value="opens roblox launcher", inline=True)
    embed1.add_field(name="lunarclient", value="opens lunarclient", inline=True)
    embed1.add_field(name="calc", value="opens calculator", inline=True)
    embed1.add_field(name="timer", value="opens timer", inline=True)
    embed1.set_footer(text="Page 1/5")


    embed2 = discord.Embed(color=0x0BA8B4, title="PC Commands")
    embed2.add_field(name="vup", value="turn up pc volume", inline=True)
    embed2.add_field(name="vdown", value="turn down pc volume", inline=True)
    embed2.add_field(name="bup", value="turn up brightness", inline=True)
    embed2.add_field(name="bdown", value="turn down brightness", inline=True)
    embed2.add_field(name="msgbox", value="opens msgbox", inline=True)
    embed2.add_field(name="screenshot", value="takes a screenshot of pc", inline=True)
    embed2.add_field(name="pcdownloads", value="checks pc downloads folder", inline=True)
    embed2.set_footer(text="Page 2/5")


    embed3 = discord.Embed(color=0x0BA8B4, title="Browser Commands")
    embed3.add_field(name="maps", value="opens google maps", inline=True)
    embed3.add_field(name="edgewindow", value="opens new Browser window", inline=True)
    embed3.add_field(name="roblox", value="opens roblox.com", inline=True)
    embed3.add_field(name="robloxsearch", value="search any roblox user with their ID", inline=True)
    embed3.add_field(name="snake", value="opens google snake", inline=True)
    embed3.add_field(name="tab", value="opens new tab", inline=True)
    embed3.add_field(name="translate", value="opens google translate", inline=True)
    embed3.add_field(name="url", value="opens any url", inline=True)
    embed3.add_field(name="ytsearch", value="search youtube for videos", inline=True)
    embed3.add_field(name="uselessfacts", value="opens useless facts api website", inline=True)
    embed3.add_field(name="devtools", value="opens devtools", inline=True)
    embed3.add_field(name="bcalc", value="opens calculator in Browser", inline=True)
    embed3.add_field(name="ngrams", value="opens google ngrams", inline=True)
    embed3.add_field(name="downloads", value="checks browser downloads", inline=True)
    embed3.set_footer(text="Page 3/5")


    embed4 = discord.Embed(color=0x0BA8B4, title="Trolling Commands")
    embed4.add_field(name="poosay", value="calls you a poosay", inline=True)
    embed4.add_field(name="rickroll", value="opens a rickroll", inline=True)
    embed4.add_field(name="history", value="opens Browser history", inline=True)
    embed4.add_field(name="close", value="closes active window", inline=True)
    embed4.add_field(name="hotkey", value="presses hotkey", inline=True)
    embed4.add_field(name="usertype", value="makes the host type anything", inline=True)
    embed4.set_footer(text="Page 4/5")

    embed5 = discord.Embed(color=0x0BA8B4, title="NSFW Commands")
    embed5.add_field(name="r34", value="searches rule34.xxx for images", inline=True)
    embed5.add_field(name="pornhub", value="searches pornhub.com for videos", inline=True)
    embed5.set_footer(text="Page 5/5")
    

    reactions = ("◀️", "🛑", "▶️")
    current_page = 0
    if current_page == 0:
        page = await ctx.send(embed=embed)
    for emoji in reactions:
        await page.add_reaction(emoji)

    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, user: user == ctx.author)

            if str(reaction.emoji) == "◀️":
                current_page -= 1
            elif str(reaction.emoji) == "▶️":
                current_page += 1
            elif str(reaction.emoji) == "🛑":
                await reaction.remove(user)
                await page.delete(delay=2.5)
                break  # Exit the loop if the stop button is clicked

            # Ensure current_page is within bounds
            current_page = max(0, min(current_page, 6))

            if current_page == 0:
                await page.edit(embed=embed)
            elif current_page == 1:
                await page.edit(embed=embed1)
            elif current_page == 2:
                await page.edit(embed=embed2)
            elif current_page == 3:
                await page.edit(embed=embed3)
            elif current_page == 4:
                await page.edit(embed=embed4)
            elif current_page == 5:
                await page.edit(embed=embed5)
            elif current_page == 6:
                await page.edit(embed=embed)
            await reaction.remove(user)  # Remove the user's reaction after processing
        except asyncio.TimeoutError:
            await ctx.send("Timed out.")
            await page.delete(delay=2.5)
            break  # Exit the loop on timeout

@bot.event
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, commands.CommandNotFound): 
        await ctx.reply("Invalid Command. Type **c!help** to see all commands")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Slow down! Try again in **{round(error.retry_after)}s.**")


bot.run(conf.TOKEN)
