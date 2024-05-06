module.exports = {
    // Declaration
    proc_expr: $ => seq($._PROC_PROC, field('type', $.IDENTIFIER),
                        $._PROC_OPEN, optional($._proc_params), $._PROC_CLOSE, field('body', $._body)),
    proc_stmt: $ => prec.left(seq($._PROC_PROC, field('type', $.IDENTIFIER), field('name', $.IDENTIFIER),
                              $._PROC_OPEN, optional($._proc_params), $._PROC_CLOSE, field('body', optional($._body)))),

    _proc_params: $ => seq(choice(
        seq($._proc_pos_params, optional(seq($._PROC_ARGSEP, $._proc__params)), optional(seq($._PROC_ARGSEP, $._proc_kw_params))),
        seq($._proc__params, optional(seq($._PROC_ARGSEP, $._proc_kw_params))),
        $._proc_kw_params), optional($._PROC_ARGSEP)),

    _proc_pos_params: $ => prec.left(2, field('pos_params', seq($.proc_params, $._PROC_ARGSEP, $._PROC_POSONLY))),
    _proc__params: $ => prec.left(1, field('params', $.proc_params)),
    _proc_kw_params: $ => prec.left(0, field('kw_params', seq($._PROC_KWONLY, $._PROC_ARGSEP, $.proc_params))),

    proc_params: $ => prec.left(seq($.proc_param, repeat(seq($._PROC_ARGSEP, $.proc_param)))),
    proc_param: $ => seq(field('type', $.IDENTIFIER), field('name', $.IDENTIFIER), field('default', optional(seq($._PROC_DEFAULT, $._expression)))),
    // Invokation
    proc_invoke: $ => prec.left(1000, seq(field('proc', $._expression), $._PROC_OPEN, field('args', optional($.proc_args)), $._PROC_CLOSE)),
    proc_args: $ => seq($.proc_arg, repeat(seq($._PROC_ARGSEP, $.proc_arg)), optional($._PROC_ARGSEP)),
    proc_arg: $ => seq(field('name', optional(seq($.IDENTIFIER, $._PROC_KWARG))), field('val', $._expression)),
};
