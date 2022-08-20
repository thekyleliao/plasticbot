import discord, random, os, time, asyncio

TOKEN = "OTk2MTI0OTUzOTY1NTAyNjA0.GmP4Xw.G0XLfq9S1wcJaJ1T-BNgCeKy27zhTlmiIWtA3Q"

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            global answerChoice
            if m.content == 'top':
                answerChoice = 'top'
            elif m.content == 'bottom':
                answerChoice = 'bottom'
            print(answerChoice)

            return m.content == 'top' or "bottom" and m.channel == channel
            

        msg = await client.wait_for('message', check=check)
        
        await channel.send(f'{answerChoice}'.format(msg))

client.run(TOKEN)