#!/bin/python3

#> Imports
import typing
import operator
import itertools
from parglare import get_collector
from caustic.cst import bases, atom, block, expression, statement
from caustic.parser import SourceInfo
from collections import abc as cabc
#</Imports

#> Header >/
__all__ = ('action',)

action = get_collector()

@action
def pass_last(ctx, args, *_) -> typing.Any: return args[-1]
@action
def pass_dict(ctx, *_, **kwargs) -> dict: return kwargs

# Invoke
@action
def Invoke(ctx, *_, proc: bases.CausticASTNode, passed: cabc.Sequence[dict]) -> bases.CausticASTNode:
    argis,args = zip(*((i,p) for i,p in enumerate(passed) if not p['kw']))
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

# Procedure
KWONLY_MARKER = object()

@action
def VarParam(ctx, *_, **kwargs) -> dict | object:
    return KWONLY_MARKER if 'type' not in kwargs else kwargs

@action
def ProcedureParams(ctx, *_,
                    pos_only: cabc.Sequence[dict] | None = None,
                    pos_or_kw: cabc.Sequence[dict] | None = None,
                    var_pos_and_kw_only: dict | None = None,
                    var_kw: cabc.Sequence[dict] | None = None) -> dict:
    res = {'params': []}
    # positional only
    if pos_only is None: res['pos_only'] = 0
    else:
        res['pos_only'] = len(pos_only)
        for pop in pos_only:
            res['params'].append((pop['name'], pop['type']))
    # positional or keyword
    if pos_or_kw is not None:
        for pokwp in pos_only:
            res['params'].append((pokwp['name'], pokwp['type']))
    # var-positional and keyword
    if var_pos_and_kw_only is None:
        res['var_pos'] = None
        res['kw_only'] = None
    else:
        # var-positional
        res['var_pos'] = (None if (var_pos_and_kw_only['var_pos'] is KWONLY_MARKER)
                          else (var_pos_and_kw_only['var_pos']['name'],
                                var_pos_and_kw_only['var_pos']['type']))
        # keyword-only
        if var_pos_and_kw_only['kw_only'] is None:
            res['kw_only'] = None
        else:
            res['kw_only'] = len(var_pos_and_kw_only['kw_only'])
            for kwop in var_pos_and_kw_only['kw_only']:
                res['params'].append((kwop['name'], kwop['type']))
    # var-keyword
    res['var_kw'] = None if var_kw is None else (var_kw['name'], var_kw['type'])
    # return
    return res

## Expression
@action
def ProcedureExpr(ctx, *_, type: atom.DottedIdentifier | None, params: dict | None, body: block.Block | None) -> expression.ProcedureExpr:
    kwargs = {'params': ()} if params is None else params
    return expression.ProcedureExpr(metadata=SourceInfo.from_ctx(ctx), return_type=type, **kwargs, body=body)
## Statement
@action
def ProcedureStmt(ctx, *_, name: atom.Identifier, type: atom.DottedIdentifier | None, params: dict | None, body: block.Block | None) -> statement.ProcedureStatement:
    kwargs = {'params': ()} if params is None else params
    return statement.ProcedureStatement(metadata=SourceInfo.from_ctx(ctx), name=name, return_type=type, **kwargs, body=body)
