module.exports = {
    root: $ => repeat($._body),

    ...require('./atoms.js'),
    ...require('./block.js'),
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
