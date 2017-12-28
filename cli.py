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
  This tool can fetch and post info to gitter\n
    '''
    pass


@cli.command()
@click.option('--message', type=str)
@pass_config
def post(config, message):
    click.echo(config.ob.post(message))


@cli.command()
@click.option('--info', default='u', help='Command to fetch info'
'based on the argument passed')
@pass_config
def get(config, info):
	gp = GitterPy()
	if info=='u':
		click.echo(config.ob.get_user())
	elif info=='r':
		click.echo(config.ob.get_rooms())
	elif info=='g':
		click.echo(config.ob.get_groups())
	elif info=='m':
		click.echo(config.ob.get_messages())
	else:
		click.echo('Invalid argument: Use gitterpy --help')