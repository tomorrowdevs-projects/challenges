package main

import (
  "bufio"
  "fmt"
  "os"
  "strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("enter word/sentence: ")
	if scanner.Scan() {
    var w string = scanner.Text()
    // removing spaces and converting to uppercase
    word_stripped := strings.ReplaceAll(w, " ", "")
    word_upper := strings.ToUpper(word_stripped)

    word_iterable := []rune(word_upper)
    //Iterate
    for i := 0; i < len(word_iterable); i++ {
        fmt.Print(string(word_iterable[i]) + "  ")
    }
	}
}
