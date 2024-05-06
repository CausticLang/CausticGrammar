// Helpers
mk_prefix = ($, assoc, prec, op) =>
    assoc(prec, seq($['_OP_'+op], $._expression));
mk_postfix = ($, assoc, prec, op) =>
    assoc(prec, seq($._expression, $['_OP_'+op]));
mk_infix = ($, assoc, prec, op) => assoc(prec,
    seq(field('left', $._expression), $['_OP_'+op], field('right', $._expression)));

// Rules
module.exports = {
    /* Subscription "operators" */
    attribute: $ => prec.left(90, seq(field('root', $._expression), $._OP_ATTR, field('name', $.IDENTIFIER))),
    subscript: $ => prec.left(90, seq(field('root', $._expression), $._OP_SUBSCRIPT_LEFT,
                                      field('sub', $._expression), $._OP_SUBSCRIPT_RIGHT)),
    /* Unary operators */
    _unary_ops: $ => choice(
        $.op_pos, $.op_neg, $.op_log_inv, $.op_bit_inv,
        $.op_inc, $.op_dec,
    ),
    // Prefix
    op_pos: $ => mk_prefix($, prec.right, 70, 'POS'),
    op_neg: $ => mk_prefix($, prec.right, 70, 'NEG'),
    op_log_inv: $ => mk_prefix($, prec.right, 70, 'LOG_INV'),
    op_bit_inv: $ => mk_prefix($, prec.right, 70, 'BIT_INV'),
    // Postfix
    op_inc: $ => mk_postfix($, prec.right, 71, 'INC'),
    op_dec: $ => mk_postfix($, prec.right, 71, 'DEC'),
    /* Binary (infix) operators */
    _binary_ops: $ => choice(
        $.op_add, $.op_sub, $.op_mult, $.op_mmul, $.op_div, $.op_mod, $.op_exp,
        $.op_eq, $.op_ne, $.op_lt, $.op_le, $.op_gt, $.op_gt, $.op_null_coalescing,
        $.op_log_and, $.op_log_or, $.op_log_xor,
    ),
    // Arithmetic
    op_add: $ => mk_infix($, prec.left, 60, 'ADD'),
    op_sub: $ => mk_infix($, prec.left, 60, 'SUB'),
    op_mult: $ => mk_infix($, prec.left, 61, 'MULT'),
    op_mmul: $ => mk_infix($, prec.left, 61, 'MMUL'),
    op_div: $ => mk_infix($, prec.left, 61, 'DIV'),
    op_mod: $ => mk_infix($, prec.left, 61, 'MOD'),
    op_exp: $ => mk_infix($, prec.left, 62, 'EXP'),
    // Comparison
    op_eq: $ => mk_infix($, prec.left, 51, 'EQ'),
    op_ne: $ => mk_infix($, prec.left, 51, 'NE'),
    op_lt: $ => mk_infix($, prec.left, 52, 'LT'),
    op_le: $ => mk_infix($, prec.left, 52, 'LE'),
    op_gt: $ => mk_infix($, prec.left, 52, 'GT'),
    op_ge: $ => mk_infix($, prec.left, 52, 'GE'),
    op_null_coalescing: $ => mk_infix($, prec.left, 40, 'NULL_COALESCING'),
    // Logical
    op_log_and: $ => mk_infix($, prec.left, 42, 'LOG_AND'),
    op_log_or: $ => mk_infix($, prec.left, 40, 'LOG_OR'),
    op_log_xor: $ => mk_infix($, prec.left, 41, 'LOG_XOR'),
    // Bitwise
    op_bit_and: $ => mk_infix($, prec.left, 45, 'BIT_AND'),
    op_bit_or: $ => mk_infix($, prec.left, 44, 'BIT_OR'),
    op_bit_xor: $ => mk_infix($, prec.left, 43, 'BIT_XOR'),
    /// Shift
    op_lshift: $ => mk_infix($, prec.left, 53, 'LSHIFT'),
    op_rshift: $ => mk_infix($, prec.left, 53, 'RSHIFT'),
    /* Ternary operators */
    _ternary_ops: $ => choice(
        $.op_ternary_conditional,
    ),
    op_ternary_conditional: $ => prec.left(30,
        seq(field('target', $._expression),
            $._OP_TERNARY_CONDITION,
            field('true', $._expression),
            $._OP_TERNARY_DELIM,
            field('false', $._expression))),
};
