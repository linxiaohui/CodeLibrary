
package com.hackerrank.tutorials.statistics

object Day1SD {
    def main(args:Array[String]) {
        val N=readInt
        val X=readLine.split(" ").map(_.toDouble)
        val u=X.sum/N
        val V=scala.math.sqrt(((X.foldLeft(0.0)((b,x)=>b+(x-u)*(x-u)))/N))
        println(f"$V%.1f")
    }
}