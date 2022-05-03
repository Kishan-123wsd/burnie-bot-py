from pydoc import describe
import discord
from discord.ext import commands
import sys
import os
import traceback
import json



bot = commands.Bot(command_prefix='.', intents = discord.Intents().all())




@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f" {len(bot.guilds)} Servers | .help"))
  print("Bot Is Online")
bot.remove_command('help')



#addition



@bot.group(invoke_without_command=True)
async def help(ctx, user:discord.Member=None):
    if user==None:
        user=ctx.author
    embed = discord.Embed(
      title = 'Help Menu Of BurnieBot',
      description = 'Type `.help <module | command>` For More Information.',
      color=0xfa0727,
      
    
    )
    embed.add_field(name='<:mod:970701679710318673> Moderation',value='`kick`, `ban`, `mute`, `unmute`, `unban`, `purge`, `lock`, `unlock`, `roleadd`,`roleremove`,`addrole` `addchannel`')

    embed.add_field(name='🏑  Fun Commands',value='`snipe`, `whois`, `serverinfo`, `say`, `embedsay`, `nick`, `dm`, `avatar`, `add`, `substract` ',
    ).add_field(name='<:ifo:970701580745728100> Information', value='`invite`, `support`, `vote`, `premium`, `botinfo`')
    embed.add_field(name='<:lnks:970701629215080478> Important Links', value='[Invite Me](https://discord.com/api/oauth2/authorize?client_id=970555340775112704&permissions=8&scope=bot)  [Vote Me](https://discord.ly/burnie/vote) [Support Server](https://discord.gg/aQ24CNtqrg) ')
    embed.set_footer(text='Thanks For Using BurnieBot, Type .<command | module> For More Information.',
    ).set_thumbnail(
        url = user.avatar_url
    ).set_footer(
        text = f'Requested By - {ctx.author} ',
        icon_url = ctx.author.avatar_url
    )
      
    msg=await ctx.channel.send(embed=embed)
    await msg.add_reaction('<:mbatick:968065370701312041>') 



@help.command()
async def mute(ctx, user:discord.Member=None):
  if user==None:
        user=ctx.author
  ban = discord.Embed(
    title = "Moderation",
    description =  '```If Somebody is breaking rules again and again | mute him from the server as punishment```',
    color = 0xfa0727
  ).add_field(
    name = "Aliases",
    value = "`No Aliases`"
  ).add_field(
    name = "Usage",
    value = "`.mute <member> [reason]` "
  ).set_thumbnail(
    url = user.avatar_url
  ).set_footer(
    text = f'Requested By - {ctx.author}',
    icon_url = ctx.author.avatar_url
  )
  await ctx.reply(embed=ban)

@help.command()
async def ban(ctx, user:discord.Member=None):
  if user==None:
        user=ctx.author
  ban = discord.Embed(
    title = "Moderation",
    description =  '```If Somebody is breaking rules again and again | ban him from the server as punishment```',
    color = 0xfa0727
  ).add_field(
    name = "Aliases",
    value = "`No Aliases`"
  ).add_field(
    name = "Usage",
    value = "`.ban <member> [reason]` "
  ).set_thumbnail(
    url = user.avatar_url
  ).set_footer(
    text = f'Requested By - {ctx.author}',
    icon_url = ctx.author.avatar_url
  )
  await ctx.reply(embed=ban)

@help.command()
async def kick(ctx, user:discord.Member=None):
  if user==None:
        user=ctx.author
  kick = discord.Embed(
    title = "Moderation",
    description =  '```If Somebody is breaking rules again and again | kick him from the server as punishment```',
    color = 0xfa0727
  ).add_field(
    name = "Aliases",
    value = "`No Aliases`"
  ).add_field(
    name = "Usage",
    value = "`.kick <member> [reason]` "
  ).set_thumbnail(
    url = user.avatar_url
  ).set_footer(
    text = f'Requested By - {ctx.author}',
    icon_url = ctx.author.avatar_url
  )
  await ctx.reply(embed=kick)

@help.command()
async def unmute(ctx, user:discord.Member=None):
  if user==None:
        user=ctx.author
  ban = discord.Embed(
    title = "Moderation",
    description =  '```Unmute Specified Member```',
    color = 0xfa0727
  ).add_field(
    name = "Aliases",
    value = "`No Aliases`"
  ).add_field(
    name = "Usage",
    value = "`.unmute <member>` "
  ).set_thumbnail(
    url = user.avatar_url
  ).set_footer(
    text = f'Requested By - {ctx.author}',
    icon_url = ctx.author.avatar_url
  )
  await ctx.reply(embed=ban)




@bot.command()
@commands.has_permissions(administrator=True, manage_roles=True)
async def reactrole(ctx, emoji, role: discord.Role, *, message):

    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {'role_name': role.name, 
        'role_id': role.id,
        'emoji': emoji,
        'message_id': msg.id}

        data.append(new_react_role)

    with open('reactrole.json', 'w') as f:
        json.dump(data, f, indent=4)


    










@help.command()
async def unban(ctx, user:discord.Member=None):
  if user==None:
        user=ctx.author
  ban = discord.Embed(
    title = "Moderation",
    description =  '```Unban Specified Member```',
    color = 0xfa0727
  ).add_field(
    name = "Aliases",
    value = "`No Aliases`"
  ).add_field(
    name = "Usage",
    value = "`?unban <member>` "
  ).set_thumbnail(
    url = user.avatar_url
  ).set_footer(
    text = f'Requested By - {ctx.author}',
    icon_url = ctx.author.avatar_url
  )
  await ctx.reply(embed=ban)

@help.command()
async def add(ctx, user:discord.Member=None):
  if user==None:
        user=ctx.author
  ban = discord.Embed(
    title = "Fun Command",
    description =  '```Add Command```',
    color = 0xfa0727
  ).add_field(
    name = "Aliases",
    value = "`No Aliases`"
  ).add_field(
    name = "Usage",
    value = "`.add [number] [number]` "
  ).set_thumbnail(
    url = user.avatar_url
  ).set_footer(
    text = f'Requested By - {ctx.author}',
    icon_url = ctx.author.avatar_url
  )
  await ctx.reply(embed=ban)



@help.command()
async def substract(ctx, user:discord.Member=None):
  if user==None:
        user=ctx.author
  ban = discord.Embed(
    title = "Fun Command",
    description =  '```Substract Command```',
    color = 0xfa0727
  ).add_field(
    name = "Aliases",
    value = "`minus`"
  ).add_field(
    name = "Usage",
    value = "`.substract [number] [number] ` "
  ).set_thumbnail(
    url = user.avatar_url
  ).set_footer(
    text = f'Requested By - {ctx.author}',
    icon_url = ctx.author.avatar_url
  )
  await ctx.reply(embed=ban)




@bot.command()
async def invite(ctx):
    invite = discord.Embed(
        title = "Invite Link Of BurnieBot",
        description = '''>>> • [Click here To Invite BurnieBot](https://discord.com/api/oauth2/authorize?client_id=970555340775112704&permissions=8&scope=bot)
• [Click here To Join Support Server](https://discord.gg/aQ24CNtqrg)''',
        color = 0xfa0727
    )
    await ctx.reply(embed=invite)


@bot.command()
async def premium(ctx):
    await ctx.reply(f"Premium Is Coming soon. ")



@bot.command(aliases=['minus'])
async def substract(ctx, a: int, b: int):
    embed = discord.Embed(
        title =  "Substraction Of Two Numbers",
        description  = a-b,
        color = 0xfa0727

    )
    await ctx.reply(embed=embed)



@bot.command()
async def botinfo(ctx, user:discord.Member=None):
    if user==None:
        user=ctx.author
    guild = ctx.guild
    bot_info = discord.Embed(
        title = "BurnieBot",
        description = '''About BurnieBot''',
        color = 0xfa0727
        ).add_field(
            name = "Bot Latency",
            value = f"Ping {round(bot.latency*1000)}"
        )   
    bot_info.add_field(
        name = "Developers",
        value = '''[Kishan#4983](https://discord.com/users/968156311856480278)
[Austyun#0001](https://discord.com/users/965166145185407036) 
[Raihan#9107](https://discord.com/users/904698970427760681)'''

        ).set_thumbnail(
        url = user.avatar_url
    ).set_footer(
        text = f'Requested By - {ctx.author} ',
        icon_url = ctx.author.avatar_url
    )
    await ctx.send(embed=bot_info)





@bot.command()
async def ping(ctx):
    ping = discord.Embed(
        title = "Ping Command",
        description  = f" <:mbatick:968065370701312041> Pong!! `{round(bot.latency*1000)}` `ms`",
        color = 0xfa0727
    )
    await ctx.reply(embed=ping)



@bot.command(aliases=['es'])
async def embedsay(ctx, *, message):
    embedsay = discord.Embed(
        title = "",
        description = f"{message} ",
        color = discord.Color.random()
    )
    await ctx.send(embed=embedsay)


@bot.command()
async def say(ctx,message):
    await ctx.send(f" {message} ")



    
    

@bot.command()
async def support(ctx):
    embed = discord.Embed(
        title = "Support Server Link Of Burnie Bot?",
        description = "Do You Want Support Server Link?? Click [here](https://discord.gg/aQ24CNtqrg) ",
        color = 0xfa0727
    )
    await ctx.send(embed=embed)



    







@bot.command(name="whois")
async def whois(ctx,user:discord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = discord.Embed(colour=0xfa0727,timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Requested by - {ctx.author}',
  icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)

  
 
    embed.add_field(name='Bot?',value=user.bot,inline=False)

    embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)

    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_roles=True)
async def poll(ctx,*,message):
  embed=discord.Embed(title=" ",
                     description=f"{message}",
                     color=0x21FFB8)
 
  msg=await ctx.channel.send(embed=embed)
  await msg.add_reaction('<:mbatick:968065370701312041>')  
  await msg.add_reaction('<:mbatcross:968065739925913630>')


@help.command()
async def poll(ctx, user:discord.Member=None):
  if user==None:
        user=ctx.author
  ban = discord.Embed(
    title = "Moderation",
    description =  '```Poll Command```',
    color = 0xfa0727
  ).add_field(
    name = "Aliases",
    value = "`No Aliases`"
  ).add_field(
    name = "Usage",
    value = "`.poll <message>` "
  ).set_thumbnail(
    url = user.avatar_url
  ).set_footer(
    text = f'Requested By - {ctx.author}',
    icon_url = ctx.author.avatar_url
  )
  await ctx.reply(embed=ban)


@bot.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = False)
  await ctx.send( ctx.channel.mention + " is now locked")

@bot.command(pass_content=True)
async def nick(ctx, member: discord.Member, nick):
  await member.edit(nick=nick)
  await ctx.send(f"Nickname Was Changed For {member.mention}")


@bot.command()
@commands.has_permissions(manage_roles=True)
async def roleadd(ctx, role: discord.Role, user: discord.Member):
  await user.add_roles(role)
  embed = discord.Embed(
    title='ROLE ADD COMMAND',
    description=f'  Given Role To {role.mention} to {user.mention}',
    color=0xfa0727
  )
  await ctx.send(embed=embed)


 

@bot.command()
@commands.has_permissions(manage_roles=True)
async def roleremove(ctx, role: discord.Role, user: discord.Member):
  await user.remove_roles(role)
  embed = discord.Embed(
    title='ROLE REMOVE COMMAND',
    description=f'Taked Role From {role.mention} to {user.mention}.',
    color=0xfa0727
  )
  await ctx.send(embed=embed)


@bot.command()
async def avatar(ctx,member: discord.Member):
  

    icon_url = member.avatar_url

    avatarEmbed = discord.Embed(title = f"{member.name}\'s Avatar", color = 0x21FFB8)

    avatarEmbed.set_image(url = f"{icon_url}")

    avatarEmbed.timestamp = ctx.message.created_at

    await ctx.send(embed = avatarEmbed)


@bot.command()
async def add(ctx, a:int, b:int):
    add = discord.Embed(
        title = "Addition Command",
        description = a + b,
        color = 0xfa0727
    )
    await ctx.reply(embed=add)



@bot.command()
@commands.has_permissions(manage_channels = True)
async def dm(ctx, user: discord.User, *, msg):
  await ctx.send('Succesfull')
  await user.send(f'<:mbatick:968065370701312041> {msg}')


@bot.command()
@commands.has_permissions(manage_channels = True)
async def addchannel(ctx, *name):
  for name in name:
    await ctx.guild.create_text_channel(name)
    await ctx.send(f"<:mbatick:968065370701312041> {name} has been created")







@bot.command()
@commands.has_permissions(manage_channels = True)
async def unlock(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = True)
  await ctx.send(f' <:mbatick:968065370701312041> {ctx.channel.mention}   is now unlocked')








@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name,
                                               member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'<:mbatick:968065370701312041> Unbanned {user.mention}')


@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member,*,reason=None):
    await member.kick(reason=reason)
    await ctx.channel.send(f"<:mbatick:968065370701312041> {member.name} Has Been Kicked For The Reason {reason} ")

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.channel.send(f"<:mbatick:968065370701312041> {member.name} Has Been Banned!! For The Reason {reason}  ")



@bot.command()
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def addrole(ctx, *, name):
    guild = ctx.guild
    await guild.create_role(name=name)
    await ctx.send(f'<:tick:966364754954321931> Role {name} has been created')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member,*,reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channels in guild.channels:
            await channels.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=False )
            await member.add_roles(mutedRole, reason=reason)
            await ctx.channel.send(f"Muted {member.mention} for the reason{reason} ")
            await member.send(f"You Have Been Muted In {guild.name} ")

@bot.command(aliases=['si'])
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title=name + " Server Information",
                          description=description,
                          color=0x21FFB8)
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member : discord.Member):
    guild = ctx.guild


    MutedRole = discord.utils.get(guild.roles, name="Muted")
    await member.remove_roles(MutedRole)
        
    unmute_role = discord.Embed(
        title = f" {member.mention} ",
        description =f' {member.mention} You Have Been Unmuted!! ',
        color = 0xfa0727

        )
    await ctx.send(embed=unmute_role)
    await member.send(f" {member.mention} You Have Been Unmuted In {guild.name} ")

@bot.command(aliases=['mc'])
async def membercount(ctx):
  memberCount = str(ctx.guild.member_count)
  embed = discord.Embed(
    title = f" {ctx.guild.name} ",
    description = "Total Members",
    color = 0xfa0727
  )
  embed.add_field(name="Member Count", value=memberCount, inline=True)
  await ctx.send(embed=embed)



@bot.command()
async def purge(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send(f"Purged {amount} ")
    





@bot.listen('on_message')
async def stuff(message):
    if message.content.startswith("<@970555340775112704>"):
        

      Kishan = discord.Embed(
        title = '',
        description = '''Hey, I'm BurnieBot

Please use the following command instead: `.help`

If you continue to have problems, consider asking for help [Click Here](https://discord.gg/aQ24CNtqrg)''',
        color = 0xfa0727
      )

      msg = await message.channel.send(embed=Kishan)
      

extensions = [
              "cogs.moderation",
              
              

]
if __name__ == "__main__":
  for extension in extensions:
    try:
      bot.load_extension(extension)
    except Exception as e:
      print(f"Error Loading {extension}", file=sys.stderr)
      traceback.print_exc()


bot.run("OTcwNTU1MzQwNzc1MTEyNzA0.Ym9qGQ.8qQuEnio3JFbIeyQF_hVZxLucFc")
