#!/bin/python3

#> Imports
import typing
from parglare import get_collector
from caustic.parser import SourceInfo
from caustic.cst import typedecl
from caustic.cst.bases import CausticASTNode, BaseExpression
from caustic.cst.atom import Identifier, DottedIdentifier
from caustic.cst.statement import ProcedureStatement
from collections import abc as cabc
#</Imports

#> Header >/
__all__ = ('action',)

action = get_collector()

@action
def pass_dict(ctx, *_, **kwargs) -> dict: return kwargs
@action
def pass_last(ctx, args, *_) -> typing.Any: return args[-1]

@action
def Singleton(ctx, *_, name: Identifier, val: BaseExpression | None) -> statement.SingletonType:
    return typedecl.SingletonType(metadata=SourceInfo.from_ctx(ctx), name=name, val=val)

@action
def Enum(ctx, *_, name: Identifier, type: BaseExpression | None, body: cabc.Sequence[dict]) -> typedecl.EnumType:
    return typedecl.EnumType(metadata=SourceInfo.from_ctx(ctx), name=name, type=type,
                             body=tuple((b['name'], b['type'] for b in body)))

@action
def members(ctx, *_, name: Identifier, type: BaseExpression, default: CausticASTNode | None) -> tuple[Identifier, DottedIdentifier, CausticASTNode | None]:
    return (name, type, default)

@action
def Struct(ctx, *_, name: Identifier, inherits: DottedIdentifier | None,
           body: cabc.Sequence[tuple[Identifier, DottedIdentifier, CausticASTNode | None]]) -> typedecl.StructType:
    return typedecl.StructType(metadata=SourceInfo.from_ctx(ctx), name=name, members=tuple(body))

@action
def Class(ctx, *_, name: Identifier, inherits: DottedIdentifier | None,
          body: cabc.Sequence[tuple[Identifier, DottedIdentifier, CausticASTNode | None]]) -> typedecl.StructType:
    return typedecl.StructType(metadata=SourceInfo.from_ctx(ctx), name=name, members=tuple(body))
