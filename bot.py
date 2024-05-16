import disnake
from disnake.ext import commands
from typing import Optional
import datetime
import os
from typing import Optional



bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(), test_guilds=[751479900619145257])

CENSORED_WORDS = ["гав", "вуф", "гув", "гуф", "гаф", "гум", "гумич", "гумыч", "гaв", 'гyм', "гуm", "гym"]
MEOW_WORDS = ["мяу", "мур", "муррр", "мяяу", "мяяяу", "meow", "mrrp", ':cat:', ':cat2:', "miau", "миау", "миaу"]
VOROBEY_WORDS = ["воробей", "vorobey", "в0робей", "вор0бей", "воробeй", "в0р0бей", "в0p0бей", "воpобей", "вoробeй", "ворoбeй", "снегирь", "снeгирь", "cнегирь", "cнeгирь", "снегиpь"]

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")
 
 
@bot.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id=1240634090118451291)
    channel = bot.get_channel(751721488285040670)

    embed = disnake.Embed(
        title="Новый работяга",
        description=f"{member.name}#{member.discriminator}",
        color=0xDC143C
    )

    await member.add_roles(role)
    await channel.send(embed=embed)


@bot.event
async def on_message(message):
    for content in message.content.split():
        for meow_word in MEOW_WORDS:
            if content.lower() == meow_word:
                await message.channel.send(f"{message.author.mention} __муррр, meoow))0)__😺🐱🐈:cat2::cat2:")
    await bot.process_commands(message)

@bot.listen()
async def on_message(message):
    for content in message.content.split():
        for vor in VOROBEY_WORDS:
            if content.lower() == vor:
                await message.channel.send(f"{message.author.mention} meow")
                
    await bot.process_commands(message)

@bot.listen()
async def on_message(message):
    for content in message.content.split():
        for censored_word in CENSORED_WORDS:
            if content.lower() == censored_word:
                await message.channel.send(f"{message.author.mention}, больше такого не пиши.😡🤬🤬")
    await bot.process_commands(message)



@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author}, у Вас недостаточно прав для выполнения данной команды.")
    elif isinstance(error, commands.UserInputError):
        await ctx.send(embed=disnake.Embed(
            description=f"Правильное использование команды: '{ctx.prefix}{ctx.command.name}' {ctx.command.brief}\nExample: {ctx.prefix}{ctx.command.usage}"
        ))

@bot.command(name="кик", aliases=["кикнуть", "kick"], usage=["!кик @soap46757 gag"])
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, *, reason="Причина не указана."):
    await ctx.send(f"Модератор {ctx.author.mention} кикнул {member.mention} по причине: {reason}", delete_after=60) #КИК
    await member.kick(reason=reason)
    await ctx.message.delete()

@bot.command(name="бан", aliases=["забанить", "ban"], usage=["!бан @soap46757 gag"])
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: disnake.Member, *, reason="Причина не указана."):
    await ctx.send(f"Модератор {ctx.author.mention} забанил {member.mention} по причине: {reason}", delete_after=60) #БАН
    await member.ban(reason=reason)
    await ctx.message.delete()

@bot.command(name="mute", aliases=["мьют", "замутить", "мут"], usage=["!мут @soap46757 gag"])
@commands.has_permissions(administrator=True)
async def mute(ctx, member: disnake.Member, *, reason="Причина не указана."):
    member = member
    role = disnake.utils.get(member.guild.roles, id=1240635273487056999)
    role2 = disnake.utils.get(member.guild.roles, id=1240634090118451291)
    await member.add_roles(role)
    await ctx.send(f"Модератор {ctx.author.mention} выдал мут пользователю {member.mention} по причине: {reason}", delete_after=60) #МУТ(ДАЁТ РОЛЬ МУТА)
    await member.remove_roles(role2)
    await ctx.message.delete()
    print(f'{datetime.datetime.now()} || {ctx.message.author} выдал мут пользователю {member.nick}/{member.mention} по причине: "{reason}".')

@bot.command(name="unmute", aliases=["анмьют", "размутить", "анмут"], usage=["!анмут @soap46757"])
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: disnake.Member):
    member = member
    role = disnake.utils.get(member.guild.roles, id=1240635273487056999)
    role2 = disnake.utils.get(member.guild.roles, id=1240634090118451291)
    await member.remove_roles(role)
    await ctx.send(f"Модератор {ctx.author.mention} снял мут с пользователя {member.mention}.", delete_after=60) #АНМУТ(ЗАБИРАЕТ РОЛЬ МУТА)
    await member.add_roles(role2)
    await ctx.message.delete()
    print(f'{datetime.datetime.now()} || {ctx.message.author} снял мут с {member.nick}/{member.mention}.')

@bot.slash_command(name="ban", usage=["/ban user:@Пидорас reason:gag"])
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member: disnake.Member, *, reason):
    await ctx.send(f"Модератор {ctx.author.mention} забанил  {member.mention} по причине: {reason}", delete_after=60) #БАН
    await member.ban(reason=reason)
    await ctx.message.delete()

@bot.slash_command(name="кик", usage=["/kick user:@soap46757 reason:gag"])
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, *, reason):
    await ctx.send(f"Модератор {ctx.author.mention} кикнул {member.mention} по причине: {reason}", delete_after=60) #КИК
    await member.kick(reason=reason)
    await ctx.message.delete()


@bot.slash_command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: disnake.Member):
    member = member
    role1 = disnake.utils.get(member.guild.roles, id=1240635273487056999)
    role2 = disnake.utils.get(member.guild.roles, id=1240634090118451291)
    await member.remove_roles(role1)
    await ctx.send(f"Модератор {ctx.author.mention} снял мут с пользователя {member.mention}.", delete_after=60) #АНМУТ(ЗАБИРАЕТ РОЛЬ МУТА)
    await member.add_roles(role2)
    await ctx.message.delete()

@bot.slash_command(name="mute", usage=["/mute user:@soap46757 reason:gag"])
@commands.has_permissions(administrator=True)
async def mute(ctx, member: disnake.Member, *, reason):
    member = member
    role1 = disnake.utils.get(member.guild.roles, id=1240635273487056999)
    role2 = disnake.utils.get(member.guild.roles, id=1240634090118451291)
    await member.add_roles(role1)
    await ctx.send(f"Модератор {ctx.author.mention} выдал мут пользователю {member.mention} по причине: {reason}", delete_after=60) #МУТ(ДАЁТ РОЛЬ МУТА)
    await member.remove_roles(role2)
    await ctx.message.delete()

class Viberi(disnake.ui.View):  
    def __init__(self):  
        super().__init__(timeout=10.0)  
        self.value = None 
      
    @disnake.ui.button(label="Делать", style=disnake.ButtonStyle.green)  
    async def prinyal(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):  
        await inter.send("Вы сделали.")  
        self.value = True  
        self.stop() 
 
    @disnake.ui.button(label="Не делать", style=disnake.ButtonStyle.red)  
    async def otkazal(self, button: disnake.ui.Button, inter: disnake.CommandInteraction):  
        await inter.send("Вы отказались делать.")  
        self.value = False  
        self.stop() 
 
@bot.command(name="delat")  
async def ask_delat(ctx, member: disnake.Member):  
    print("Команда вызвана")  # Отладочное сообщение 
    view = Viberi()  
    await ctx.send(f"{ctx.message.author.mention} предложил делать {member.mention}, {member.mention} Вы согласны?", view=view)  
    await view.wait()  
  
    if view.value == True:  
        await ctx.send("Кек)))")  
    elif view.value == False:  
        await ctx.send("Анлак(((")  
    else:  
        await ctx.send("Нет ответа") 