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
async def dice(ctx,dic = 20,mod = 0,c = 1):
	global x
	global y
	res = ""
	while c > 0:
		result = random.randint(1,int(dic))
		if x > 0 && y > 0:
			result = x
			y = y-1
		res = res+str(result)+"\n"
		c = c-1
	x = 0
	await ctx.send(str(res))
	

@client.command(pass_context = True)
async def test1(ctx,td,kx):
	global x
	global y
	x = int(td)
	y = int(kx)
	await ctx.send(str(x)+" "+str(kx))

@client.command(pass_context = True)
async def test2(ctx):
	await ctx.send(str(x))

token = os.environ.get('TOKEN')
client.run(str(token))
