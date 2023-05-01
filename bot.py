import discord
import requests
import json
import random
from discord.ext import commands

TOKEN ="MTEwMTIwNTk0ODM5NzI3NzI0NQ.GUT72O.SNyrskIqwvrwpgn2ANhB9IN0z802suLxS_VONw"
WEATHER_API_KEY = "ffd3e1feee96659462c9235776b0d242"
CHUCK_API_URL = 'https://api.chucknorris.io/jokes/random'
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command(name='joke')
async def joke(ctx):
    response = requests.get(CHUCK_API_URL)
    joke = json.loads(response.text)['value']
    await ctx.send(joke)

@bot.command(name='weather')
async def weather(ctx, location=None):
    if location is None:
        await ctx.send('Please provide a location')
        return
    
    params = {
        'q': location,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }
    response = requests.get(WEATHER_API_URL, params=params)
    weather = json.loads(response.text)
    temp = weather['main']['temp']
    description = weather['weather'][0]['description']
    await ctx.send(f'The weather in {location} is {temp}°C and {description}')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    if number_of_dice is None:
        await ctx.send('Please provide a Number of dice')
        return
    if number_of_sides is None:
        await ctx.send('Please provide a number of sides')
        return
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


bot.run(TOKEN)