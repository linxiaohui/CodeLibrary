/*
*/
package FunctionalProgramming.MemoizationAndDP;
object Fibonacci {
    def main(args:Array[String]) {
        val T:Int=readInt()
        val l=(1 to T).map(x=>readInt()).toList
        val m=l.max
        val fib:Array[BigInt]=(0 to m).map(_=>0:BigInt).toArray
        fib(1)=1
        for(i<-(2 to m)) {
            fib(i)=fib(i-1)+fib(i-2)
        }
        for(i<-l) {
            println(fib(i)%(100000007))
        }
    }
    
}