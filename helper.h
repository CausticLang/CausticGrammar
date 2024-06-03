#define _cap_PCC0 _0
#define _cap_PCC0s _0s
#define _cap_PCC0e _0e

#define _cap_COPYSTR(frm) \
    strcpy(malloc(((strlen(frm) + 1) * sizeof(char))), frm)
#define _cap_ERROR(rname, msg) \
    cap_error(auxil, __pcc_ctx, rname, msg, _cap_PCC0s, _cap_PCC0e)

#define _cap_MKNODE(type) \
    (cst_n##type*)malloc(sizeof(cst_n##type))
#define _cap_MKINITNODE(type, ...) \
    cst_binit_##type(malloc(sizeof(cst_Node)), cst_ninit_##type(_cap_MKNODE(type), __VA_ARGS__), _cap_PCC0s, _cap_PCC0e, cap_lno(auxil), cap_cno(auxil, _cap_PCC0s))

#define _cap_ADDPARAM(ptype, type_, name_, val_) \
    do { \
        assert(auxil->stack->mark == PROC_PARAMS); \
        cst_ProcParam* param = malloc(sizeof(cst_ProcParam)); \
        *param = (cst_ProcParam)CST__PROCEDURES__PROC_PARAM__INIT; \
        param->type = type_; \
        param->name = name_; \
        param->val = val_; \
        param->param_type = CST__PROCEDURES__PROC_PARAM_TYPE__##ptype; \
        auxil->stack->data = realloc(auxil->stack->data, ++auxil->stack->auxcount * sizeof(cst_ProcParam*)); \
        ((cst_ProcParam**)auxil->stack->data)[auxil->stack->auxcount-1] = param; \
    } while(0)

#define _cap_ADDNODE(node) \
    cst_ADDNODE(auxil->root, node)
#define _cap_LASTNODE auxil->root->n_nodes-1
