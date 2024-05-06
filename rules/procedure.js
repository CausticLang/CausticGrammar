module.exports = {
    proc_invoke: $ => prec.left(1000, seq(field('proc', $._expression), $._PROC_OPEN, field('args', optional($.proc_args)), $._PROC_CLOSE)),
    proc_args: $ => seq($.proc_arg, repeat(seq($._PROC_ARGSEP, $.proc_arg)), optional($._PROC_ARGSEP)),
    proc_arg: $ => seq(field('name', optional(seq($.IDENTIFIER, $._PROC_KWARG))), field('val', $._expression)),
};
