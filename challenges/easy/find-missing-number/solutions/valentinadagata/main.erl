-module(main).
-import(lists,[sum/1]).
-export([start/0]).

start() ->
  MyList=[230, 222, 220, 224, 229, 221, 225, 223, 228, 226],
  Total = sum(lists:seq(lists:min(MyList), lists:max(MyList))),
  MissingNum = Total - sum(MyList),
  io:fwrite("~w~n", [MissingNum]),
  MissingNum.
