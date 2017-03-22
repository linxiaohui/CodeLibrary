package code.rosetta

object ArryListConcat {
  def main(args: Array[String]) {
    //Array concatenation
    val a = new Array[Int](10)
    println(a.length)
    val arr1 = Array(1, 2, 3)
    val arr2 = Array(4, 5, 6)
    val arr3 = Array(7, 8, 9)

    println(arr1 ++ arr2 ++ arr3)
    //or:
    println(Array concat (arr1, arr2, arr3))

    //List concatenation
    val l1 = List(1, 2, 3)
    val l2 = List(4, 5, 6)
    val l3 = List(7, 8, 9)

    println(l1 ++ l2 ++ l3)
    //or:
    println(List concat (l1, l2, l3))
    //or
    println(l1 ::: l2 ::: l3)

    //字符串连接
    val s = "hello"
    val s2 = s + " world"
    val f2 = () => " !"

    println(s2 + f2()) //> hello world !
  }
}