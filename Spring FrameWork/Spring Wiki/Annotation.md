Annotation은 클래스와 메서드에 추가하여 다양한 기능을 부여하는 역할을 한다.
구체적으로 Spring Framework에서 는 해당 클래스가 어떤 역할인지 정하기도 하고, Bean을 주입하기도 하며, 자동으로 getter나 setter를 생성하기도 한다.


스프링에서 사용되는 주요 Annotation.

1. @Component : 해당 클래스가 스프링에서 관리하는 Bean임을 나타냄.

2. @Autowired : 해당 타입의 Bean을 주입받음.

3. @Qualifier : 해당 Bean의 이름으로 주입받음. `@Autowired`와 함께 사용.

4. @Configuration : 스프링 설정 파일임을 나타냄.

5. @Bean : 해당 메소드가 스프링에서 관리하는 Bean을 생성, `@Configuration` 내에서 사용.

6. @Scope : 해당 Bean의 범위를 지정함.

7. @Controller : 스프링 MVC 중 컨트롤러임을 나타냄.

8. @RequestMapping : 요청 매핑 주소를 정의함.

9. @Service : 서비스 계층임을 나타냄.

10. @Repository : DAO 계층임을 나타냄.
