import click


@click.group(short_help="detroit_data CLI.")
def detroit_data():
    """detroit_data CLI.
    """
    pass


@detroit_data.command()
@click.argument("name", default="detroit_data")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [detroit_data]
