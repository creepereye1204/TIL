
프로그램 디자인이 결합도를 느슨하게 되도록하고 의존관계 역전 원칙과 단일 책임 원칙을 따르도록 클라이언트의 생성에 대한 의존성을 클라이언트의 행위로부터 분리하는 것이며 장점으로는 다음과 같다.

1. 의존성이 줄어든다.

2. 재사용성이 높은 코드가 된다.

3. 테스트하기 좋은 코드가 된다.

4. 가독성이 높아진다.

##예제 code
```java
// MessageService 인터페이스
public interface MessageService {
    void sendMessage(String message, String recipient);
}

// EmailServiceImpl 클래스 (MessageService 인터페이스 구현)
public class EmailServiceImpl implements MessageService {
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println("Email sent to " + recipient + " with message: " + message);
    }
}

// SMSServiceImpl 클래스 (MessageService 인터페이스 구현)
public class SMSServiceImpl implements MessageService {
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println("SMS sent to " + recipient + " with message: " + message);
    }
}
public class MessageClient {

    private MessageService messageService;
    
    // 생성자를 통한 의존성 주입(Constructor Injection)
    public MessageClient(MessageService messageService) {
        this.messageService = messageService;
    }

    public void sendMessage(String message, String recipient) {
        messageService.sendMessage(message, recipient);
    }
}
public class Main {

    public static void main(String[] args) {

        // 이메일 서비스의 인스턴스 생성
        MessageService emailService = new EmailServiceImpl();
        // 의존성 주입하여 메시지 클라이언트 객체 생성
        MessageClient emailClient = new MessageClient(emailService);
        emailClient.sendMessage("Hello, World!", "user@example.com");

        // SMS 서비스의 인스턴스 생성
        MessageService smsService = new SMSServiceImpl();
        // 의존성 주입하여 메시지 클라이언트 객체 생성
        MessageClient smsClient = new MessageClient(smsService);
        smsClient.sendMessage("Hello, World!", "010-1234-5678");
    }
}


```
이 예제에서는 MessageClient가 MessageService 인터페이스를 구현한 EmailServiceImpl 및 SMSServiceImpl 클래스와 느슨한 결합을 유지하면서 객체를 주입받아 각각의 결과를 출력한다.
이처럼 자바에서 의존성 주입 패턴을 사용하면 유연성이 높은 코드를 작성할 수 있으며 재사용성과 가독성이 향상된 테스트하기 좋은 코드로 발전할 수 있다.
