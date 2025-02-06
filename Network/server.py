import enet


def start_server():
    max_packet_size = 1500  # 최대 패킷 크기 설정
    host = enet.Host(enet.Address(b"0.0.0.0", 24872), 32, 2, 0, max_packet_size)
    print("서버가 실행 중입니다...")

    while True:
        event = host.service(1000)

        if event:
            try:
                if event.type == enet.EVENT_TYPE_RECEIVE:
                    raw_data = event.packet.data

                    try:
                        # 데이터 구조를 이해하고 필요한 부분을 추출

                        message_length = int.from_bytes(raw_data[1:5], "little")  # little-endian
                        message = raw_data[5 : 5 + message_length].decode("utf-8", errors="ignore")  # UTF-8로 디코딩

                        print(f"수신한 채팅 메시지: {message}")

                        # 클라이언트 정보
                        client_address = event.peer
                        client_id = dir(event.peer)
                        print(f"클라이언트 주소: {client_address}, 패킷 정보: {client_id}")

                        # 클라이언트에게 응답 (필요한 경우)
                        response_message = f"서버에서 수신한 메시지: {message}"
                        response_packet = enet.Packet(response_message.encode("utf-8"))
                        event.peer.send(0, response_packet)
                        host.flush()

                    except UnicodeDecodeError as e:
                        print(f"메시지 디코딩 오류: {e}, 수신한 데이터: {raw_data}")
                    except Exception as e:
                        print(f"오류 발생: {e}")

                elif event.type == enet.EVENT_TYPE_DISCONNECT:
                    print(f"{event.peer.address}가 연결을 끊었습니다.")
                elif event.type == 0:
                    raw_data = event.packet.data
                    message_length = int.from_bytes(raw_data[1:5], "little")  # little-endian
                    message = raw_data[5 : 5 + message_length].decode("utf-8", errors="ignore")  # UTF-8로 디코딩

                    print(f"수신한 채팅 메시지: {message}")

            except Exception as e:
                print(f"오류 발생: {e}")


if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("서버가 종료되었습니다.")
    except Exception as e:
        print("오류 발생:", str(e))
