import discord
import requests
import json


def get_meme():
    response= requests.get('https://meme-api.com/gimme')
    json_data= json.loads(response.text)
    return json_data['url']
def get_opmeme():
    response= requests.get('https://meme-api.com/gimme/onepiecememes')
    json_data= json.loads(response.text)
    return json_data['url']
def get_catmeme():
    response= requests.get('https://meme-api.com/gimme/Catmemes')
    json_data= json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    
    async def on_ready(self):
        print("Logged in as {0}!".format(self.user))
        
        welcome_message= '*Welcome to MemeBot, I can do a few things for you-*\nFor general memes, use command- **\'$meme\'** \nFor cat memes, use command- **\'$catmeme\'** \nFor One Piece(anime) memes, use command- **\'$opmeme\'** \n\n Have some good LOLs'
        channel=client.get_channel(730517254793461841) #channel_id
        await channel.send(welcome_message)
        
    ''' for guild in self.guilds:
            print(f"Bot is active in guild: {guild.name}")
        
        # Accessing all the channels in that guild
        for channel in guild.channels:
            print(f"Channel: {channel.name} (ID: {channel.id})")        '''
    
        
    async def on_message(self,message):
        if message.author == self.user:
            return
        
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())  
        if message.content.startswith('$opmeme'):
            await message.channel.send(get_opmeme())      
        if message.content.startswith('$catmeme'):
            await message.channel.send(get_catmeme())
            
            
intention= discord.Intents.default()
intention.message_content= True

client= MyClient(intents=intention)
client.run('')  #insert Bot token here



