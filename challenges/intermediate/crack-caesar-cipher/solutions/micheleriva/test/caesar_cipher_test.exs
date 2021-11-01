defmodule CaesarCipherTest do
  use ExUnit.Case
  doctest CaesarCipher

  test "greets the world" do
    assert CaesarCipher.hello() == :world
  end
end
