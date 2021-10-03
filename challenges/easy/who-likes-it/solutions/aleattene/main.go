
// GO solution for challenge: "Who likes this"

package main

import ("fmt"; "strconv")

func likes(followers ...string) string {
  switch (len(followers)) {
    case 0:
      return "no one likes this"
    case 1:
      return followers[0] + " likes this"
    case 2:
      return followers[0] + " and " + followers[1] + " like this"
    case 3:
      return followers[0] + ", " + followers[1] + " and " + followers[2] + " like this"
    default:
      other := strconv.Itoa(len(followers)-2)
      return followers[0] + ", " + followers[1] + " and other " + other + " like this"
  }
}

func main() {
  followers_empty := []string{}
  followers_one := []string{"Peter"}
  followers_two := []string{"Jacob","Alex"}
  followers_three := []string{"Max", "John","Mark"}
  followers_four := []string{"Alex", "Jacob","Mark", "Max"}
  followers_other := []string{"Alex", "Jacob","Mark", "Max", "Michele", "Gabriele", "Simone", "Valentina", "Daniele"}
  fmt.Println(likes(followers_empty...))
  fmt.Println(likes(followers_one...))
  fmt.Println(likes(followers_two...))
  fmt.Println(likes(followers_three...))
  fmt.Println(likes(followers_four...))
  fmt.Println(likes(followers_other...))
}