package code.rosetta

import util.control.Breaks.{ breakable, break }
import java.util.Random

object BreakAndFor extends App {

  while (true) {
    val a = new Random().nextInt(20)
    println(a)
    if (a >= 10)
      break
    val b = new Random().nextInt(20)
    println(b)
  }

  for (i <- 10 to 0 by -1) println(i)
  //or
  10 to 0 by -1 foreach println

}
