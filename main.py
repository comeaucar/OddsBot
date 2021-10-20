# Imports
import os
import discord
from discord.ext import commands, tasks
import requests
import asyncio

# API Key Declaration
api_key = os.environ['api_key']

# Discord Config
client = commands.Bot(command_prefix='?', case_insensitive=True)
discord_token = os.environ['token']
channel_id = 900048955331706901
channel = client.get_channel(channel_id)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="type .help for commands ¯\\_(ツ)_/¯"))
    print('OddsBot is ready')


# URLS
base_url = "https://api.the-odds-api.com/v4/sports/"
sport_list_url = "https://api.the-odds-api.com/v4/sports/?apiKey=" + api_key
markets_url = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?regions=us&markets=h2h&apiKey=" + api_key
sports_list = requests.get(sport_list_url).json()
markets_list = requests.get(markets_url).json()

# Sport Keys
nfl_key = "americanfootball_nfl"
mlb_key = "baseball_mlb"
nhl_key = "icehockey_nhl"
nba_key = "basketball_nba"
mma_key = "mma_mixed_martial_arts"
epl_key = "soccer_epl"
seriea_key = "soccer_italy_serie_a"


# Retrieve Methods

@tasks.loop(hours=24)
async def getMLBMarkets(ctx):
    url = base_url + mlb_key + "/odds/?regions=us&apiKey=" + api_key
    request = requests.get(url).json()
    channel = client.get_channel(900169037403816027)
    try:
        for game in request:
            embed = discord.Embed(
                title="MLB EVENT",
                timestamp=ctx.message.created_at,
                color=discord.Color.dark_teal()
            )
            embed.add_field(name="Start Time", value=game['commence_time'], inline=False)
            embed.add_field(name="Home", value=game['home_team'], inline=False)
            embed.add_field(name="Away", value=game['away_team'], inline=False)
            embed.add_field(name="Odds", value=f"**----------------**", inline=False)
            bookmakers = game['bookmakers'][0]
            markets = bookmakers['markets'][0]
            outcomes = markets['outcomes']
            embed.add_field(name="Bookmaker", value=bookmakers['title'], inline=False)
            embed.add_field(name="Markets", value=markets['key'], inline=False)
            embed.add_field(name="Home", value=outcomes[0]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[0]['price'], inline=True)
            embed.add_field(name="-", value="-", inline=False)
            embed.add_field(name="Away", value=outcomes[1]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[1]['price'], inline=True)
            embed.set_thumbnail(
                url="https://www.legitgamblingsites.com/wp-content/uploads/2019/05/MLB-Betting-1280x720.png")
            embed.set_footer()
            embed_send = await channel.send(embed=embed)
            await embed_send.add_reaction('\U0001F1ED')
            await embed_send.add_reaction('\U0001F170')
    except:
        print("Baseball Exception")


@tasks.loop(hours=24)
async def getNFLMarkets(ctx):
    url = base_url + nfl_key + "/odds/?regions=us&apiKey=" + api_key
    request = requests.get(url).json()
    channel = client.get_channel(900169287325593601)
    try:
        for game in request:
            embed = discord.Embed(
                title="NFL EVENT",
                timestamp=ctx.message.created_at,
                color=discord.Color.red()
            )
            embed.add_field(name="Start Time", value=game['commence_time'], inline=False)
            embed.add_field(name="Home", value=game['home_team'], inline=False)
            embed.add_field(name="Away", value=game['away_team'], inline=False)
            embed.add_field(name="Odds", value=f"**----------------**", inline=False)
            bookmakers = game['bookmakers'][0]
            markets = bookmakers['markets'][0]
            outcomes = markets['outcomes']
            embed.add_field(name="Bookmaker", value=bookmakers['title'], inline=False)
            embed.add_field(name="Markets", value=markets['key'], inline=False)
            embed.add_field(name="Home", value=outcomes[0]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[0]['price'], inline=True)
            embed.add_field(name="-", value="-", inline=False)
            embed.add_field(name="Away", value=outcomes[1]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[1]['price'], inline=True)
            embed.set_thumbnail(url="https://brandslogos.com/wp-content/uploads/images/large/nfl-logo.png")
            embed.set_footer()
            embed_send = await channel.send(embed=embed)
            await embed_send.add_reaction('\U0001F1ED')
            await embed_send.add_reaction('\U0001F170')
    except Exception as e:
        print(e)
        print("NFL Exception")


@tasks.loop(hours=24)
async def getNHLMarkets(ctx):
    url = base_url + nhl_key + "/odds/?regions=us&apiKey=" + api_key
    request = requests.get(url).json()
    channel = client.get_channel(900169315981070356)
    try:
        for game in request:
            embed = discord.Embed(
                title="NHL EVENT",
                timestamp=ctx.message.created_at,
                color=discord.Color.blue()
            )
            embed.add_field(name="Start Time", value=game['commence_time'], inline=False)
            embed.add_field(name="Home", value=game['home_team'], inline=False)
            embed.add_field(name="Away", value=game['away_team'], inline=False)
            embed.add_field(name="Odds", value=f"**----------------**", inline=False)
            bookmakers = game['bookmakers'][0]
            markets = bookmakers['markets'][0]
            outcomes = markets['outcomes']
            embed.add_field(name="Bookmaker", value=bookmakers['title'], inline=False)
            embed.add_field(name="Markets", value=markets['key'], inline=False)
            embed.add_field(name="Home", value=outcomes[0]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[0]['price'], inline=True)
            embed.add_field(name="-", value="-", inline=False)
            embed.add_field(name="Away", value=outcomes[1]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[1]['price'], inline=True)
            embed.set_thumbnail(url="https://www.canadianbettingsites.net/wp-content/uploads/NHL-Betting-Guide-1.png")
            embed.set_footer()
            embed_send = await channel.send(embed=embed)
            await embed_send.add_reaction('\U0001F1ED')
            await embed_send.add_reaction('\U0001F170')
    except Exception as e:
        print(e)
        print("NHL Exception")


@tasks.loop(hours=24)
async def getNBAMarkets(ctx):
    url = base_url + nba_key + "/odds/?regions=us&apiKey=" + api_key
    request = requests.get(url).json()
    channel = client.get_channel(channel_id)
    try:
        for game in request:
            embed = discord.Embed(
                title="NBA EVENT",
                timestamp=ctx.message.created_at,
                color=discord.Color.orange()
            )
            embed.add_field(name="Start Time", value=game['commence_time'], inline=False)
            embed.add_field(name="Home", value=game['home_team'], inline=False)
            embed.add_field(name="Away", value=game['away_team'], inline=False)
            embed.add_field(name="Odds", value=f"**----------------**", inline=False)
            bookmakers = game['bookmakers'][0]
            markets = bookmakers['markets'][0]
            outcomes = markets['outcomes']
            embed.add_field(name="Bookmaker", value=bookmakers['title'], inline=False)
            embed.add_field(name="Markets", value=markets['key'], inline=False)
            embed.add_field(name="Home", value=outcomes[0]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[0]['price'], inline=True)
            embed.add_field(name="-", value="-", inline=False)
            embed.add_field(name="Away", value=outcomes[1]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[1]['price'], inline=True)
            embed.set_thumbnail(url="https://cdn.freebiesupply.com/images/large/2x/nba-logo-transparent.png")
            embed.set_footer()
            embed_send = await channel.send(embed=embed)
            await embed_send.add_reaction('\U0001F1ED')
            await embed_send.add_reaction('\U0001F170')
    except Exception as e:
        print(e)
        print("NHL Exception")


@tasks.loop(hours=24)
async def getMMAMarkets(ctx):
    url = base_url + mma_key + "/odds/?regions=us&apiKey=" + api_key
    request = requests.get(url).json()
    channel = client.get_channel(channel_id)
    try:
        for game in request:
            embed = discord.Embed(
                title="MMA EVENT",
                timestamp=ctx.message.created_at,
                color=discord.Color.dark_gold()
            )
            embed.add_field(name="Start Time", value=game['commence_time'], inline=False)
            embed.add_field(name="Home", value=game['home_team'], inline=False)
            embed.add_field(name="Away", value=game['away_team'], inline=False)
            embed.add_field(name="Odds", value=f"**----------------**", inline=False)
            bookmakers = game['bookmakers'][0]
            markets = bookmakers['markets'][0]
            outcomes = markets['outcomes']
            embed.add_field(name="Bookmaker", value=bookmakers['title'], inline=False)
            embed.add_field(name="Markets", value=markets['key'], inline=False)
            embed.add_field(name="Home", value=outcomes[0]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[0]['price'], inline=True)
            embed.add_field(name="-", value="-", inline=False)
            embed.add_field(name="Away", value=outcomes[1]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[1]['price'], inline=True)
            embed.set_thumbnail(url="https://pngimg.com/uploads/ufc/ufc_PNG64.png")
            embed.set_footer()
            embed_send = await channel.send(embed=embed)
            await embed_send.add_reaction('\U0001F1ED')
            await embed_send.add_reaction('\U0001F170')
    except Exception as e:
        print(e)
        print("NHL Exception")


@tasks.loop(hours=24)
async def getEPLMarkets(ctx):
    url = base_url + epl_key + "/odds/?regions=us&apiKey=" + api_key
    request = requests.get(url).json()
    channel = client.get_channel(channel_id)
    try:
        for game in request:
            embed = discord.Embed(
                title="EPL EVENT",
                timestamp=ctx.message.created_at,
                color=discord.Color.purple()
            )
            embed.add_field(name="Start Time", value=game['commence_time'], inline=False)
            embed.add_field(name="Home", value=game['home_team'], inline=False)
            embed.add_field(name="Away", value=game['away_team'], inline=False)
            embed.add_field(name="Odds", value=f"**----------------**", inline=False)
            bookmakers = game['bookmakers'][0]
            markets = bookmakers['markets'][0]
            outcomes = markets['outcomes']
            embed.add_field(name="Bookmaker", value=bookmakers['title'], inline=False)
            embed.add_field(name="Markets", value=markets['key'], inline=False)
            embed.add_field(name="Home", value=outcomes[0]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[0]['price'], inline=True)
            embed.add_field(name="-", value="-", inline=False)
            embed.add_field(name="Away", value=outcomes[1]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[1]['price'], inline=True)
            embed.set_thumbnail(url="https://www.fifplay.com/img/public/premier-league-2-logo.png")
            embed.set_footer()
            embed_send = await channel.send(embed=embed)
            await embed_send.add_reaction('\U0001F1ED')
            await embed_send.add_reaction('\U0001F170')
    except Exception as e:
        print(e)
        print("NHL Exception")


@tasks.loop(hours=24)
async def getSERIEAMarkets(ctx):
    url = base_url + seriea_key + "/odds/?regions=us&apiKey=" + api_key
    request = requests.get(url).json()
    channel = client.get_channel(channel_id)
    try:
        for game in request:
            embed = discord.Embed(
                title="SERIE-A EVENT",
                timestamp=ctx.message.created_at,
                color=discord.Color.green()
            )
            embed.add_field(name="Start Time", value=game['commence_time'], inline=False)
            embed.add_field(name="Home", value=game['home_team'], inline=False)
            embed.add_field(name="Away", value=game['away_team'], inline=False)
            embed.add_field(name="Odds", value=f"**----------------**", inline=False)
            bookmakers = game['bookmakers'][0]
            markets = bookmakers['markets'][0]
            outcomes = markets['outcomes']
            embed.add_field(name="Bookmaker", value=bookmakers['title'], inline=False)
            embed.add_field(name="Markets", value=markets['key'], inline=False)
            embed.add_field(name="Home", value=outcomes[0]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[0]['price'], inline=True)
            embed.add_field(name="-", value="-", inline=False)
            embed.add_field(name="Away", value=outcomes[1]['name'], inline=True)
            embed.add_field(name="Price", value=outcomes[1]['price'], inline=True)
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/en/6/6c/Serie_A_logo.png")
            embed.set_footer()
            embed_send = await channel.send(embed=embed)
            await embed_send.add_reaction('\U0001F1ED')
            await embed_send.add_reaction('\U0001F170')
    except Exception as e:
        print(e)
        print("NHL Exception")


@client.event
async def on_reaction_add(reaction, user):
    channel = client.get_channel(900171245402861588)
    if (user.name != "OddsBot"):
        await channel.send(
            '{} has added {} to the message {}'.format(user.name, reaction.emoji, reaction.message.embeds[0].title))
        if (reaction.emoji == "🇭"):
            await channel.send("Taking the Home side: {} over {}".format(reaction.message.embeds[0].fields[1].value,
                                                                         reaction.message.embeds[0].fields[2].value))
        else:
            await channel.send("Taking the Away side: {} over {}".format(reaction.message.embeds[0].fields[2].value,
                                                                         reaction.message.embeds[0].fields[1].value))


@getMLBMarkets.before_loop
async def before_mlb_loop():
    await asyncio.sleep(1)
    await client.wait_until_ready()
    print("Client Ready")

@getNFLMarkets.before_loop
async def before_mlb_loop():
    await asyncio.sleep(1)
    await client.wait_until_ready()
    print("Client Ready")

@getNHLMarkets.before_loop
async def before_mlb_loop():
    await asyncio.sleep(1)
    await client.wait_until_ready()
    print("Client Ready")
getMLBMarkets.start()
getNFLMarkets.start()
getNHLMarkets.start()
client.run(os.environ['token'])
