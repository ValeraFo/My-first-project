import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix = '&')
client.remove_command("help")

@client.event
async def on_ready():
	print("Bot is online")

@client.command(pass_context = True)
async def clear(ctx,amount=1):
    await ctx.channel.purge(limit = amount+1)


@client.command(pass_context = True)
async def help(ctx):
    emb = discord.Embed(title = "Команды")
    
    emb.add_field( name = "&dice num1 num2", value = "Даёт случайное число от 1 до num1 и складывает его с num2")
    emb.add_field( name = "&clear num", value = "Удаляет сообщения в количестве num")
    
    await ctx.send(embed = emb)

@client.command(pass_context = True, aliases = ['d','д'])
async def dice(ctx,dic = 20,mod = "0",c = 1):
	res = ""
	if mod[0] == "-":
		di = 0 - int(mod[1])
	else:
		di = int(mod)
	while c > 0:
		result = random.randint(1,int(dic))
		res = res+str(result+int(mod))+"\n"
		c = c-1
		dm = ""
	await ctx.send(str(res))


token = os.environ.get('TOKEN')
client.run(str(token))
