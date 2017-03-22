package ioc;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class SpringApp {

	public static void main(String[] args) {
		
		// 实例化IoC容器, 从当前类加载路径中获取配置文件
		System.out.println(System.getProperty("java.class.path"));
		ApplicationContext context = new ClassPathXmlApplicationContext("ioc.xml");
		// 从容器中获取Bean，面向接口编程，而不是面向实现
		HelloApi helloApi = context.getBean("hello", HelloApi.class);
		// 执行业务逻辑
		helloApi.sayHello();
	}
}
