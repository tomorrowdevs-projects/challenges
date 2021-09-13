package main

import (
  "fmt"
  "bufio"
  "os"
  "strings"
)

func main() {
  likes := ask_likes()
  fmt.Printf(makeSentence(likes))
}

func ask_likes() []string {
  likes := []string{}
  scanner := bufio.NewScanner(os.Stdin)
  fmt.Println("Enter person below (blank to quit)")
  // building an infinite loop until a blank is entered
  for true {
    if scanner.Scan() {
      p := scanner.Text()
      // the following makes sure only the name is extracted
      name := strings.Split(p, " ")[0]
      if name != "" {
        likes = append(likes, name)
      } else {
        break
      }
    }
    fmt.Println("Enter person below (blank to quit)")
  }
  return likes
}

func makeSentence(likes []string) string {
  switch likesCount := len(likes); {
  case likesCount == 1:
    return fmt.Sprintf("%s like this", likes[0])
  case likesCount == 2:
    return fmt.Sprintf("%s and %s like this", likes[0], likes[1])
  case likesCount == 3:
    return fmt.Sprintf("%s, %s and %s like this", likes[0], likes[1], likes[2])
  case likesCount > 3:
    var rem int = len(likes) - 2
    return fmt.Sprintf("%s, %s and %d others like this", likes[0], likes[1], rem)
  }
  return "no one likes this"
}

