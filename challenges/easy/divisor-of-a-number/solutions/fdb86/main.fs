module CountDivisors =

    let divisors n =

      let listDiv = [ 1 .. n ]
      let result = listDiv |> List.countBy (fun x -> n % x = 0)
      snd result.Head



    printfn $"The number of divisors of 4 is: {divisors 4}" // => 3 (1, 2, 4)
    printfn $"The number of divisors of 4 is: {divisors 5}" // => 2 (1, 5)
    printfn $"The number of divisors of 4 is: {divisors 12}" // => 6 (1, 2, 3, 4, 6, 12)
    printfn $"The number of divisors of 4 is: {divisors 30}" // => 8 (1, 2, 3, 5, 6, 10, 15, 30)