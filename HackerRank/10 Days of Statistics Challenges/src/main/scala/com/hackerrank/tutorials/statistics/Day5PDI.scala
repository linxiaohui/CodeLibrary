
package com.hackerrank.tutorials.statistics

import scala.math.E
import scala.math.pow

object Day5PDI {
    def main(args:Array[String]) {
        import scala.math.E
        import scala.math.pow
        val mean=readLine.trim().toDouble
        val num = readLine.trim().toInt
        val P = pow(mean,num)*pow(E,-mean)/(1 to num).toList.reduce((x,y)=>x*y)
        println("%.3f".format(P))
    }   
}