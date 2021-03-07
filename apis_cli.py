import click

@click.group()
def apis():
    """A CLI wrapper for the API of Public APIs."""

if __name__ == '__main__':
    apis(prog_name='apis')

@click.option('-a', '--no-auth', is_flag=True, help='Filter out APIs with required auth')
@apis.command()
def entries(no_auth: bool):
    """List all cataloged APIs."""

