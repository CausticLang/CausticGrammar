#!/bin/python3

#> Imports
from parglare import get_collector
from caustic.cst import bases, block
from caustic.parser import SourceInfo
from collections import abc as cabc
#</Imports

#> Header >/
__all__ = ('action',)

action = get_collector()

@action
def Line(ctx, *args, content: bases.CausticASTNode):
    return block.Line(metadata=SourceInfo.from_ctx(ctx), content=content)
@action
def Block(ctx, *args, body: cabc.Sequence[bases.CausticASTNode]):
    return block.Block(metadata=SourceInfo.from_ctx(ctx), body=body)
