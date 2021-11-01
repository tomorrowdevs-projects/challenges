defmodule CaesarCipher do
  
  @type frequencyTable :: %{
    integer => integer
  }

  @type frequencyTuple :: {
    integer, integer
  }

  @frequency [
    {?a, 8.167},
    {?b, 1.492},
    {?c, 2.782},
    {?d, 4.253},
    {?e, 12.702},
    {?f, 2.228},
    {?g, 2.015},
    {?h, 6.094},
    {?i, 6.966},
    {?j, 0.153},
    {?k, 0.772},
    {?l, 4.025},
    {?m, 2.406},
    {?n, 6.749},
    {?o, 7.507},
    {?p, 1.929},
    {?q, 0.095},
    {?r, 5.987},
    {?s, 6.327},
    {?t, 9.056},
    {?u, 2.758},
    {?v, 0.978},
    {?w, 2.360},
    {?x, 0.150},
    {?y, 1.974},
    {?z, 0.074}
  ]

  @spec crack(str :: String.t()) :: String.t()
  def crack(str) do
    input = sanitize_input(str)

    input
      |> Enum.reduce(%{}, &(count_char_occurrence(&1, &2)))
      |> Map.to_list
      |> calculate_char_frequency(get_input_length(input))
      |> determine_shift(@frequency)
  end

  def crack_and_print(str) do
    shift_value = crack(str)
    IO.puts(encode(str, shift_value))
  end

  @spec encode(str :: String.t(), shift :: integer) :: String.t()
  def encode(str, shift) do
    str
      |> to_charlist
      |> Enum.map(&(make_shift(&1, shift)))
      |> to_string
  end

  def decode(str, shift) do
    encode(str, -shift)
  end

  @spec make_shift(char :: Char.t(), shift :: integer) :: Char.t()
  defp make_shift(char, shift) do
    cond do
      char in ?A..?Z -> rem(char - ?A + shift, 26) + ?A
      char in ?a..?z -> rem(char - ?a + shift, 26) + ?a
      true           -> char
    end
  end

  @spec sanitize_input(input :: String.t()) :: List.t(Char.t())
  defp sanitize_input(input) do
    input
      |> String.downcase
      |> to_charlist
      |> filter_letters
  end

  @spec get_input_length(input :: String.t()) :: integer
  defp get_input_length(input) do
    input
      |> to_string
      |> String.length
  end

  @spec filter_letters(chars :: List.t(Char.t())) :: List.t(Char.t())
  defp filter_letters(chars) do
    Enum.filter(chars, fn char -> char in ?a..?z end)
  end

  @spec count_char_occurrence(char :: Char.t(), acc :: frequencyTable) :: frequencyTable
  defp count_char_occurrence(char, acc) do
    cond do
      Map.has_key?(acc, char) -> Map.put(acc, char, Map.get(acc, char) + 1)
      true                    -> Map.put(acc, char, 1)
    end
  end

  @spec calculate_char_frequency(List.t(frequencyTuple), length :: integer) :: frequencyTuple
  defp calculate_char_frequency(chars, length) do
    Enum.map(chars, fn {char, frequency} -> {char, Float.round((frequency / length) * 100, 2)} end)
  end

  @spec determine_shift(frequencyTuple, frequencyTuple) :: integer 
  defp determine_shift(input, frequency_table) do
    input_chars     = input           |> sort_frequency_table |> extract_frequency_chars
    frequency_chars = frequency_table |> sort_frequency_table |> extract_frequency_chars

    [{ result, _ } | _] = Enum.zip(input_chars, frequency_chars)
      |> Enum.map(fn { input_char, frequency_char } -> abs(input_char - frequency_char) end)
      |> Enum.frequencies
      |> Map.to_list
      |> Enum.sort_by(fn {_, frequency} -> frequency end)
      |> Enum.reverse

    result
  end

  @spec sort_frequency_table(frequencyTable) :: frequencyTable
  defp sort_frequency_table(frequency_table) do
    frequency_table
      |> Enum.sort_by(fn {_, frequency} -> frequency end)
      |> Enum.reverse
  end

  @spec extract_frequency_chars(frequencyTable) :: List.t(integer)
  defp extract_frequency_chars(frequency_table) do
    frequency_table
      |> Enum.map(fn {char, _} -> char end)
  end

end
