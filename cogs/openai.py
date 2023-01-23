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

    if client.user.mentioned_in(message):
      message_raw = message.content.split()
      prompt = ' '

      prompt = prompt.join(message_raw[1:])

      response = openai.Completion.create(model="text-davinci-003",
                                          prompt=prompt,
                                          temperature=0.5,
                                          max_tokens=60,
                                          top_p=0.3,
                                          frequency_penalty=0.5,
                                          presence_penalty=0.0)

      response_text = response.choices[0].text
      await message.reply(response_text)

  @commands.command(aliases=['c'])
  async def chat(self, ctx, *, arg):

    prompt = arg

    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=prompt,
                                        temperature=0.5,
                                        max_tokens=60,
                                        top_p=0.3,
                                        frequency_penalty=0.5,
                                        presence_penalty=0.0)

    print(prompt)

    message = response.choices[0].text
    await ctx.reply(message)


def setup(client):

  client.add_cog(Chat(client))
