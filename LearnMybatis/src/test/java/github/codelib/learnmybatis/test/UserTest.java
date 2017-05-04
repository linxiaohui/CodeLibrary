package github.codelib.learnmybatis.test;

import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import github.codelib.learnmybatis.model.User;

public class UserTest {

	public static void main(String[] args) throws IOException {
        //mybatis的配置文件
        String resource = "conf.xml";
        //使用类加载器加载mybatis的配置文件（它也加载关联的映射文件）
        InputStream is = UserTest.class.getClassLoader().getResourceAsStream(resource);
        //构建sqlSession的工厂
        SqlSessionFactory sessionFactory = new SqlSessionFactoryBuilder().build(is);
        //使用MyBatis提供的Resources类加载mybatis的配置文件（它也加载关联的映射文件）
        Reader reader = Resources.getResourceAsReader(resource); 
        //构建sqlSession的工厂
        //SqlSessionFactory sessionFactory = new SqlSessionFactoryBuilder().build(reader);
        //创建能执行映射文件中sql的sqlSession
        SqlSession session = sessionFactory.openSession();
        
        /**
         * 映射sql的标识字符串，
         * github.codelib.learnmybatis.mapper.UserMapper是UserMapper.xml文件中mapper标签的namespace属性的值，
         * getUser是select标签的id属性值，通过select标签的id属性值就可以找到要执行的SQL
         */
        String statement = "github.codelib.learnmybatis.mapper.UserMapper.save";
        User u = new User(1, "20", "Mybatis");
        session.insert(statement, u);
        session.commit();
        statement = "github.codelib.learnmybatis.mapper.UserMapper.findById";
        User user = session.selectOne(statement, 1);
        System.out.println(user);
        String updateStatement = "github.codelib.learnmybatis.mapper.UserMapper.update";
        u.setUserName("LearnMybatis");
        session.update(updateStatement, u);
        session.commit();
        User user2 = session.selectOne(statement, 1);
        System.out.println(user2);
        session.close();

	}

}
