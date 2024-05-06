module.exports = {
    _body: $ => choice($.block, $._line, $._empty_line),
    block: $ => seq($._BLOCK_OPEN, repeat($._body), $._BLOCK_CLOSE),
    _line: $ => seq(choice($._statement, $._expression), $._LINE_END),
    _empty_line: $ => $._LINE_END,
};
