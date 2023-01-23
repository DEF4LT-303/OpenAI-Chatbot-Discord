from main import *


class Help(commands.Cog):
  
    def __init__(self, client):

        self.client = client

    @commands.command(aliases=['info'], pass_context=True)
    async def help(self, ctx):


        with open('./cogs/Data/prefixes.json', 'r') as f:
            prefixes = json.load(f)


        prefix = prefixes[str(ctx.guild.id)]


        embedVar = discord.Embed(title="Help Message",
                               description="Showing all the commands",
                               color=0x00ff00)
        embedVar.add_field(
            name=":exclamation: Prefix",
            value=
            f"○ Change Prefix: `prefix <argument>`\nThe current Prefix is `{prefix}`",
            inline=False)

        embedVar.add_field(
            name=":wrench: Utility",
            value=
            '○ Invite Link: `invite`\n○  CGPA Calculator: `cg <parameters>`\n○ Chat: `$chat <arg>`',
            inline=True)


        embedVar.set_footer(text=f'Requested by {ctx.author}',
                            icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embedVar)

       


def setup(client):
    # Every extension should have this function
    client.add_cog(Help(client))
