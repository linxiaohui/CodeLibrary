
package com.hackerrank.tutorials.statistics

import scala.math.pow

object Day4BDII {
    def main(args:Array[String]) {
        import scala.math.pow
        val P=readLine.split(" ").map(_.toDouble)
        val p = P(0)/100.0
        val num = P(1)
        val p1=pow(1-p,num)+num*p*pow(1-p,num-1)+num*(num-1)/2*p*p*pow(1-p,num-2)
        val p2=1-pow(1-p,num)-num*p*pow(1-p,num-1)
        println(f"$p1%.3f")
        println(f"$p2%.3f")
    }
}