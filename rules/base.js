/*
    TODO: $._line can be matched even without $._LINE_END
*/

module.exports = {
    root: $ => repeat($._body),

    ...require('./atoms.js'),
    ...require('./block.js'),
    ...require('./symbols.js'),
    ...require('./operators.js'),
    ...require('./procedure.js'),

    _expression: $ => choice(
        prec.left(999, seq($._PAREN_OPEN, $._expression, $._PAREN_CLOSE)),
        $.IDENTIFIER,
        $.attribute, $.subscript,
        $._unary_ops, $._binary_ops, $._ternary_ops,
        $.proc_invoke, $.proc_expr,
    ),
    _statement: $ => choice(
        $.proc_stmt,
    ),
};
