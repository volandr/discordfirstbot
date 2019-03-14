import discord
from discord.ext import commands
from discord.ext.commands import Bot
import requests
from bs4 import BeautifulSoup as bs
import os



headers={'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
base_url = 'https://yummyanime.club/random'

def anime_parse(base_url, headers):
    session=requests
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        print('OK')
        soup = bs(request.content, 'html.parser')
        a_name=soup.h1.string
        a_poster=soup.find('div',attrs={'class': 'poster-block'}).find('img')["src"]
        a_opis=soup.find('div',attrs={'id': 'content-desc-text'}).p.string
        print(a_opis)
        return (a_name,a_poster,a_opis)
    else:
            print('Error')



Bot = commands.Bot(command_prefix='!')
@Bot.event
async def on_ready():
    print("Bot online")

@Bot.command(pass_context= True)
async def anime(ctx):
    anime = anime_parse(base_url, headers)
    embed=discord.Embed(title="Случайное аниме", color=0xff8000)
    url_logo="https://yummyanime.club"+anime[1]
    embed.set_thumbnail(url=url_logo)
    embed.add_field(name='Название', value=anime[0], inline=True)
    embed.add_field(name='Описание', value=anime[2], inline=True)
    await Bot.say(embed=embed)

token = os.environ.get('BOT_TOKEN')







