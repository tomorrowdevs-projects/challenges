package main

import (
  "bufio"
  "fmt"
  "os"
  "strings"
)

func space(s string, spacing string) string {
  // adding a (changeable) spacing between each character of a string
  spaced := ""
  iterable := []rune(strings.ReplaceAll(s, " ", ""))
  for i := 0; i < len(iterable); i++ {
    spaced += string(iterable[i]) + spacing
  }
  return spaced
} 

func vaporcode(s string) string {
  // returns an uppercase, double-spaced string
  return strings.ToUpper(space(s, "  "))
}

func main(){
  // asking input to the user
  scanner := bufio.NewScanner(os.Stdin)
  fmt.Print("enter word/sentence: ")
  if scanner.Scan() {
    // storing and printing the vaporwave
    vaporwave := vaporcode(scanner.Text())
    fmt.Print(vaporwave)
  } 
}

