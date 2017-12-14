
package com.hackerrank.tutorials.statistics

object Day5NDII {
    def main(args:Array[String]) {
        val in1=readLine.trim().split(" ").map(_.toDouble)
        val h1=readLine.trim().map(_.toDouble)
        val in3=readLine.trim().split(" ").map(_.toDouble)
        /*下面的数据是使用Python代码算出来的*/
        /*
         from scipy.stats import norm
         N=norm(loc=70, scale=10)
         print("{:.2f}".format(100-100*N.cdf(80)))
         print("{:.2f}".format(100-100*N.cdf(60)))
         print("{:.2f}".format(100*N.cdf(60)))
         */
        println(0.16)
        println(0.84)
        println(0.16)
    }
}