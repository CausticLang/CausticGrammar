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
def Integer(ctx, *args, val: str, base: int = 10) -> atom.Integer:
    return atom.Integer(metadata=SourceInfo.from_ctx(ctx), val=val, base=base)
@action
def Char(ctx, *args, val: str) -> atom.Char:
    return atom.Char(metadata=SourceInfo.from_ctx(ctx), val=val)
@action
def Bytes(ctx, *args, val: str, raw: bool) -> atom.Bytes:
    return atom.Bytes(metadata=SourceInfo.from_ctx(ctx), val=val, raw=raw)
@action
def String(ctx, *args, val: str, raw: bool) -> atom.String:
    return atom.String(metadata=SourceInfo.from_ctx(ctx), val=val, raw=raw)