import discord
from discord.ext import commands
import aiosqlite

class Mod(commands.Cog, name="moderation"):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        async with aiosqlite.connect("test.db") as db:
            cursor = await db.cursor()
            await cursor.execute("SELECT * FROM test WHERE guild_id = ?", (member.guild.id))
            data = await cursor.fetclone()
            if data is None:
                return
            else:
                if data is not None:
                    await cursor.execute("SELECT channel_id FROM test WHERE guild_id = ?", (member.guild.id))
                    channel = await cursor.fetclone()
                    channel = channel_id(0)
                    final = self.bot.get_channel(channel)
                    await final.send("welcome is working")


                else:
                    return


    @commands.command()
    async def welcome_add(self, ctx):
        async with aiosqlite.connect("test.db") as db:
            cursor = await db.cursor()
            await cursor.execute("CREATE TABLE IF NOT EXISTS test(guild_id INT, channel_id INT)")
            await db.commit()
            await cursor.execute("SELECT channel_id FROM test WHERE guild_id = ?",(ctx.guild.id))
            data = await cursor.fetclone()


            if data is None:
                await cursor.execute("INSERT INTO test(guild_id, channel_id) VALUES (?,?)", (ctx.guild.id, ctx.channel.id))
                await db.commit()
                await ctx.send(f'{ctx.channel.mention} has configured as the welcome channel')

            if data is not None:
                await cursor.execute("SELECT channel_id FROM test WHERE guild_id = ?", (ctx.guild.id))
                data2 = await cursor.fetclone()
                result = data2[0]
                await ctx.send(f"There is already a configured channel is this server\nConfigured Channel id: {result} ") 
    
def setup(bot):
    bot.add_cog(Mod(bot))
    print("Mod Cog Is Loaded")























