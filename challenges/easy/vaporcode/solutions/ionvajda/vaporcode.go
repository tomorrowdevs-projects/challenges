package main

import (
	"fmt"
	"strings"
)

func vaporCode(str string) string {
  var upperString string
  for _, letter := range strings.ReplaceAll(str, " ", "") {
      upperString += strings.ToUpper(string(letter))
      upperString += "  "
  }
  return upperString
}

func main() {
  fmt.Println(vaporCode("Hello, World!"))
  fmt.Println(vaporCode("I love JavaScript!"))
  fmt.Println(vaporCode("I love Rust!"))
}