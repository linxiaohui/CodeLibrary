
package com.hackerrank.tutorials.statistics

import scala.math.sqrt

object Day7SRCC {
    def main(args:Array[String]) {
        import scala.math.sqrt
        val n=readLine.trim().toInt
        val xi=readLine.trim().split(" ").map(_.toDouble)
        val yi=readLine.trim().split(" ").map(_.toDouble)
        
        val xm=xi.sorted.zipWithIndex.toMap
        val ym=yi.sorted.zipWithIndex.toMap
        
        val x=xi.map(f=>xm(f)+1.0)
        val y=yi.map(f=>ym(f)+1.0)
        val ux=x.sum/n
        val uy=y.sum/n
        val cov=x.zip(y).foldLeft(0.0)((r, z)=> r+(z._1-ux)*(z._2-uy))
        val sigmax = sqrt(x.foldLeft(0.0)((r,i)=> r+(i-ux)*(i-ux)))
        val sigmay = sqrt(y.foldLeft(0.0)((r,i)=> r+(i-uy)*(i-uy)))
        println("%.3f".format(cov/sigmax/sigmay))
    }    
}