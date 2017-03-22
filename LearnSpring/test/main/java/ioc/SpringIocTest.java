package ioc;
import org.junit.Test;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.context.support.FileSystemXmlApplicationContext;

public class SpringIocTest {
    @Test
    public void testClassPathXmlApplicationContext() {
        // 初始化容器,从当前类加载路径中获取配置文件
    	System.out.println(System.getProperty("java.class.path"));
        BeanFactory beanFactory = new ClassPathXmlApplicationContext("ioc.xml");
        // 另一种方式
        ApplicationContext context = new ClassPathXmlApplicationContext("ioc.xml");
        // 从容器中获取Bean
        HelloApi helloApi = beanFactory.getBean("hello", HelloApi.class);
        HelloApi helloApi2 = context.getBean("hello", HelloApi.class);
        // 执行业务逻辑
        helloApi.sayHello();
        helloApi2.sayHello();
        
        System.out.println(helloApi == helloApi2 );
        
    }
    
    @Test
    public void testFileSystemApplicationContext() {
        // 初始化容器, 从文件系统获取配置文件，默认是相对路径，可以指定绝对路径
    	System.out.println(System.getProperty("user.dir"));
        BeanFactory beanFactory = new FileSystemXmlApplicationContext("src/main/resources/ioc.xml");
        // 从容器中获取Bean
        HelloApi helloApi = beanFactory.getBean("hello", HelloApi.class);
        // 执行业务逻辑
        helloApi.sayHello();
    }

}
