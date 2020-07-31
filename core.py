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
async def help(ctx):
	emb = discord.Embed(title = "Команды")
	
	emb.add_field( name = "&sum <num1> <num2>", value = "Суммирует num1 и num2")
	emb.add_field( name = "&sub <num1> <num2>", value = "Отнимает num2 от num1")
	emb.add_field( name = "&mul <num1> <num2>", value = "Умножает num1 на num2")
	emb.add_field( name = "&div <num1> <num2>", value = "Делит num1 на num2")
	emb.add_field( name = "&dice num1 num2", value = "Даёт случайное число от 1 до num1 и складывает его с num2")
	
	await ctx.send(embed = emb)

@client.command(pass_context = True)
async def sum(ctx,s1,s2):
	await ctx.send(str(s1)+" + "+str(s2)+" = "+str(int(s1)+int(s2)))

@client.command(pass_context = True)
async def sub(ctx,s1,s2):
	await ctx.send(str(s1)+" - "+str(s2)+" = "+str(int(s1)-int(s2)))

@client.command(pass_context = True)
async def mul(ctx,s1,s2):
	await ctx.send(str(s1)+" * "+str(s2)+" = "+str(int(s1)*int(s2)))

@client.command(pass_context = True)
async def div(ctx,s1,s2):
	await ctx.send(str(s1)+" / "+str(s2)+" = "+str(int(int(s1)/int(s2))))

@client.command(pass_context = True)
async def dice(ctx,dic,mod):
	if int(mod) => 0:
		result = random.randint(1,int(dic))
		await ctx.send(str(result+int(mod)))
	else:
		mod = "0"
		result = random.randint(1,int(dic))
		await ctx.send(str(result+int(mod)))

token = os.environ.get('TOKEN')
client.run(str(token))
