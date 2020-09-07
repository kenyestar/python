import discord
from discord.ext import commands

client = commands.Bot( command_prefix = '.')

# Words
hello_words = [ 'hello', 'hi', 'привет', 'ky', 'здарова' ]
answer_words = [ 'узнать информацию о сервере', 'какая информация',
				'команды', 'команды сервера', 'что здесь делать' ]
goodbye_words = ['пока', 'bb', 'poka', 'пока всем' ] 

# Подключение бота
@client.event

async def on_ready():
	print ( 'BOT connected' )

# Clear message
@client.command ( pass_context = True )

async def clear ( ctx, amount = 100 ):
	await ctx.channel.purge( limit = amount )

# Clear command
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def helo( ctx, amount = 1 ):
	await ctx.channel.purge( limit = amount )

	author = ctx.message.author
	await ctx.send( f'Helo { author.mention }' )


# Kick
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None ):
	await ctx.channel.purge( limit = 1 )

	await member.kick ( reason = reason )



# Ответы на вопросы
@client.event

async def on_message ( message ):
		msg = message.content.lower()

		await client.process_commands(message)

		if msg in hello_words:
			await message.channel.send( 'Привет,чего хотел?' )

		if msg in answer_words:
			await message.channel.send( 'Пропиши в чат команду .help, и все узнаешь!' )

		if msg in goodbye_words:
			await message.channel.send ( 'Пока,удачи тебе!' )

# Connect

token = open( 'token.txt', 'r' ).readline()

client.run( token )