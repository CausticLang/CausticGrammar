#!/bin/python

#> Imports
import sys
import parglare
import operator
from pprint import pprint

from caustic import cst
from caustic.parser import error
#</Imports

#> Header
#</Header

#> Main >/
test = 'from a.b import c as d, e as f, g;'
test = '0$3:012012$;'
#test = 'f"test{{{test}}} t";'

def f(ctx, args, **kwargs):
    global p
    p = (ctx, args, kwargs)

def node_builder(ctx, args, **kwargs):
    return getattr(getattr(cst, ctx.production.user_meta['mod']),
                   ctx.production.user_meta.get('cls', ctx.production.symbol.name))(**kwargs)
def node_unpack_builder(ctx, args, **kwargs):
    print(args[ctx.production.user_meta.get('index', 0)])
    return node_builder(ctx, (), **(args[ctx.production.user_meta.get('index', 0)] | kwargs))

grammar = parglare.Grammar.from_file('./canonical/canonical.pg')
parser = parglare.GLRParser(grammar, lexical_disambiguation=True, actions={
    'pass_last': lambda ctx, args: args[-1],
    'pass_index': lambda ctx, args: args[ctx.production.index],
    'expr': lambda ctx, args, **kwargs: eval(ctx.production.expr, None, kwargs | {'ctx': ctx, 'args': args, 'kwargs': kwargs}),
    'obj': lambda ctx, _, **kwargs: kwargs,
    'pass_meta': lambda ctx, _, **kwargs: ctx.production.user_meta | kwargs,
    'node': node_builder,
    'unpack_node': node_unpack_builder,
}, tables=parglare.LALR)
try:
    forest = parser.parse(test)
    tree = forest.get_first_tree()
    parsed = parser.call_actions(tree)
except parglare.ParseError as pe:
    print(error.format_exc(pe), file=sys.stderr)
else:
    pprint(parsed)
