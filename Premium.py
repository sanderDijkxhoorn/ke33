##vervang dit
bot_key="NTIwODY1OTY2OTI2NzI1MTIx.Du0F9A.JnHICv997wmGle12HjBDiFxB88E"
default_role="RainbowRole"
##--------------------
import discord
import asyncio
import logging
import time
from discord.ext.commands import Bot
from discord.ext import commands
from time import sleep
from colorsys import hls_to_rgb
client = commands.Bot(command_prefix = "=") #Initialise client bot
client = discord.Client()
dothething = {}
@client.event
async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('---------------------------------') 
        await client.change_presence(status=discord.Status.dnd, game=discord.Game(name='type "=help" for help'))
@client.event
async def on_message(message):
        global dothething
        if message.author == client.user:
                return
        if message.content.startswith("=stop"):
                await client.send_message(message.channel,"stopped <@520865966926725121> ({0.author.mention})".format(message))
                try:
                        dothething[str(message.server.id)]=0
                except:
                        print("error")
        if message.content.startswith("=test"):
                await client.send_message(message.channel, "{0.author.mention} used test".format(message))
                await client.send_message(message.author, "@here WBDOAUDGAWVKDDD")
                await client.send_message(message.author, "WHIH @here WAUDGLAI:JDHAWBKD")
                await client.send_message(message.author, "ADWHA @here OGDADUDA")
                await client.send_message(message.author, "JAWBDJ @here LBWADDAWKBLD:Hl")
                await client.send_message(message.author, "AKWH @here DLUWGDLAWDH")
                await client.send_message(message.author, "AJLWDBWA @here ULDDAWGKD")
                await client.send_message(message.author, "dajlwDLvJWHAGDKAVWK")
                await client.send_message(message.author, "AWDLJG @here LDIYHWAD")
                await client.send_message(message.author, "DWIHGD @here I&AWyoL")
                await client.send_message(message.author, "awDBAW @here GDUIOWALH")
                await client.send_message(message.author, "DAWDA @here WDWA")
                await client.send_message(message.author, "teswA @here WADwaadwWt")
                await client.send_message(message.author, "teWDA @here AWDt")
                await client.send_message(message.author, "teWDWD @here DWDAAAWwaddst")
                await client.send_message(message.author, "teawa @here wdawdawst")
                await client.send_message(message.author, "tedwav @here dwdwast")
                await client.send_message(message.author, "teawaw @here adwst")
                await client.send_message(message.author, "teawda @here wdadwwdst")
                await client.send_message(message.author, "teadwa @here wwadawdst")
                await client.send_message(message.author, "teswada @here  @here wdawdt")
                await client.send_message(message.author, "tedasdwd @here wst")
                await client.send_message(message.author, "tesddada @here dwdat")
                await client.send_message(message.author, "tesadd @here awawdast")
                await client.send_message(message.author, "tesdad @here wdadsst")
                await client.send_message(message.author, "tdawda @here wdst")
                await client.send_message(message.author, "tewdawa @here wawdst")
                await client.send_message(message.author, "tesadwad @here  @here wadwadwgegst")
                await client.send_message(message.author, "tafafesse @here sgest")
                await client.send_message(message.author, "tscxczfs @here vfest")
                await client.send_message(message.author, "teaweadas @here dwwst")
                await client.send_message(message.author, "teaawf @everyone fast")
                await client.send_message(message.author, "teddawf @everyone ast")
                await client.send_message(message.author, "tafafaw @everyone efafst")
                await client.send_message(message.author, "tseters @everyone dfaefsefest")
                await client.send_message(message.author, "fsfadwv @everyone fegetest")
                await client.send_message(message.author, "tffaw @everyone est")
                await client.send_message(message.author, "tefwa @everyone st")
                await client.send_message(message.author, "teawf @everyone wast")
                await client.send_message(message.author, "tedwv @everyone fst")
                await client.send_message(message.author, "tesf @everyone ast")
                await client.send_message(message.author, "tew @everyone fst")
                await client.send_message(message.author, "tefa @everyone fst")
                await client.send_message(message.author, "tefsfa @everyone wfest")
                await client.send_message(message.author, "te @everyone st")
                await client.send_message(message.author, "teswwa @everyone efst")
                await client.send_message(message.author, "tesw @everyone aafwfwat")
                await client.send_message(message.author, "tes @everyone fst")
                await client.send_message(message.author, "tesf @everyone wat")
                await client.send_message(message.author, "tea @everyone st")
                await client.send_message(message.author, "tea3w @everyone fergwfwast")
                await client.send_message(message.author, "tes5 @everyone 323wt")
                await client.send_message(message.author, "tes525 @everyone f4fset")
                await client.send_message(message.author, "tes52 @everyone 3t")
                await client.send_message(message.author, "tes325 @everyone 33525t")
                await client.send_message(message.author, "tes @everyone 52t")
                await client.send_message(message.author, "tes641646 @everyone 3616t")
                await client.send_message(message.author, "tes166 @everyone 3346t")
                await client.send_message(message.author, "tes64 @everyone 116t")
                await client.send_message(message.author, "t46 @everyone 1est")
                await client.send_message(message.author, "te46 @everyone  @everyone 63446343st")
                await client.send_message(message.author, "te464 @everyone 36346st")
                await client.send_message(message.author, "t6434 @everyone 6est")
                await client.send_message(message.author, "t4e @everyone st")
                await client.send_message(message.author, "te2 @everyone 535242st")
                await client.send_message(message.author, "3636 @everyone 44664346431test")
                await client.send_message(message.author, "te6433 @everyone 64st")
                await client.send_message(message.author, "t356436 @everyone 537674est")
                await client.send_message(message.author, "te6436 @everyone st")
                await client.send_message(message.author, "t6364 @everyone 346est")
                await client.send_message(message.author, "te6161 @everyone 61st")
                await client.send_message(message.author, "tes643 @everyone 6326t")
                await client.send_message(message.author, "te1434 @everyone 66st")
                await client.send_message(message.author, "te631v664163616st")
                await client.send_message(message.author, "tes166 @everyone 34663t")
                await client.send_message(message.author, "te6 @everyone 116st")
                await client.send_message(message.author, "te6616 @everyone st")
                await client.send_message(message.author, "wtf do you want from me --__--")
        if message.content.startswith("=clear"):
                tmp = await client.send_message(message.channel, "Clearing messages...  {0.author.mention}".format(message))
                print('Clearing in channel: ' + str(message.server.name) + '. Command send by: {0.author.mention}'.format(message))
                async for msg in client.logs_from(message.channel):
                        await client.delete_message(msg)
        if message.content.startswith("=invite"):
                await client.send_message(message.author, "https://discordapp.com/api/oauth2/authorize?client_id=520865966926725121&permissions=8&scope=bot")
                print('Sended invite link to {0.author.mention}'.format(message))
        if message.content.startswith("=invite"):
                await client.send_message(message.channel, "Look at your dm {0.author.mention} :smiley:".format(message))
        if message.content.startswith("=help"):
                await client.send_message(message.channel, "To start the bot type =start (the role you need to create is RainbowRole it need permissions otherwise it could not change anything.) =stop for stopping the rainbow role if need extra help or wanna buy fast version or anything like that contact ZYKI#0739")
        if message.content.startswith("=start"):
                await client.send_message(message.channel, "Started <@520865966926725121> ({0.author.mention})".format(message))
                print('{0.author.mention} used: "=start"'.format(message) + ' in channel: ' + str(message.server.name))
                hue=0
                if message.content.strip().startswith("=start "):
                        role = discord.utils.find(lambda m: m.name == message.content[6:].strip() ,message.server.roles)
                else:
                        role = discord.utils.find(lambda m: m.name == default_role ,message.server.roles)
                try:
                        dothething[str(message.server.id)]
                except:
                        dothething[str(message.server.id)]=0
                if role and not dothething[str(message.server.id)]:
                        dothething[str(message.server.id)]=1
                        while dothething[str(message.server.id)]:
                                users = [int(str(x.status)=="online") for x in message.server.members if role in x.roles] #black magic fuckery here
                                users.append(0)
                                print(str(message.server.name)+" - "+str(users))
                                if max(users):
                                        for i in range(50): #arbitrary rate limits
                                                if not dothething[str(message.server.id)]:
                                                        break
                                                hue = (hue+7)%360
                                                rgb = [int(x*255) for x in hls_to_rgb(hue/360, 0.5, 1)]
                                                clr = discord.Colour(((rgb[0]<<16) + (rgb[1]<<8) + rgb[2]))
                                                try:
                                                        await client.edit_role(message.server, role, colour=clr)
                                                except:
                                                        print("no permissions on this server: " + str(message.server.name))
                                                        await client.send_message(message.channel, "I need permissions O.o")
                                                        dothething[str(message.server.id)]=0
                                else:
                                        await asyncio.sleep(1)
client.run(bot_key)
