module.exports = {
    base: $ => $._expression,

    ...require('./atoms.js'),
    ...require('./symbols.js'),
    ...require('./operators.js'),

    _expression: $ => choice(
        $.IDENTIFIER,
        $.attribute, $.subscript,
        $._unary_ops,
        $._binary_ops,
        $._ternary_ops,
    ),
};
