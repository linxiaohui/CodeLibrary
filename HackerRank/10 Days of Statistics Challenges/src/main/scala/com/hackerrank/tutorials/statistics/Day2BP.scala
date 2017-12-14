
package com.hackerrank.tutorials.statistics

object Day2BP {
    def main(args:Array[String]) {
        val v= for(i<-1 to 6; j<-1 to 6) yield i+j
        println("%d/%d".format(v.filter(_<=9).size,v.size))
    }
}