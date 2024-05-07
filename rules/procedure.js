module.exports = {
    // Declaration
    proc_expr: $ => seq($._PROC_PROC, field('type', $.type),
                        $._PROC_OPEN, optional($._proc_params), $._PROC_CLOSE, field('body', $._body)),
    proc_stmt: $ => prec.left(seq($._PROC_PROC, field('type', $.type), field('name', $.IDENTIFIER),
                              $._PROC_OPEN, optional($._proc_params), $._PROC_CLOSE, field('body', optional($._body)))),

    _proc_params: $ => seq(choice(
        seq(field('pos_params', $.proc_params), $._PROC_ARGSEP, $._PROC_POSONLY,
            optional(seq($._PROC_ARGSEP, field('params', $.proc_params))),
            optional(seq($._PROC_ARGSEP, $._PROC_KWONLY, $._PROC_ARGSEP, field('kw_params', $.proc_params)))),
        seq(field('params', $.proc_params),
            optional(seq($._PROC_ARGSEP, $._PROC_KWONLY, $._PROC_ARGSEP, field('kw_params', $.proc_params)))),
        seq($._PROC_KWONLY, $._PROC_ARGSEP, field('kw_params', $.proc_params)),
    ), optional($._PROC_ARGSEP)),

    _proc_pos_params: $ => prec.left(field('pos_params', seq($.proc_params, $._PROC_ARGSEP, $._PROC_POSONLY))),
    _proc__params: $ => prec.left(field('params', $.proc_params)),
    _proc_kw_params: $ => prec.left(field('kw_params', seq($._PROC_KWONLY, $._PROC_ARGSEP, $.proc_params))),

    proc_params: $ => prec.left(seq($.proc_param, repeat(seq($._PROC_ARGSEP, $.proc_param)))),
    proc_param: $ => seq(field('type', $.type), field('name', $.IDENTIFIER), field('default', optional(seq($._PROC_DEFAULT, $._expression)))),
    // Invokation
    proc_invoke: $ => prec.left(seq(field('proc', $._expression), $._PROC_OPEN, field('args', optional($.proc_args)), $._PROC_CLOSE)),
    proc_args: $ => seq($.proc_arg, repeat(seq($._PROC_ARGSEP, $.proc_arg)), optional($._PROC_ARGSEP)),
    proc_arg: $ => seq(field('name', optional(seq($.IDENTIFIER, $._PROC_KWARG))), field('val', $._expression)),
};
