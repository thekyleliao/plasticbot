import discord
import random
import os
import time
import asyncio



TOKEN = "OTk2MTI0OTUzOTY1NTAyNjA0.GmP4Xw.G0XLfq9S1wcJaJ1T-BNgCeKy27zhTlmiIWtA3Q"

client = discord.Client()

#totalList = (A,B,C,D,E,F,G,H,I,J)

A = ("Coca-Cola", 13834, "https://www.debriar.co.uk/uploads/images/zoom/COCA_COLA_500_ML_PET_BOTTLES.png.jpg")
B = ("Pepsico", 5155, "https://foodsided.com/files/image-exchange/2016/04/ie_22482.jpeg")
C = ("Nestle", 8633, "https://i5.walmartimages.com/asr/c64fe48e-d6c0-48cf-80d5-a647d0db641a_1.ad40a19cda58afb1c7baaf016423f67b.jpeg")
D = ("Unilever(Shampoo)", 5558, "https://www.upmraflatac.com/contentassets/90ad95d8905e4c58b8c52980d525c53c/unilever-products-with-reduced-plastic-packaging.jpg?preset=tmpl-size-full")
E = ("Mondelez(snacks)", 1171, "https://www.bakingbusiness.com/ext/resources/2020/2/MondelezPortfolio_Lead.jpg?t=1582200080&width=1080")
F = ("Mars(m&ms)", 678, "https://www.bfernandez.com/wp-content/uploads/2020/03/mars-wrigley-pic-1-1200x675.jpg")
G = ("Procter&Gamble(Pampers)", 3535, "https://www.royalwarrant.org/sites/default/files/P%26G%20Effect%20campaign_group%20images.jpg")
H = ("Phillips Morris(Tobacco)", 2593, "https://static.seekingalpha.com/uploads/2013/2/7098401_13603631989466_0.jpg")
I = ("Colgate", 5991, "https://www.beeqasi.co.ke/wp-content/uploads/2020/06/colgate-brand.jpg")
J = ("Perfetti",465,"https://bangladeshbusinessdir.com/wp-content/uploads/2015/05/Perfetti-Van-Melle-bd.jpg")

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

    if message.channel.name == 'bot-testing':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower == '>whoami':
            await message.channel.send(f'Well I am plastic bot(name is a work in progress). Nice to meet you {username}. My goal is to reveal to you the contents of my database regarding plastic pollution using games to hopefully encourage everyone to contact the companies that produce all these goods to reduce and stop all of the plastic they use. The products they make, we use, and at the end of the product lifespan they often end up in the water where organizations pick them up to stop them from further harming the enviornment.')
        elif user_message.lower() == '>play':
            global first, second
            totalList = [A,B,C,D,E,F,G,H,I,J]
            listLength = len(totalList) - 1
            rchoose = random.randint(0,listLength)
            first = totalList[rchoose]
            del totalList[rchoose]
            listLength = len(totalList) - 1 
            rchoose = random.randint(0,listLength)
            second = totalList[rchoose]
            print(first)
            print("above is first")
            print(second)
            print("above is second")
            await message.channel.send(f'Based on statistics from breakfreefromplastic, what do you think has been found more in the ocean?')
            await asyncio.sleep(1)
            await message.channel.send(f'Is it {first[0]} or {second[0]}')
            await asyncio.sleep(1)
            await message.channel.send(f'{first[2]}')
            await asyncio.sleep(1)
            await message.channel.send(f'{second[2]}')
            await asyncio.sleep(1)
            await message.channel.send(f'Answer with either top or bottom, which refers to the order of the images.')
            await asyncio.sleep(1)
           
           #reading into the documentation to figure how to make code below be an event
            
            
            if user_message.lower() == "top":
                await message.channel.send(f'{first[0]} had {first[1]} pieces of plastic found in a global cleanup while {second[0]} had {second[1]} pieces found.')
                if first[1] > second[1]:
                    await message.channel.send(f'{first[0]} polluted more.')
                    await asyncio.sleep(1)
                    await message.channel.send(f'{username} you were right. ')
                    
                else:
                    await message.channel.send(f'{second[0]} polluted more.')
                    await asyncio.sleep(1)
                    await message.channel.send(f'{username} you were wrong.')
                    
            elif user_message.lower() == "bottom":
                await message.channel.send(f'{first[0]} had {first[1]} pieces of plastic found in a global cleanup while {second[0]} had {second[1]} pieces found.')
                if second[1] > first[1]:
                    await message.channel.send(f'{second[0]} polluted more.')
                    await asyncio.sleep(1)
                    await message.channel.send(f'{username} you were right.')
                    
                else: 
                    await message.channel.send(f'{first[0]} polluted more.')
                    await asyncio.sleep(1)
                    await message.channel.send(f'{username} you were wrong.')
                    





# code below is for testing, my nested ifs are not working
#        if user_message.lower() == "top":
 #           await message.channel.send(f'{first[0]} had {first[1]} pieces of plastic found in a global cleanup while {second[0]} had {second[1]} pieces found.')
  #          if first[1] > second[1]:
   #             await message.channel.send(f'{first[0]} polluted more.')
    #            await asyncio.sleep(1)
     #           await message.channel.send(f'{username} you were right. ')
      #      else:
       #         await message.channel.send(f'{second[0]} polluted more.')
        #        await asyncio.sleep(1)
         #       await message.channel.send(f'{username} you were wrong.')
       # elif user_message.lower() == "bottom":
        #    await message.channel.send(f'{first[0]} had {first[1]} pieces of plastic found in a global cleanup while {second[0]} had {second[1]} pieces found.')
         #   if second[1] > first[1]:
          #      await message.channel.send(f'{second[0]} polluted more.')
           #     await asyncio.sleep(1)
            #    await message.channel.send(f'{username} you were right.')
           # else: 
            #    await message.channel.send(f'{first[0]} polluted more.')
             #   await asyncio.sleep(1)
              #  await message.channel.send(f'{username} you were wrong.')
            


                
                
# will use these messages later.                
#               await message.channel.send(f'Which of the products you looked at have you used? React to the images you have')
                    #await message.channel.send(f'Send the message >play to play again.')
                    #await message.author.send(f'You choose these companies, {first[0]}, {second[0]}. Here are their contact infos along with the statistics and a sample email/message you can shout at them.')
#
client.run(TOKEN)

# Need to figure out a solution to storing data and retrieving it
# A list of dictionaries with their names as part of list which a random gen can pick one based on indexed order.
# We then use that dictionary to feed into variables that feed into our messages.
# Then we can play the game. We can make a message to send the link in channel which will produce the image that can be reacted upon.
# 
#
#
#
#
#
#
