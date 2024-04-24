#!/bin/python3

#> Imports
from parglare import get_collector
from caustic.cst import atom
from caustic.parser import SourceInfo
#</Imports

#> Header >/
__all__ = ('action',)

action = get_collector()

@action
def Identifier(ctx, *args, name: str):
    return atom.Identifier(metadata=SourceInfo.from_ctx(ctx), name=name)
@action
def DottedIdentifier(ctx, *args, names: list[str]):
    return atom.DottedIdentifier(metadata=SourceInfo.from_ctx(ctx), names=names)
