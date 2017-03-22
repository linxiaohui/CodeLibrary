package ioc;

public class HelloImpl implements HelloApi {

	public String sayHello() {
		System.out.println("Hello Spring");
		return "Hello Spring";
	}

}
