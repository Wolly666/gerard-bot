#Discord
import discord
import random
import time

from auth import authenticate
from datetime import datetime


#Discord
client = discord.Client()
passf = open('pass', 'r+')
passw = passf.read()
client.login('rivalo5@gmail.com', passw)
update = open('update', 'r+')
update_check = update.read()
elco_id_test = '104730674921021440' #Test server
elco_id = '100365048907583488'
sfw_channel = '106475514138472448'
admin = 'Rivalo'

#Buienradar

album = None # You can also enter an album ID here
image_path = 'http://www.buienradar.nl/image?type=zozw'
clientImg = authenticate()



@client.event
def on_message(message):
	global image
	if message.content.startswith('!help'):
		helpf = open('help')
		client.send_message(message.channel, helpf.read())
		helpf.close()
	if message.content.startswith('!changelog'):
		changelog = open('changelog')
		client.send_message(message.channel, changelog.read())
		changelog.close()

	if message.content.startswith('!hallo'):
		client.send_message(message.channel, 'Hallo {}!'.format(message.author.mention()))
	if message.content.startswith('!slope'):
		client.send_message(message.channel, 'http://i.imgur.com/d5ML2op.png')
	if message.content.startswith('!google'):
		client.send_message(message.channel, 'https://www.google.nl/#q={}'.format(message.content.split("!google ",1)[1].replace (" ", "+")))

	if message.content.startswith('!naam'):
		client.edit_profile('loofam', username=message.content.split("!naam ",1)[1])
	if message.content.startswith('!kanaal'):
		client.edit_channel(message.channel, name=message.content.split("!kanaal ",1)[1])
	if message.content.startswith('!motd'):
		client.edit_channel(message.channel, topic=message.content.split("!motd ",1)[1])

	if message.content.startswith('!ecchi'):


		if  message.channel.id == sfw_channel:	
			client.send_message(message.channel, 'Plox, geen halve pr0n in de Safe for work chat')
		else:
			ecchi = random.choice(open('ecchi').readlines())
			client.send_message(message.channel, ecchi)
		
	if message.content.startswith('!aaa'):
		client.send_message(message.channel, 'AAAA {}, LET MIE TINK OF THAT KWESTJUN'.format(message.author.mention()))
		client.send_message(message.channel, 'THAT IS:')
		ball8 = random.choice(open('ball8').readlines())
		time.sleep(2)
		client.send_message(message.channel, ball8)

	if message.content.startswith(("!noice", "!nice")):
		client.send_message(message.channel, 'http://media.giphy.com/media/yJFeycRK2DB4c/giphy.gif')
		client.send_message(message.channel, 'Click, nice!', False, True)
	if message.content.startswith(("!buien", "!buienradar", "!weer", "!regen")):
		client.send_message(message.channel, '{0}'.format(image['link']))
		
	if message.content.startswith('!updatebuien'):
		if str(message.author) == admin:
			client.send_message(message.channel, 'Momentje Fuhrer {}, dit gaat even duren.'.format(message.author.mention()))
			image = clientImg.upload_from_url(image_path, config=None, anon=True)
			client.send_message(message.channel, 'Kek, klaar')
		else:
			client.send_message(message.channel, 'Nee {}, daarvan wordt ik fucking traag'.format(message.author.mention()))

	if message.content.startswith(("http://bit", "http://kona", "https://bit","https://kona","http://www.bit", "http://www.kona" )):
		if  message.channel.id == sfw_channel:	
			client.delete_message(message)
			client.send_message(message.channel, 'Bit.ly en Konachan WRONG')
			
	if message.content.startswith('!repo'):
		client.send_message(message.channel, 'https://github.com/Rivalo/gerard-bot')





		


		
		
@client.event
def on_ready():
	global image
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	print('Updated:')
	print(update_check.startswith('yes'))
	client.send_message(elco_id, 'Goedemorgen, even opstarten')

	image = clientImg.upload_from_url(image_path, config=None, anon=True)

	client.send_message(elco_id, 'Buienradar geladen, slope kompjoeted, wrong!')


	
	

	if update_check.startswith('yes'):
		client.send_message(elco_id, 'Ah Gerard! Er is een update! Check de fucking changelog')
		print('Printing Update')
		update.seek(0)
		update.write('no')
		update.truncate()
		update.close()

	update.close()


client.run()
