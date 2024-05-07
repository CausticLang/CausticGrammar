/*
    TODO: $._line can be matched even without $._LINE_END
*/

module.exports = {
    root: $ => repeat($._body),

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

    // note: keywords cannot begin with "_", given this
    // configuration
    _word: $ => /[a-z]\w*/i,

    $: {
        word: '_word',
    },
};
