from main import *
import openai

openai.api_key = os.environ['openai_api']


class Chat(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_message(self, message):

    if message.author.bot:
      return

    if message.mention_everyone:
        return

    try:
      if client.user.mentioned_in(message):
  
        async with message.channel.typing():
          message_raw = message.content.split()
          prompt = ' '
    
          prompt = prompt.join(message_raw[1:])
    
          response = openai.Completion.create(model="text-davinci-003",
                                              prompt=prompt,
                                              temperature=0.7,
                                              max_tokens=2000,
                                              top_p=0.3,
                                              frequency_penalty=0.5,
                                              presence_penalty=0.2)
    
          response_text = response.choices[0].text
      
          await message.reply(response_text)

    except Exception as e:
      await message.reply(f"An exception has occured... :(\n {e}")
      

  @commands.command(aliases=['c'])
  async def chat(self, ctx, *, arg):

    try: 
      async with message.channel.typing():
        prompt = arg
    
        response = openai.Completion.create(model="text-davinci-003",
                                            prompt=prompt,
                                            temperature=0.7,
                                            max_tokens=2000,
                                            top_p=0.3,
                                            frequency_penalty=0.5,
                                            presence_penalty=0.2)
    
        print(prompt)
    
        message = response.choices[0].text
        await ctx.reply(message)

    except Exception as e:
      await message.reply(f"An exception has occured... :(\n {e}")


def setup(client):

  client.add_cog(Chat(client))
