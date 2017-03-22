package code.rosetta

object OpString extends App {

  def isNumeric(input: String): Boolean = input.forall(_.isDigit)

  //复制字符串
  val src = "Hello"
  // Its actually not a copy but a reference
  // That is not a problem because String is immutable
  // In fact its a feature
  val des = src
  assert(src eq des) // Proves the same reference is used. 
  // To make a real copy makes no sense.
  // Actually its hard to make a copy, the compiler is too smart.
  // mkString, toString makes also not a real copy
  val cop = src.mkString.toString
  assert((src eq cop)) // Still no copyed image
  val copy = src.reverse.reverse // Finally double reverse makes a copy
  assert(src == copy && !(src eq copy)) // Prove, but it really makes no sense.

  //空字符串
  // assign empty string to a variable
  val s = ""
  // check that string is empty
  s.isEmpty // true
  s == "" // true
  s.size == 0 // true
  // check that string is not empty
  s.nonEmpty // false
  s != "" // false
  s.size > 0 // false

  //字符串比较
  def compare(a: String, b: String) {
    if (a == b) println(s"'$a' and '$b' are lexically equal.")
    else println(s"'$a' and '$b' are not lexically equal.")

    if (a.equalsIgnoreCase(b)) println(s"'$a' and '$b' are case-insensitive lexically equal.")
    else println(s"'$a' and '$b' are not case-insensitive lexically equal.")

    if (a.compareTo(b) < 0) println(s"'$a' is lexically before '$b'.")
    else if (a.compareTo(b) > 0) println(s"'$a' is lexically after '$b'.")

    if (a.compareTo(b) >= 0) println(s"'$a' is not lexically before '$b'.")
    if (a.compareTo(b) <= 0) println(s"'$a' is not lexically after '$b'.")

    println(s"The lexical relationship is: ${a.compareTo(b)}")
    println(s"The case-insensitive lexical relationship is: ${a.compareToIgnoreCase(b)}\n")
  }

  compare("Hello", "Hello")
  compare("5", "5.0")
  compare("java", "Java")
  compare("ĴÃVÁ", "ĴÃVÁ")
  compare("ĴÃVÁ", "ĵãvá")

  // 字符串查找
  "abcd".startsWith("ab") //returns true
  "abcd".endsWith("zn") //returns false
  "abab".contains("bb") //returns false
  "abab".contains("ab") //returns true

  var loc = "abab".indexOf("bb") //returns -1
  loc = "abab".indexOf("ab") //returns 0
  loc = "abab".indexOf("ab", loc + 1) //returns 2

  //字符串字串
  // Ruler             1         2         3         4         5         6
  //         012345678901234567890123456789012345678901234567890123456789012
  val str = "The good life is one inspired by love and guided by knowledge."
  val (n, m) = (21, 16) // An one-liner to set n = 21, m = 16

  // Starting from n characters in and of m length
  assert("inspired by love" == str.slice(n, n + m))

  // Starting from n characters in, up to the end of the string
  assert("inspired by love and guided by knowledge." == str.drop(n))

  // Whole string minus last character
  assert("The good life is one inspired by love and guided by knowledge" == str.init)

  // Starting from a known character within the string and of m length
  assert("life is one insp" == str.dropWhile(_ != 'l').take(m))

  // Starting from a known substring within the string and of m length
  assert("good life is one" == { val i = str.indexOf("good"); str.slice(i, i + m) })
  // Alternatively
  assert("good life is one" == str.drop(str.indexOf("good")).take(m))

  //split & join
  println("Hello,How,Are,You,Today" split "," mkString ".")

}