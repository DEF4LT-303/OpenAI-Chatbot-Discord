from main import *
import openai


openai.api_key = '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'

class Chat(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['c'])
  async def chat(self, ctx, *, arg):

    prompt = arg

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.5,
    max_tokens=60,
    top_p=0.3,
    frequency_penalty=0.5,
    presence_penalty=0.0
  )

    print(prompt)

    message = response.choices[0].text
    await ctx.send(message)


def setup(client):

  client.add_cog(Chat(client))
