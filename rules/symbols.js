module.exports = {
    _BLOCK_OPEN:           $ => '{',
    _BLOCK_CLOSE:          $ => '}',
    _LINE_END:             $ => ';',

    // Operators
    /// Subscription
    _OP_ATTR:              $ => '.',
    _OP_SUBSCRIPT_LEFT:    $ => '[',
    _OP_SUBSCRIPT_RIGHT:   $ => ']',
    /// Prefix
    _OP_POS:               $ => '+',
    _OP_NEG:               $ => '-',
    _OP_LOG_INV:           $ => '!',
    _OP_BIT_INV:           $ => '~',
    /// Postfix
    _OP_INC:               $ => '++',
    _OP_DEC:               $ => '--',
    /// Infix
    _OP_ADD:               $ => '+',
    _OP_SUB:               $ => '-',
    _OP_MULT:              $ => '*',
    _OP_MMUL:              $ => '@',
    _OP_DIV:               $ => '/',
    _OP_MOD:               $ => '%',
    _OP_EXP:               $ => '**',

    _OP_EQ:                $ => '==',
    _OP_NE:                $ => '!=',
    _OP_LT:                $ => '<',
    _OP_LE:                $ => '<=',
    _OP_GT:                $ => '>',
    _OP_GE:                $ => '>=',
    _OP_NULL_COALESCING:   $ => '??',

    _OP_LOG_AND:           $ => '&&',
    _OP_LOG_OR:            $ => '||',
    _OP_LOG_XOR:           $ => '^^',

    _OP_BIT_AND:           $ => '&',
    _OP_BIT_OR:            $ => '|',
    _OP_BIT_XOR:           $ => '^',
    _OP_LSHIFT:            $ => '<<',
    _OP_RSHIFT:            $ => '>>',
    /// Ternary
    _OP_TERNARY_CONDITION: $ => '?',
    _OP_TERNARY_DELIM:     $ => ':',
};
