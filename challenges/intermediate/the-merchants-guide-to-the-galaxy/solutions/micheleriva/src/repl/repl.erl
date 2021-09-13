-module(repl).

-export([eval_loop/0]).

eval_loop() ->
    {ok, Input} = io:read("> "),
    eval(Input).

eval(Input) ->
    io:fwrite(Input),
    io:fwrite("\n").
