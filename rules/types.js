module.exports = {
    type: $ => prec.left(seq(field('top', $.IDENTIFIER),
                             optional(seq($._SUBTYPE_OPEN, field('sub', $.type), $._SUBTYPE_CLOSE)))),
};
