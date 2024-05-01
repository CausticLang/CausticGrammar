#!/bin/python3

#> Imports
import operator
import parglare
import itertools
from caustic import cst
#</Imports

#> Header >/
action = parglare.get_collector()

@action
def enum_member(ctx, _, *, name: cst.expressions.atoms.Identifier,
                val: cst.expressions.Expression | None = None) -> cst.statements.objects.Enum.Member:
    return cst.statements.objects.Enum.Member(name=name, val=val)

@action
def struct_member(ctx, _, *, name: cst.expressions.atoms.Identifier, type: cst.typedecl.Type,
                  default: cst.expressions.Expression | None = None) -> cst.statements.objects.Struct.Member:
    return cst.statements.objects.Struct.Member(name=name, type=type, default=default)

@action
def namespace_val(ctx, _, *, type: cst.typedecl.Type, name: cst.expressions.atoms.Identifier, val: cst.expressions.Expression) \
        -> cst.statements.objects.Namespace.Member:
    return cst.statements.objects.Namespace.Member(name=name, type=type, val=val)

@action
def namespace(ctx, _, *, name: cst.expressions.atoms.Identifier, super: cst.typedecl.Type | None = None,
              members: list[cst.statements.objects.Namespace.Member | cst.procedure.ProcedureStmt]) -> cst.statements.objects.Namespace:
    ns = cst.statements.objects.Namespace(source=cst.SourceInfo.from_parglare_ctx(ctx),
                                         name=name, super=super, members=[], procedures=[])
    for m in members:
        (ns.procedures if isinstance(m, cst.procedure.ProcedureStmt) else ns.members).append(m)
    return ns

@action
def class_attribute(ctx, data: list[dict]) -> cst.statements.objects.Class.Attribute:
    return cst.statements.objects.Class.Attribute(**data[0])

@action
def cls(ctx, _, *, name: cst.expressions.atoms.Identifier, super: cst.typedecl.Type | None = None,
        members: list[cst.statements.objects.Namespace.Member | cst.statements.objects.Class.Attribute | cst.procedure.ProcedureStmt]) -> cst.statements.objects.Class:
    cls = cst.statements.objects.Class(source=cst.SourceInfo.from_parglare_ctx(ctx),
                                      name=name, super=super, members=[], procedures=[], attributes=[])
    for m in members:
        (cls.procedures if isinstance(m, cst.procedure.ProcedureStmt)
         else cls.members if isinstance(m, cst.statements.objects.Namespace.Member)
         else cls.attributes).append(m)
    return cls
                    
