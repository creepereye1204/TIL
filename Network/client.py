import enet
print("enet version:", enet.__version__)

# 클라이언트 코드


def start_client():
    # 서버의 IP 주소와 포트를 지정합니다.
    server_ip = b"192.168.219.110"  # 여기에 실제 서버 IP를 입력하세요.
    server_port = 24872

    host = enet.Host(enet.Address(b"0.0.0.0", 24872), 32, 2, 0, 0)
    peer = host.connect(enet.Address(
        server_ip, server_port), 0, 0)  # 추가 인자 0, 0을 전달

    message = "Hello, Server!"
    packet = enet.Packet(message.encode("utf-8"))
    peer.send(0, packet)  # 채널 0을 통해 메시지 전송

    # 메시지 전송 후 이벤트 처리
    while True:
        event = host.service(1000)
        if event.type == enet.EVENT_TYPE_RECEIVE:
            print("서버로부터 응답:", event.packet.data.decode("utf-8"))
        elif event.type == enet.EVENT_TYPE_DISCONNECT:
            print("서버와 연결이 끊어졌습니다.")
            break


if __name__ == "__main__":
    start_client()
