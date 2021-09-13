-module(parser).

-include("parser.hrl").

-compile(export_all).

detect_input_command(Input) ->
    lists:map(fun ({Command, CommandRegex}) ->
                      case re:run(Input, CommandRegex) of
                          {match, _X} -> {ok, Command, Input};
                          _Else -> {error, unknown_assignement}
                      end
              end,
              ?KNOWN_COMMANDS).

filter_unknown_commands(Commands) ->
    lists:filter(fun (X) ->
                         case X of
                             {ok, _X, _Y} -> true;
                             {error, unknown_assignement} -> false
                         end
                 end,
                 Commands).

parse(Input) ->
    [H | _T] =
        filter_unknown_commands(detect_input_command(Input)),
    H.
