import enet


# 클라이언트 코드
def start_client():
    host = enet.Host(enet.Address(b"0.0.0.0", 24872), 32, 2, 0, 0)
    peer = host.connect(enet.Address(b"127.0.0.1", 24872))

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
