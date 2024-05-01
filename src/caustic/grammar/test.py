#!/bin/python3

#> Imports
import sys
import parglare
from pprint import pprint

from caustic import cst
from caustic.parser.error import format_exc
#</Imports

#> Header
def mknode(ctx, _, **kwargs):
    kwargs = {k: v for k,v in ctx.production.user_meta.items() if k != 'node'} | kwargs
    try:
        return (cst.CSTNode.NODE_DIRECTORY[ctx.production.node](
            source=cst.SourceInfo.from_parglare_ctx(ctx), **kwargs))
    except AttributeError as ae:
        ae.add_note(f'In production: {ctx.production!r}')
        raise ae

actions = {
    'obj': lambda ctx, _, **kwargs: kwargs,
    'expr': lambda ctx, args, **kwargs: eval(cxt.production.expr, kwargs | {'ctx': ctx, 'args': args, 'kwargs': kwargs}),
    'pass_last': lambda ctx, args: args[-1],
    'pass_meta': lambda ctx, _, **kwargs: ctx.production.user_meta | kwargs,
    'pass_index': lambda ctx, args: args[ctx.production.index],

    'node': mknode,
    'unpack_node': lambda ctx, args, **kwargs: mknode(ctx, (), **(args[ctx.production.user_meta.get('index', 0)] | kwargs))
}
#</Header

#> Main >/
import os
try: os.remove('./canonical/canonical.pgt')
except: pass
print('Parsing grammar')
grammar = parglare.Grammar.from_file('./canonical/canonical.pg')
print('Building parser')
parser = parglare.GLRParser(grammar, lexical_disambiguation=False, actions=actions)

try:
    forest = parser.parse(input('Ready for input\n'))
    tree = forest.get_first_tree()
    parsed = parser.call_actions(tree)
except parglare.ParseError as pe:
    print(format_exc(pe, verbose_got=True), file=sys.stderr)
else:
    pprint(parsed)
