package com.hackerrank.tutorials.statistics

import breeze.stats.distributions.Gaussian

object Day6CLTII {
    def main(args:Array[String]) {
        val tickets=readLine.trim().toDouble
        val students=readLine.trim().toDouble
        val u=readLine.trim().toDouble
        val dev=readLine.trim().toDouble
        val g = Gaussian(u,dev/scala.math.sqrt(students))
        println("%.4f".format(g.cdf(1.0*tickets/students)))
    }    
}