#!/bin/python

#> Imports
import parglare
import operator
from pprint import pprint

from caustic import cst
#</Imports

#> Header
#</Header

#> Main >/
test = 'from a.b import c as d, e as f, g;'
test = '0$3:012012$;'

def f(ctx, args, **kwargs):
    global p
    p = (ctx, args, kwargs)

def node_builder(ctx, args, **kwargs):
    return getattr(getattr(cst, ctx.production.user_meta['mod']),
                   ctx.production.user_meta.get('cls', ctx.production.symbol.name))

grammar = parglare.Grammar.from_file('./canonical.pg')
parser = parglare.GLRParser(grammar, lexical_disambiguation=True, actions={
    'pass_last': lambda ctx, args: args[-1],
    'pass_index': lambda ctx, args: args[ctx.production.index],
    'expr': lambda ctx, args, **kwargs: eval(ctx.production.expr, None, kwargs | {'ctx': ctx, 'args': args, 'kwargs': kwargs}),
    'obj': lambda ctx, _, **kwargs: kwargs,
    'pass_meta': lambda ctx, _, **kwargs: ctx.production.user_meta | kwargs,
    'node': node_builder,
})
forest = parser.parse(test)
tree = forest.get_first_tree()
parsed = parser.call_actions(tree)

pprint(parsed)
