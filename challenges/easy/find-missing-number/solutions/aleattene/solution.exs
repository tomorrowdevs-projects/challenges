
# Elixir solution for easy challenge: "Find the missing number"

defmodule Challenge do
    @moduledoc """
      This module implements a function that
      returns the missing number in a list of values.
      """

    @doc """
    The following function returns the difference between the sum of the values of a list
    constructed starting from a minimum and maximum value
    (coinciding with the minimum and maximum value of the list received in input)
    and the sum of the values of the same list received in input.
    """
    def missing_number(list) do
      Enum.sum(Enum.min(list) .. Enum.max(list)) - Enum.sum(list)
    end

end


# TEST CASES
numbers = [230, 222, 220, 224, 229, 221, 225, 223, 228, 226]
IO.puts Challenge.missing_number(numbers) # expected value: 227
numbers = [1230, 1222, 1220, 1224, 1229, 1221, 1225, 1223, 1228, 1226]
IO.puts Challenge.missing_number(numbers) # expected value: 1227
missing_number = 1999
number = for n <- 0..5000, n != missing_number, do: n
IO.puts Challenge.missing_number(number) # expected value: 1999
missing_number = 14587
number = for n <- 0..20000, n != missing_number, do: n
IO.puts Challenge.missing_number(number) # expected value: 14587
missing_number = 173877
number = for n <- 0..200000, n != missing_number, do: n
IO.puts Challenge.missing_number(number) # expected value: 173877