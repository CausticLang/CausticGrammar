#!/bin/python3

#> Imports
import operator
import parglare
from caustic import cst
#</Imports

#> Header >/
action = parglare.get_collector()

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
def proc_invokation(ctx, _, *, target: cst.expressions.Expression, args: dict | None) -> cst.procedure.Invokation:
    return cst.procedure.Invokation(source=cst.SourceInfo.from_parglare_ctx(ctx),
                                    target=target, **(args or {}))
