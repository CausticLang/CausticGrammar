#!/bin/python3

#> Imports
from parglare import get_collector
from caustic.cst import constant
from caustic.parser import SourceInfo
#</Imports

#> Header >/
__all__ = ('action',)

action = get_collector()

@action
def BoolTrue(ctx, *_) -> constant.BoolTrue:
    return constant.BoolTrue(metadata=SourceInfo.from_ctx(ctx))
@action
def BoolFalse(ctx, *_) -> constant.BoolFalse:
    return constant.BoolFalse(metadata=SourceInfo.from_ctx(ctx))

@action
def Null(ctx, *_) -> constant.Null:
    return constant.Null(metadata=SourceInfo.from_ctx(ctx))

@action
def Default(ctx, *_) -> constant.Default:
    return constant.Default(metadata=SourceInfo.from_ctx(ctx))
