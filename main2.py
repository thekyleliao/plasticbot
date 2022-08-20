# modules I am using
import discord, random, os, time, asyncio

# place for the token for the bot
TOKEN = "OTk2MTI0OTUzOTY1NTAyNjA0.GmP4Xw.G0XLfq9S1wcJaJ1T-BNgCeKy27zhTlmiIWtA3Q"

client = discord.Client()

# initialization event to confirm bot is on in terminal
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# data list
A = ("Coca-Cola", 13834, "https://www.debriar.co.uk/uploads/images/zoom/COCA_COLA_500_ML_PET_BOTTLES.png.jpg", "https://us.coca-cola.com/support/contact-us")
B = ("Pepsico", 5155, "https://foodsided.com/files/image-exchange/2016/04/ie_22482.jpeg","https://contact.pepsico.com/pepsico/contact-us")
C = ("Nestle", 8633, "https://i5.walmartimages.com/asr/c64fe48e-d6c0-48cf-80d5-a647d0db641a_1.ad40a19cda58afb1c7baaf016423f67b.jpeg","https://www.nestleusa.com/info/contact-us-landing")
D = ("Unilever", 5558, "https://www.upmraflatac.com/contentassets/90ad95d8905e4c58b8c52980d525c53c/unilever-products-with-reduced-plastic-packaging.jpg?preset=tmpl-size-full","https://www.unilever.com/contact/")
E = ("Mondelez", 1171, "https://www.bakingbusiness.com/ext/resources/2020/2/MondelezPortfolio_Lead.jpg?t=1582200080&width=1080","https://www.mdlzcusthelp.com/feedbackform")
F = ("Mars", 678, "https://www.bfernandez.com/wp-content/uploads/2020/03/mars-wrigley-pic-1-1200x675.jpg","https://www.mars.com/contact-us")
G = ("Procter&Gamble", 3535, "https://www.royalwarrant.org/sites/default/files/P%26G%20Effect%20campaign_group%20images.jpg","https://us.pg.com/contact-us/#media")
H = ("Phillips Morris", 2593, "https://static.seekingalpha.com/uploads/2013/2/7098401_13603631989466_0.jpg","https://www.pmi.com/contact-us/contact-us-form")
I = ("Colgate", 5991, "https://www.beeqasi.co.ke/wp-content/uploads/2020/06/colgate-brand.jpg","https://www.colgatepalmolive.com/en-us/contact-us")
J = ("Perfetti",465,"https://bangladeshbusinessdir.com/wp-content/uploads/2015/05/Perfetti-Van-Melle-bd.jpg","https://www.perfettivanmelle.com/contact-directory/sales-operations/the-americas/")

# end of data list

# functions for playing the game(basically choosing two random companies and determining which one pollutes more.)
def playSystem():
   global first, second
   totalList = [A,B,C,D,E,F,G,H,I,J]
   listLength = len(totalList) - 1
   rchoose = random.randint(0,listLength)
   first = totalList[rchoose]
   del totalList[rchoose]
   listLength = len(totalList) - 1 
   rchoose = random.randint(0,listLength)
   second = totalList[rchoose]
def answerRight():
    global rightChoice
    if first[1] > second[1]:
        rightChoice = "top"
        print(rightChoice)
    else:
        rightChoice = "bottom"
        print(rightChoice)


    
# code below is for the incoming discord messages

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

# ensures that the bot act on its own messages.
    if message.author == client.user:
        return

# code for playing the higher or lower game
    if user_message == ">play":
        playSystem()
        answerRight()
        await message.channel.send(f'Based on statistics from breakfreefromplastic, what do you think has been found more in the ocean?')
        await asyncio.sleep(1)
        await message.channel.send(f'Is it {first[0]} or {second[0]}')
        await asyncio.sleep(1)
        await message.channel.send(f'{first[2]}')
        await asyncio.sleep(1)
        await message.channel.send(f'{second[2]}')
        await asyncio.sleep(1)
        await message.channel.send(f'Answer with either top or bottom, which refers to the order of the images.')
    
# system for waiting for an answer and saving it
        def check(m):
            global answerChoice
            answerChoice = ""
            if m.content == 'top':
                answerChoice = 'top'
            elif m.content == 'bottom':
                answerChoice = 'bottom'
            print(answerChoice)
            
            return True

        msg = await client.wait_for('message', check=check)
# end of that system for waiting for an answer and saving it

# system for determining what response to provide the user based on if they are right or wrong
        if answerChoice == rightChoice:
            await asyncio.sleep(1)
            await message.channel.send(f'You were correct in your choice.')
        
        if answerChoice != rightChoice:
            await asyncio.sleep(1)
            await message.channel.send(f'You were wrong in your choice.')
        await asyncio.sleep(1)
        await message.channel.send(f'{first[0]} had {first[1]} pieces of plastic found in a global cleanup while {second[0]} had {second[1]} pieces found.')
        if rightChoice == 'top':
            await asyncio.sleep(1)
            await message.channel.send(f'{first[0]} polluted more.')
        elif rightChoice =='bottom':
            await asyncio.sleep(1)
            await message.channel.send(f'{second[0]} polluted more.')

# messages that are dmed to the user and sum up the end of the game.
        await message.channel.send(f'Send the message >play to play again.')
        await message.author.send(f'You choose between these companies, {first[0]} and {second[0]}.')
        await message.author.send(f'{first[3]} is the link for contacting {first[0]}, while {second[3]} is the link for contacting {second[0]}.')
        await message.author.send("We hope that with the contact information and the knowledge that every year thousands of pieces of plastic are being found(just in the breakfreefromplastic survey) from these companies that you make the choice of contacting these companies to find out what they are doing about it.")
        # create a sample email message that we generate using the name and statistics.
        # make system for counting # of right answers


client.run(TOKEN)