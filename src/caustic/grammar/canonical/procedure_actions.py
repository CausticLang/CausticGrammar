#!/bin/python3

#> Imports
import operator
import parglare
import itertools
from caustic import cst
#</Imports

#> Header >/
action = parglare.get_collector()

# Declaration
@action
def proc_param(ctx, _, *, name: cst.expressions.atoms.Identifier, type: cst.typedecl.Type | None,
               default: cst.expressions.Expression | None = None) -> cst.procedure.Param:
    return cst.procedure.Param(name=name, type=type, default=default)

@action
def proc_params(ctx, _, *, pos_only: list[cst.procedure.Param] | None = None,
                pos_or_kw: list[cst.procedure.Param] | None = None, var_pos_and_kwonly: dict | None = None) -> dict:
    params = {'params': []}
    if pos_only is not None:
        params['pos_only'] = len(pos_only)
        params['params'].extend(pos_only)
    if pos_or_kw is not None:
        params['params'].extend(pos_or_kw)
    if var_pos_and_kwonly is not None:
        if (var_pos := var_pos_and_kwonly.get('var_pos')) is not None:
            params['var_pos'] = var_pos
        if (kw_only := var_pos_and_kwonly.get('kw_only')) is not None:
            params['kw_only'] = len(kw_only)
            params['params'].extend(kw_only)
    return params


@action
def proc_expr(ctx, _, *, return_type: cst.typedecl.Type | None, params: dict | None, body: cst.block.Block) -> cst.procedure.ProcedureExpr:
    return cst.procedure.ProcedureExpr(source=cst.SourceInfo.from_parglare_ctx(ctx),
                                       body=body, return_type=return_type, **(params or {'params': None}))
@action
def proc_stmt(ctx, _, *, name: cst.expressions.atoms.Identifier, return_type: cst.typedecl.Type | None, params: dict | None, body: cst.block.Block) -> cst.procedure.ProcedureExpr:
    return cst.procedure.ProcedureStmt(source=cst.SourceInfo.from_parglare_ctx(ctx),
                                       name=name, body=body, return_type=return_type, **(params or {'params': None}))

# Invokation
@action
def proc_args(ctx, _, *, args: list[dict] | None = None, kwargs: list[dict] | None = None) -> dict:
    pargs = {}
    # Pos args
    if args is not None:
        pargs['args'] = []
        pargs['unpack_args'] = set()
        for i,a in enumerate(args):
            pargs['args'].append(a['val'])
            if a['unpack']: pargs['unpack_args'].add(i)
    # KW args
    if kwargs is not None:
        pargs['kwargs'] = list(map(operator.itemgetter('name', 'val'), kwargs))
    # Finish
    return pargs

@action
def proc_invoke(ctx, _, *, target: cst.expressions.Expression, args: dict | None) -> cst.procedure.Invokation:
    return cst.procedure.Invokation(source=cst.SourceInfo.from_parglare_ctx(ctx),
                                    target=target, **(args or {}))
