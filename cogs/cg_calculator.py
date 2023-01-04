from main import *

class CGcalculator(commands.Cog):

  def __init__(self, client):

    self.client = client

  @commands.command(aliases=['cg'], pass_context=True)
  async def cgpa(self, ctx):

    def check(m):
      return m.author == ctx.author

    try:

      await ctx.reply("**What is your current CGPA:** ")
  
      curr = await self.client.wait_for("message", check=check)
      curr_cg = float(curr.content)

      await ctx.reply("**How many courses have you completed:** ")

      courses = await self.client.wait_for("message", check=check)
      curr_courses = int(courses.content)

      sum = curr_cg*curr_courses

      await ctx.reply("**How many courses have you taken this sem:** ")

      taken = await self.client.wait_for("message", check=check)
      courses_taken = int(taken.content)

      await ctx.reply("**Input indivitual CG for courses separated by space (4 3 3.7 3.3):** ")

      sep_cg = await self.client.wait_for("message", check=check)
      sep_cg_list = sep_cg.content.split()

      if len(sep_cg_list) > courses_taken:
        raise Exception()

      else:
        for i in sep_cg_list:
          sum += float(i)

        new_cg = sum / (curr_courses + courses_taken)

        await ctx.reply(f"**Your CG will be:** `{round(new_cg, 2)}`")

    except:
      await ctx.reply("Please verify your info again...")


def setup(client):

  client.add_cog(CGcalculator(client))
  