-define(NUMERAL_ASSIGNEMENT,
        "^\\w+(\\s)*(is)(\\s)*(I|V|X|C|L|M)*$").

-define(VALUE_ASSIGNEMENT,
        "^(\\w|\\s)*\\s(\\d)*Credits$").

-define(MATH_QUESTION,
        "^how much is\\s[^Credits](\\w|\\s)*\\?$").

-define(TRANSLATION_QUESTION,
        "^how many Credits is (\\w|\\s)*\\?$").

-define(KNOWN_COMMANDS, [{numeral_assignement, ?NUMERAL_ASSIGNEMENT}, {value_assignement, ?VALUE_ASSIGNEMENT}, {math_question, ?MATH_QUESTION}, {translation_question, ?TRANSLATION_QUESTION}]).

-define(EXPRESSION_TOKENS, #{
        numeral_assignement => #{
                key =>  "/^\\w+/",
                value => "[I|V|X|L|C|M]$"
        },
        value_assignement => #{
                units => "\\w+.+(?=units)"
                metal => ".+units(\\s)*of(\\s)*\\w+"
                credits => "\\d+\\s*credits(\\s*)?$"
        }
        
}).