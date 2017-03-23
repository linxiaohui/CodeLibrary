/*
For a given integer KK, print the first KK rows of Pascal's Triangle.
*/
package FunctionalProgramming.Recursion;
object PascalsTriangle {

	def Pascal(n:Int):Unit = {
		if(n==1) {
			println(1)
		}
		else {
			Pascal(n-1)
			for(j<-(0 to n-1)) {
				print((j+1 to n-1).product/(1 to n-1-j).product+" ")
			}
			println()
		}
	}

    def main(args: Array[String]) {
        val K=readInt()
        Pascal(K)
    }
}