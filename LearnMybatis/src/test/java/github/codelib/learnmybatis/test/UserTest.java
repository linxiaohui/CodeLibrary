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
        //mybatis�������ļ�
        String resource = "conf.xml";
        //ʹ�������������mybatis�������ļ�����Ҳ���ع�����ӳ���ļ���
        InputStream is = UserTest.class.getClassLoader().getResourceAsStream(resource);
        //����sqlSession�Ĺ���
        SqlSessionFactory sessionFactory = new SqlSessionFactoryBuilder().build(is);
        //ʹ��MyBatis�ṩ��Resources�����mybatis�������ļ�����Ҳ���ع�����ӳ���ļ���
        Reader reader = Resources.getResourceAsReader(resource); 
        //����sqlSession�Ĺ���
        //SqlSessionFactory sessionFactory = new SqlSessionFactoryBuilder().build(reader);
        //������ִ��ӳ���ļ���sql��sqlSession
        SqlSession session = sessionFactory.openSession();
        
        /**
         * ӳ��sql�ı�ʶ�ַ�����
         * github.codelib.learnmybatis.mapper.UserMapper��UserMapper.xml�ļ���mapper��ǩ��namespace���Ե�ֵ��
         * getUser��select��ǩ��id����ֵ��ͨ��select��ǩ��id����ֵ�Ϳ����ҵ�Ҫִ�е�SQL
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
