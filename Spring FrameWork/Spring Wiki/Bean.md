##빈(Bean) 
스프링 컨테이너에 의해 관리되는 재사용 가능한 소프트웨어 컴포넌트

빈은 인스턴스화된 객체를 의미하며, 스프링 컨테이너에 등록된 객체를 스프링 빈이라고 한다.
@Bean 어노테이션을 통해 메서드로부터 반환된 객체를 스프링 컨테이너에 등록한다.
EX)
```Java
public class UserServiceImpl implements UserService {
    private UserDao userDao;
    
    // UserDao 객체를 Setter 주입받음
    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }
    
    // UserService 구현 메소드
    public User getUserById(String id) {
        return userDao.getUserById(id);
    }
}
```
```xml
<!-- UserDao Bean 등록 -->
<bean id="userDao" class="com.example.dao.UserDaoImpl" />

<!-- UserService Bean 등록 -->
<bean id="userService" class="com.example.service.UserServiceImpl">
    <property name="userDao" ref="userDao" />
</bean>
```
