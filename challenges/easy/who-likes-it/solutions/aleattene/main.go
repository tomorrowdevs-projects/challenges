
// GO solution for challenge: "Who likes this"

package main

import ("fmt"; "strconv")

func likes(followers ...string) string {
  if len(followers) == 0 {
  return "no one likes this"
  } else if len(followers) == 1 {
    return string(followers[0]) + " likes this"
  } else if len(followers) == 2 {
    return string(followers[0]) + " and " + followers[1] + " like this"
  } else if len(followers) == 3 {
    return string(followers[0]) + ", " + followers[1] + " and " + followers[2] + " like this"
  }
  other := strconv.Itoa(len(followers)-2)
  return followers[0] + ", " + followers[1] + " and other " + other + " like this"
}

func main() {
  followers_empty := []string{}
  followers_one := []string{"Peter"}
  followers_two := []string{"Jacob","Alex"}
  followers_three := []string{"Max", "John","Mark"}
  followers_four := []string{"Alex", "Jacob","Mark", "Max"}
  followers_other := []string{"Alex", "Jacob","Mark", "Max", "Michele", "Gabriele", "Simone"}
  fmt.Println(likes(followers_empty...))
  fmt.Println(likes(followers_one...))
  fmt.Println(likes(followers_two...))
  fmt.Println(likes(followers_three...))
  fmt.Println(likes(followers_four...))
  fmt.Println(likes(followers_other...))
}