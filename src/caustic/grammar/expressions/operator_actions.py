#!/bin/python3

#> Imports
from parglare import get_collector
from caustic.cst import expression
from caustic.parser import SourceInfo
from caustic.cst.bases import CausticASTNode
#</Imports

#> Header >/
__all__ = ('action',)

action = get_collector()

# Unary
@action
def Increment(ctx, *args, target: CausticASTNode) -> expression.Increment:
    return expression.Increment(metadata=SourceInfo.from_ctx(ctx), target=target)
@action
def Decrement(ctx, *args, target: CausticASTNode) -> expression.Decrement:
    return expression.Decrement(metadata=SourceInfo.from_ctx(ctx), target=target)
@action
def UPlus(ctx, *args, target: CausticASTNode) -> expression.UPlus:
    return expression.UPlus(metadata=SourceInfo.from_ctx(ctx), target=target)
@action
def UMinus(ctx, *args, target: CausticASTNode) -> expression.UMinus:
    return expression.UMinus(metadata=SourceInfo.from_ctx(ctx), target=target)
@action
def BitInvert(ctx, *args, target: CausticASTNode) -> expression.BitInvert:
    return expression.BitInvert(metadata=SourceInfo.from_ctx(ctx), target=target)
@action
def LogNot(ctx, *args, target: CausticASTNode) -> expression.LogNot:
    return expression.LogNot(metadata=SourceInfo.from_ctx(ctx), target=target)

# Binary
@action
def AssignExpr(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.AssignExpr:
    return expression.AssignExpr(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
## Arithmetic
@action
def Add(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.Add:
    return expression.Add(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def Sub(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.Sub:
    return expression.Sub(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def Mult(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.Mult:
    return expression.Mult(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def Div(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.Div:
    return expression.Div(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def Mod(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.Mod:
    return expression.Mod(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def MMul(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.MMul:
    return expression.MMul(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def Pow(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.Pow:
    return expression.Pow(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
## Comparison
@action
def Equality(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.Equality:
    return expression.Equality(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def Inequality(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.Inequality:
    return expression.Inequality(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def LessThan(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.LessThan:
    return expression.LessThan(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def GreaterThan(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.GreaterThan:
    return expression.GreaterThan(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def LessThanOrEquality(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.LessThanOrEquality:
    return expression.LessThanOrEquality(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def GreaterThanOrEquality(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.GreaterThanOrEquality:
    return expression.GreaterThanOrEquality(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def Nullish(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.Nullish:
    return expression.Nullish(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
## Logical
@action
def LogAnd(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.LogAnd:
    return expression.LogAnd(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def LogOr(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.LogOr:
    return expression.LogOr(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def LogXor(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.LogXor:
    return expression.LogXor(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
## Bitwise
@action
def BitAnd(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.BitAnd:
    return expression.BitAnd(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def BitOr(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.BitOr:
    return expression.BitOr(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def BitXor(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.BitXor:
    return expression.BitXor(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def LShift(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.LShift:
    return expression.LShift(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
@action
def RShift(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.RShift:
    return expression.RShift(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)

# Ternary
@action
def Ternary(ctx, *args, left: CausticASTNode, right: CausticASTNode) -> expression.Ternary:
    return expression.Ternary(metadata=SourceInfo.from_ctx(ctx), left=left, right=right)
