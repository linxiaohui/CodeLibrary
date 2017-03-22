package code.rosetta

object FizzBuzz extends App {
  1 to 100 foreach { n =>
    println((n % 3, n % 5) match {
      case (0, 0) => "FizzBuzz"
      case (0, _) => "Fizz"
      case (_, 0) => "Buzz"
      case _      => n
    })
  }

  //Geeky over-generalized solution 
  def replaceMultiples(x: Int, rs: (Int, String)*): Either[Int, String] =
    rs map { case (n, s) => Either cond (x % n == 0, s, x) } reduceLeft ((a, b) =>
      a fold (_ => b, s => b fold (_ => a, t => Right(s + t))))
  def fizzbuzz = replaceMultiples(_: Int, 3 -> "Fizz", 5 -> "Buzz") fold (_.toString, identity)
  1 to 100 map fizzbuzz foreach println

  //By a two-liners geek
  def f(n: Int, div: Int, met: String, notMet: String): String = if (n % div == 0) met else notMet
  for (i <- 1 to 100) println(f(i, 15, "FizzBuzz", f(i, 3, "Fizz", f(i, 5, "Buzz", i.toString))))

  //One-liner geek
  for (i <- 1 to 100) println(Seq(15 -> "FizzBuzz", 3 -> "Fizz", 5 -> "Buzz").find(i % _._1 == 0).map(_._2).getOrElse(i))

  //Functional Scala
  def fizzbuzz(l: List[String], n: Int, s: String) = if (l.head.toInt % n == 0) l :+ s else l
  def fizz(l: List[String]) = fizzbuzz(l, 3, "Fizz")
  def buzz(l: List[String]) = fizzbuzz(l, 5, "Buzz")
  def headOrTail(l: List[String]) = if (l.tail.size == 0) l.head else l.tail.mkString
  Stream.from(1).take(100).map(n => List(n.toString)).map(fizz).map(buzz).map(headOrTail).foreach(println)

}