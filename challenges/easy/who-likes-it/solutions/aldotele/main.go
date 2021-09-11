package main

import "fmt"

func main() {
  fmt.Println("Enter people below (blank to quit)")
  likes := enterLikes([]string{}, nil)
  fmt.Printf(makeSentence(likes))
}

func enterLikes(x []string, err error) []string {
    if err != nil {
        return x
    }
    var person string
    n, err := fmt.Scanf("%s", &person)
    if n == 1 {
        x = append(x, person)
    }
    return enterLikes(x, err)
}

func makeSentence(likes []string) string {
  if len(likes) == 1 {
    return fmt.Sprintf("%s like this", likes[0])
  } else if len(likes) == 2 {
    return fmt.Sprintf("%s and %s like this", likes[0], likes[1])
  } else if len(likes) == 3 {
    return fmt.Sprintf("%s, %s and %s like this", likes[0], likes[1], likes[2])
  } else if len(likes) > 3 {
    var rem int = len(likes) - 2
    return fmt.Sprintf("%s, %s and %d others like this", likes[0], likes[1], rem)
  }
  return fmt.Sprintf("no one likes this")
}
