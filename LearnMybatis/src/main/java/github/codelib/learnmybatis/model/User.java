package github.codelib.learnmybatis.model;

public class User {
    public User() {
		super();
	}
	public User(int id, String age, String userName) {
		super();
		this.id = id;
		this.age = age;
		this.userName = userName;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getAge() {
		return age;
	}
	public void setAge(String age) {
		this.age = age;
	}
	public String getUserName() {
		return userName;
	}
	public void setUserName(String userName) {
		this.userName = userName;
	}
	
	public String toString() {
		return "".format("User [%d, %s, %s]", id, age, userName);
	}
	
	private int id;  
    private String age;  
    private String userName;
}
