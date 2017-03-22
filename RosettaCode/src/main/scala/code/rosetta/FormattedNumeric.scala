package code.rosetta

object FormattedNumeric extends App{
  val r = 7.125                                   //> r  : Double = 7.125
  println(f" ${-r}%9.3f");                        //>     -7.125
  println(f" $r%9.3f");                           //>      7.125
  println(f" $r%-9.3f");                          //>  7.125    
  println(f" ${-r}%09.3f");                       //>  -0007.125
  println(f" $r%09.3f");                          //>  00007.125
  println(f" $r%-9.3f");                          //>  7.125    
  println(f" $r%+09.3f");                         //>  +0007.125
}