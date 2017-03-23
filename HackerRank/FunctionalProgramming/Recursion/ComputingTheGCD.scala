/*
compute GCD using the Euclidean algorithm.
*/

package FunctionalProgramming.Recursion;

object ComputingTheGCD {
	def gcd(x: Int, y: Int): Int = {
		if(x>y) {
			if(x%y==0) y else gcd(x%y,y)
		}
		else {
			if(y%x==0) x else gcd(y%x,x)
		}
	}

	/**This part handles the input/output. Do not change or modify it **/
	def acceptInputAndComputeGCD(pair:List[Int]) = {
		println(gcd(pair.head,pair.reverse.head))
	} 

    def main(args: Array[String]) {
         /** The part relates to the input/output. Do not change or modify it **/
         acceptInputAndComputeGCD(readLine().trim().split(" ").map(x=>x.toInt).toList)
    }
}