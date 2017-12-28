import click
from gitter import GitterPy


class Config(object):
    def __init__(self):
        self.ob = GitterPy()

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@pass_config
def cli(config):
    '''
###############Welcome to GitterPy##############\n
Your command line client to interact with gitter\n    
################################################\n
  This tool can fetch and post info to gitter\n\n
##################User Manual###################\n
Currently this tool provides two commands `get` and `post`\n

Fetching user info: gitterpy get [--info] [argument]\n
The info argument can be:\n
1) [u] -> To fetch user's profile\n
2) [r] -> To fetch the rooms\n
3) [g] -> To fetch groups\n
4) [m] -> To fetch messages\n\n

Post a message to a room: gitterpy post [--message] [text]\n
[text] -> It is the message you want to post in enclosed by quotes
    '''
    pass


@cli.command()
@click.option('--message', type=str)
@pass_config
def post(config, message):
    status = config.ob.post(message)
    if status == 200:
        click.echo('Your message was successfully posted, Status Code: {}'.format(status))
    else:
        click.echo('Your message could not be posted, Status Code: {}'.format(status))


@cli.command()
@click.option('--info', default='u', help='Command to fetch info'
'based on the argument passed')
@click.option('--json', type=bool, default=True)
@pass_config
def get(config, info, json):
	gp = GitterPy()
	if info=='u':
		click.echo(config.ob.get_user(json))
	elif info=='r':
		click.echo(config.ob.get_rooms())
	elif info=='g':
		click.echo(config.ob.get_groups())
	elif info=='m':
		click.echo(config.ob.get_messages())
	else:
		click.echo('Invalid argument: Use gitterpy --help')