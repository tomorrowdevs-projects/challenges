-module(main).
-import(lists,[sum/1]).
-export([start/0]).

findMissingNumber(MyList) ->
  Total = sum(lists:seq(lists:min(MyList), lists:max(MyList))),
  MissingNum = Total - sum(MyList),
  MissingNum.

start() ->
  MyList=[230, 222, 220, 224, 229, 221, 225, 223, 228, 226],
  io:fwrite("~w~n", [findMissingNumber(MyList)]).
