
package com.hackerrank.tutorials.statistics

object Day1Quartiles {
    
    def median(L:Array[Int]) = {
        val s=L.length
        if(s%2==1) L(s/2) else (L(s/2-1)+L(s/2))/2
    }
    def main(args:Array[String]) {
        val N=readInt
        val X=readLine.split(" ").map(_.toInt).sorted
        val q2 = median(X)
        val q1 = median(X.slice(0, X.length/2))
        val q3 = median(X.slice((X.length+1)/2, X.length))
        println(q1)
        println(q2)
        println(q3)
    }
}