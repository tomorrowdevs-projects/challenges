-module(main).
-export([start/0, d/1, sumdivs/1]).
 
d(0) -> [];
d(1) -> [];
d(N) -> lists:sort([] ++ divisors(1,N,math:sqrt(N))).

% if the square root is lower than the first num return empty
divisors(F,_N,L) when F > L -> [];
% if the remainder of N and the first is not 0, add 1 to the first number
divisors(F,N,L) when N rem F =/= 0 -> 
    divisors(F+1,N,L);
% if the number is divisible for the first, add them to the list of divisors
divisors(F,N,L) ->
    [F, N div F] ++ divisors(F+1,N,L).
 
sumdivs(N) -> lists:sum(d(N)).


start() ->
  io:fwrite("~w~n", [d(30)]).