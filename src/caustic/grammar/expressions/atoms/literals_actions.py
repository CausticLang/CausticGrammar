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
def Integer(ctx, *_, val: str, base: int = 10) -> atom.Integer:
    return atom.Integer(metadata=SourceInfo.from_ctx(ctx), val=val, base=base)
@action
def Char(ctx, *_, val: str) -> atom.Char:
    return atom.Char(metadata=SourceInfo.from_ctx(ctx), val=val)
@action
def Bytes(ctx, *_, val: str, raw: bool) -> atom.Bytes:
    return atom.Bytes(metadata=SourceInfo.from_ctx(ctx), val=val, raw=raw)
@action
def String(ctx, *_, val: str, raw: bool) -> atom.String:
    return atom.String(metadata=SourceInfo.from_ctx(ctx), val=val, raw=raw)
