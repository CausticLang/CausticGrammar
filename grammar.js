const fs = require('fs');

let Grammar = {
    name: 'CAUSTIC',
    rules: {},
    //extras:,
    inline: $ => Grammar._unpack.inline.map(n => $[n]),
    conflicts: $ => Grammar._unpack.conflicts.map(c => c.map(n => $[n])),
    externals: $ => Grammar._unpack.externals.map(n => $[n]),
    precedences: $ => Grammar._unpack.precedences,
    //word:,
    supertypes: $ => Grammar._unpack.supertypes.map(n => $[n]),
    _unpack: {
        //extras:,
        inline: [],
        conflicts: [],
        externals: [],
        precedences: [],
        word: undefined,
        supertypes: [],
    },
};


function import_rules(path) {
    console.warn(`Loading grammar rules from ${path}...`);
    //Object.assign(Grammar.rules, require(path));
    for (const [k, v] of Object.entries(require(path))) {
        if (k == '$') {
            console.warn(`${path} has extra non-rule components`);
            import_grammar(v);
        } else {
            if (k in Grammar) console.warn(`Redefinition of rule ${k} in ${path}`);
            Grammar.rules[k] = v;
        }
    }
}

function import_grammar(obj) {
    for (const [k, v] of Object.entries(obj)) {
        if (!(k in Grammar._unpack)) {
            console.warn(`New key defined: ._unpack.${k}`);
            Grammar._unpack[k] = v;
            continue;
        }
        if (v instanceof Array) {
            console.info(`Extending array ._unpack.${k} with ${v.length} element(s)`);
            v.forEach(Grammar._unpack[k].push);
        } else if (typeof(v) == "object") {
            console.info(`Updating ${v.length} item(s) of object _unpack.${k}`);
            Object.assign(Grammar._unpack[k], v);
        } else {
            console.warn(`Replacing value ._unpack.${k}`);
            Grammar._unpack[k] = v;
        }
    }
}
function finish_grammar() {
    console.warn(`Finalizing grammar`);
    if (Grammar._unpack.word !== undefined)
        Grammar.word = $ => $[Grammar._unpack.word];
    if (Grammar._unpack.extras !== undefined)
        Grammar.extras = $ => Grammar._unpack.extras.map(n => $[n]);
}

fs.readdirSync('./rules/').sort().forEach(fn => import_rules(`./rules/${fn}`));

finish_grammar();

module.exports = grammar(Grammar);
