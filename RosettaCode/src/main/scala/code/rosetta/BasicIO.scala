package code.rosetta

import scala.io.StdIn
object BasicIO {

  //This will work if the input is exactly as specified, with no extra whitespace. 
  println(readLine().split(" ").map(_.toInt).sum)

  //readLine() is Deprecated
  println(StdIn.readLine().split(" ").map(_.toInt).sum)
  //A slightly more robust version:  
  val s = new java.util.Scanner(System.in)
  val sum = s.nextInt() + s.nextInt()
  println(sum)

  //or  
  println(readLine().split(" ").filter(_.length > 0).map(_.toInt).sum)
}