%%%-------------------------------------------------------------------
%% @doc micheleriva public API
%% @end
%%%-------------------------------------------------------------------

-module(micheleriva_app).

-behaviour(application).

-export([start/2, stop/1]).

start(_StartType, _StartArgs) ->
    micheleriva_sup:start_link().

stop(_State) ->
    ok.

%% internal functions
