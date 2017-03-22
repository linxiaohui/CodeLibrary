package code.rosetta

object OpFunctions {
  //函数调用
  def ??? = throw new NotImplementedError // placeholder for implementation of hypothetical methods
  def myFunction0() = ???
  myFunction0() // function invoked with empty parameter list
  myFunction0 // function invoked with empty parameter list omitted

  def myFunction = ???
  myFunction // function invoked with no arguments or empty arg list
  /* myFunction() */ // error: does not take parameters

  def myFunction1(x: String) = ???
  myFunction1("foobar") // function invoked with single argument
  myFunction1 { "foobar" } // function invoked with single argument provided by a block
  // (a block of code within {}'s' evaluates to the result of its last expression)

  def myFunction2(first: Int, second: String) = ???
  val b = "foobar"
  myFunction2(6, b) // function with two arguments

  def multipleArgLists(first: Int)(second: Int, third: String) = ???
  multipleArgLists(42)(17, "foobar") // function with three arguments in two argument lists

  def myOptionalParam(required: Int, optional: Int = 42) = ???
  myOptionalParam(1) // function with optional param
  myOptionalParam(1, 2) // function with optional param provided

  def allParamsOptional(firstOpt: Int = 42, secondOpt: String = "foobar") = ???
  allParamsOptional() // function with all optional args
  /* allParamsOptional */ // error: missing arguments for method allParamsOptional;
  //        follow with `_' if you want to treat it as a partially applied function

  def sum(values: Int*) = values.foldLeft(0)((a:Int, b:Int) => a + b)
  sum(1, 2, 3) // function accepting variable arguments as literal

  val values = List(1, 2, 3)
  sum(values: _*) // function acception variable arguments from collection
  sum() // function accepting empty variable arguments

  def mult(firstValue: Int, otherValues: Int*) = otherValues.foldLeft(firstValue)((a, b) => a * b)
  mult(1, 2, 3) // function with non-empty variable arguments
  myOptionalParam(required = 1) // function called with named arguments (all functions have named arguments)
  myFunction2(second = "foo", first = 1) // function with re-ordered named arguments
  mult(firstValue = 1, otherValues = 2, 3) // function with named variable argument as literal

  val otherValues = Seq(2, 3)
  mult(1, otherValues = otherValues: _*) // function with named variable argument from collection
  val result = myFunction0() // function called in an expression context
  myFunction0() // function called in statement context
  /* myOptionalParam(optional = 1, 2) */ // error: positional after named argument.

  def transform[In, Out](initial: In)(transformation: In => Out) = transformation(initial)
  val result2 = transform(42)(x => x * x) // function in first-class context within an expression

  def divide(top: Double, bottom: Double) = top / bottom
  val div = (divide _) // partial application -- defer application of entire arg list
  val halve = divide(_: Double, 2) // partial application -- defer application of some arguments

  class Foo(var value: Int)
  def incFoo(foo: Foo) = foo.value += 1 // function showing AnyRef's are passed by reference
  /* def incInt(i: Int) = i += 1 */ // error: += is not a member of Int
  // (All arguments are passed by reference, but reassignment 
  // or setter must be defined on a type or a field 
  // (respectively) in order to modify its value.)

  // No distinction between built-in functions and user-defined functions
  // No distinction between subroutines and function

  //数学函数
  //Math.E; //e
  //Math.PI; //pi
  val x=Math.E+Math.PI;
  val y=Math.PI-Math.E;
  Math.sqrt(x); //square root--cube root also available (cbrt)
  Math.log(x); //natural logarithm--log base 10 also available (log10)
  Math.exp(x); //exponential
  Math.abs(x); //absolute value
  Math.floor(x); //floor
  Math.ceil(x); //ceiling
  Math.pow(x, y); //power

  //计算阶乘
  def factorial(n: Int) = {
    var res = 1
    for (i <- 1 to n)
      res *= i
    res
  }

  //or:

  def factorial2(n: Int):Int = if (n == 0) 1 else n * factorial2(n - 1)
  //or:

  def factorial3(n: Int) = (2 to n).foldLeft(1)(_ * _)

  // 计算递归层数的极限

  def recurseTest(i: Int): Unit = {
    try {
      recurseTest(i + 1)
    } catch {
      case e: java.lang.StackOverflowError =>
        println("Recursion depth on this system is " + i + ".")
    }
  }
  recurseTest(0)
}