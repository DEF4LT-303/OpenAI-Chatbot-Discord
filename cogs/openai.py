from main import *
import openai


openai.api_key = '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'

class Chat(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['c'])
  async def chat(self, ctx, *, arg):

    prompt = arg

    completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

    print(prompt)

    message = completions.choices[0].text
    await ctx.send(message)


def setup(client):

  client.add_cog(Chat(client))
