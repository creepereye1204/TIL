import enet
import time


def start_client():
    # 서버 주소 설정
    host = enet.Host(None, 1, 2, 0, 0)
    peer = host.connect(enet.Address(b"127.0.0.1", 24872), 0, 0)

    print("서버에 연결 중...")
    timeout = 5000  # 5초 대기

    # 서버 연결 대기
    event = host.service(timeout)
    if event.type == enet.EVENT_TYPE_CONNECT:
        print("서버에 연결되었습니다.")
    else:
        print("서버에 연결 실패.")
        return

    try:
        while True:
            message = input("보낼 메시지를 입력하세요 (종료하려면 'exit' 입력): ")
            if message.lower() == "exit":
                break

            # 메시지를 바이트 배열로 변환
            message_bytes = message.encode("utf-8")
            message_length = len(message_bytes)
            # 메시지 길이와 메시지를 포함한 패킷 생성
            packet_data = message_length.to_bytes(4, "little") + message_bytes

            # 서버로 메시지 전송
            peer.send(0, enet.Packet(packet_data))
            print(f"전송한 데이터: {message}")

            # 서버의 응답 대기
            event = host.service(1000)
            if event.type == enet.EVENT_TYPE_RECEIVE:
                raw_data = event.packet.data
                response_length = int.from_bytes(raw_data, "little")
                response_message = raw_data[4 : 4 + response_length].decode("utf-8", errors="ignore")
                print(f"서버로부터 수신한 응답: {response_message}")

    except KeyboardInterrupt:
        print("클라이언트가 종료되었습니다.")
    finally:
        peer.disconnect()
        host.flush()


if __name__ == "__main__":
    start_client()
