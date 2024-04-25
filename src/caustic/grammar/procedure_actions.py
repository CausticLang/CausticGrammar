#!/bin/python3

#> Imports
import operator
import itertools
from parglare import get_collector
from caustic.cst import bases, atom, expression
from caustic.parser import SourceInfo
from collections import abc as cabc
#</Imports

#> Header >/
__all__ = ('action',)

action = get_collector()

# Invoke
@action
def Invoke(ctx, *_, proc: bases.CausticASTNode, passed: cabc.Sequence[dict]) -> bases.CausticASTNode:
    # args:
    argis,args = zip(*((i,p) for i,p in enumerate(passed) if not p['kw']))
    # kwargs:
    return expression.Invoke(metadata=SourceInfo.from_ctx(ctx), proc=proc,
                             args=tuple(map(operator.itemgetter('val'), args)),
                             kwargs=tuple((expression.Invoke.VARKW_MARKER if p['var'] else p['name'], p['val'])
                                          for p in passed if p['kw']),
                             varargs=tuple(map(args.index, filter(operator.itemgetter('var'),
                                                                  map(passed.__getitem__, argis)))))

@action
def PosArg(ctx, *_, val: bases.CausticASTNode) -> dict:
    return {'kw': False, 'var': False, 'val': val}
@action
def VarPosArg(ctx, *_, val: bases.CausticASTNode) -> dict:
    return {'kw': False, 'var': True, 'val': val}
@action
def KWArg(ctx, *_, name: atom.Identifier, val: bases.CausticASTNode) -> dict:
    return {'kw': True, 'var': False, 'name': name, 'val': val}
@action
def VarKWArg(ctx, *_, val: bases.CausticASTNode) -> dict:
    return {'kw': True, 'var': True, 'val': val}
