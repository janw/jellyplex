import rich_click as click

from jellyplex.models import ContextObj

pass_ctxobj = click.make_pass_decorator(ContextObj)
