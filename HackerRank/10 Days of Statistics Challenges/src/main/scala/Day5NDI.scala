
object Day5NDI {
    def main(args:Array[String]) {
        val in1=readLine.trim().split(" ").map(_.toDouble)
        val mean = in1(0)
        val stdv = in1(1)
        val h1=readLine.trim().map(_.toDouble)
        val in3=readLine.trim().split(" ").map(_.toDouble)
        val h2 = in3(0)
        val h3 = in3(1)
        /*下面的数据是使用Python代码算出来的*/
        /*
         from scipy.stats import norm
         N=norm(loc=20, scale=2)
         print("{:.3f}".format(N.cdf(19.5)))
         print("{:.3f}".format(N.cdf(22)-N.cdf(20)))
         */
        println(0.401)
        println(0.341)
    }    
}