#!/bin/python3

#> Imports
from parglare import get_collector
from caustic.parser import SourceInfo
from caustic.cst import statement
from caustic.cst.bases import CausticASTNode
from collections import abc as cabc
#</Imports

#> Header >/
__all__ = ('action',)

action = get_collector()

@action
def Directive(ctx, *_, name: str, args: cabc.Sequence[str]) -> statement.Directive:
    return statement.Directive(metadata=SourceInfo.from_ctx(ctx), name=name, args=args)
