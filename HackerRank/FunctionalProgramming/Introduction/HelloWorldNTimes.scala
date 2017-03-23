 
package FunctionalProgramming.Introduction;


object HelloWorldNTimes {

/**/
def ff(n: Int) = (1 to n).foreach(e=>println("Hello World"))

def f(n:Int) = print("Hello World\n"*n)

    def main(args: Array[String]) {
    	  f(10)
    }
}
