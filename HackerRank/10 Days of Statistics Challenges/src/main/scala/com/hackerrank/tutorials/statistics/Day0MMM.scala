
package com.hackerrank.tutorials.statistics

object Day0MMM {
    def main(args:Array[String]) {
        val N = readInt
        val X = readLine.split(" ").map(_.toInt).sorted
        val mean = 1.0*X.sum/N
        val median = if(N%2==1) X(N/2) else (X(N/2-1)+X(N/2))/2.0
        val map = X.groupBy(x=>x).map { case (k,v) => (k,v.length) }
                  .toList
                  .sortBy(x=>(-1*x._2,x._1))
        val mode = map(0)._1
        println(mean)
        println(median)
        println(mode)
    }
}