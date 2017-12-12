
object Day2MD {
    def main(args:Array[String]) {
        val v= for(i<-1 to 6; j<-1 to 6) yield (i,j)
        println("%d/%d".format(v.filter {case (x,y)=> x!=y && x+y==6}.size,
                v.size))
    }
}