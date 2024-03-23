import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
# Dan inilah cara Kamu mengganti nama file dari variabel!
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
                    picture = discord.File(f)
    await ctx.send(file=picture)
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
#buat variabel sampah organik dan non organik
organic = ['veggie', 'grass', 'dried veggie', 'kayu', 'ranting pohon', 'daun', 'makanan sisa', 'buah busuk', 'kertas', 'tisu', 'kapas', 'serbuk kayu', 'bangkai hewan', 'kotoran hewan dan manusia']
anorganic = ['plastik', 'ban', 'kaca', 'botol', 'baterai']

@bot.command()
async def trash(ctx):
    await ctx.send("Input your trash :")
    msg = await bot.wait_for("message")
    if msg.content in organic :
        await ctx.send("Put your trash in an organic or recyclable trash can!")
    elif msg.content in anorganic :
        await ctx.send("Put your trash in an anorganic trash can!")
    

bot.run('TOKEN HERE')
