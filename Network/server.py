# import enet


# def start_server():
#     host = enet.Host(enet.Address(b"0.0.0.0", 24872), 32, 2, 0, 0)
#     print("Server is running...")

#     while True:
#         event = host.service(1000)
#         try:

#             if event.type == enet.EVENT_TYPE_CONNECT:
#                 print(f"Client connected: {event.peer.address}")
#                 event.peer.data = "Client".encode("utf-8")

#             elif event.type == enet.EVENT_TYPE_RECEIVE:
#                 print(f"Received packet: {event.packet.data.decode()} from {event.peer.data}")
#                 # 클라이언트에게 응답
#                 response = "ACK: " + event.packet.data.decode()
#                 event.peer.send(0, enet.Packet(response.encode()))
#                 host.flush()

#             elif event.type == enet.EVENT_TYPE_DISCONNECT:
#                 print(f"Client disconnected: {event.peer.data}")
#             else:
#                 print(f"Event type: {event.type}")
#         except:
#             print("An error occurred:", str(event))


# if __name__ == "__main__":
#     start_server()
# import enet


# def start_server():
#     host = enet.Host(enet.Address(b"0.0.0.0", 24872), 32, 2, 0, 0)
#     print("서버가 실행 중입니다...")

#     while True:
#         event = host.service(1000)

#         # 이벤트가 발생했는지 확인
#         if event:
#             if event.type == enet.EVENT_TYPE_CONNECT:
#                 print(f"클라이언트가 연결되었습니다: {event.peer.address}")
#                 event.peer.data = "클라이언트".encode("utf-8")

#             elif event.type == enet.EVENT_TYPE_RECEIVE:
#                 try:
#                     message = event.packet.data.decode("utf-8")
#                     print(f"패킷 수신: {message} from {event.peer.data.decode()}")

#                     # 클라이언트에게 응답
#                     response = f"ACK: {message}"
#                     event.peer.send(0, enet.Packet(response.encode("utf-8")))
#                     host.flush()
#                 except UnicodeDecodeError as e:
#                     print(f"메시지 디코딩 오류: {e}, 수신한 데이터: {event.packet.data}")

#             elif event.type == enet.EVENT_TYPE_DISCONNECT:
#                 print(f"클라이언트가 연결을 끊었습니다: {event.peer.data.decode()}")
#                 event.peer.data = None  # 데이터 초기화

#             else:
#                 print(f"이벤트 유형: {event.type}")
#         else:
#             print("이벤트가 없습니다.")


# if __name__ == "__main__":
#     try:
#         start_server()
#     except KeyboardInterrupt:
#         print("서버가 종료되었습니다.")
#     except Exception as e:
#         print("오류 발생:", str(e))
# import enet


# def start_server():
#     host = enet.Host(enet.Address(b"0.0.0.0", 24872), 32, 2, 0, 0)
#     print("서버가 실행 중입니다...")

#     while True:
#         event = host.service(1000)

#         if event:
#             if event.type == enet.EVENT_TYPE_RECEIVE:
#                 raw_data = event.packet.data
#                 print(f"수신한 데이터: {raw_data}")

#                 # 예시: 데이터가 구조체로 인코딩되었다고 가정하고, 이를 해석
#                 try:
#                     # 여기서 필요한 바이트를 추출하고 해석
#                     # 예를 들어, 첫 4바이트를 건너뛰고, 나머지를 UTF-8로 디코딩
#                     message = raw_data[4:].decode("utf-8")  # 필요한 바이트 수에 따라 조정
#                     print(f"디코딩된 메시지: {message}")

#                     # 클라이언트에게 응답
#                     response = f"ACK: {message}"
#                     event.peer.send(0, enet.Packet(response.encode("utf-8")))
#                     host.flush()
#                 except UnicodeDecodeError as e:
#                     print(f"메시지 디코딩 오류: {e}, 수신한 데이터: {raw_data}")


# if __name__ == "__main__":
#     try:
#         start_server()
#     except KeyboardInterrupt:
#         print("서버가 종료되었습니다.")
#     except Exception as e:
#         print("오류 발생:", str(e))
# import enet


# def start_server():
#     host = enet.Host(enet.Address(b"0.0.0.0", 24872), 32, 2, 0, 0)
#     print("서버가 실행 중입니다...")

#     while True:
#         event = host.service(1000)

#         if event:
#             try:
#                 if event.type == enet.EVENT_TYPE_RECEIVE:
#                     raw_data = event.packet.data

#                     try:
#                         # 예시: 데이터의 구조를 이해하고, 필요한 부분을 추출
#                         # 예를 들어, 첫 4바이트는 메시지의 길이를 나타낸다고 가정
#                         message_length = int.from_bytes(raw_data, "little")  # little-endian
#                         message = raw_data[4 : 4 + message_length].decode("utf-8", errors="ignore")  # UTF-8로 디코딩

#                         print(f"수신한 데이터: {message}")

#                         event.peer.send(0, enet.Packet(raw_data))
#                         host.flush()
#                     except UnicodeDecodeError as e:
#                         print(f"메시지 디코딩 오류: {e}, 수신한 데이터: {raw_data}")
#                     except Exception as e:
#                         print(f"오류 발생: {e}")
#                 else:
#                     raw_data = event.packet.data
#                     message_length = int.from_bytes(raw_data, "little")  # little-endian
#                     message = raw_data[4 : 4 + message_length].decode("utf-8", errors="ignore")  # UTF-8로 디코딩

#                     print(f"수신한 데이터: {message}")
#             except Exception as e:
#                 print(f"오류 발생: {e}")


# if __name__ == "__main__":
#     try:
#         start_server()
#     except KeyboardInterrupt:
#         print("서버가 종료되었습니다.")
#     except Exception as e:
#         print("오류 발생:", str(e))
# import enet


# def start_server():
#     max_packet_size = 1500  # 최대 패킷 크기 설정
#     host = enet.Host(enet.Address(b"0.0.0.0", 24872), 32, 2, 0, max_packet_size)
#     print("서버가 실행 중입니다...")

#     while True:
#         event = host.service(1000)

#         if event:
#             try:
#                 if event.type == enet.EVENT_TYPE_RECEIVE:
#                     raw_data = event.packet.data

#                     try:
#                         # 데이터 구조를 이해하고 필요한 부분을 추출
#                         # 첫 1바이트는 메시지 타입을 나타냄
#                         message_type = raw_data[0]

#                         # 첫 4바이트는 메시지의 길이를 나타냄
#                         message_length = int.from_bytes(raw_data[1:5], "little")  # little-endian
#                         message = raw_data[5 : 5 + message_length].decode("utf-8", errors="ignore")  # UTF-8로 디코딩

#                         print(f"수신한 채팅 메시지: {message}")

#                         # 클라이언트에게 응답 (필요한 경우)
#                         response_message = f"서버에서 수신한 메시지: {message}"
#                         response_packet = enet.Packet(response_message.encode("utf-8"))
#                         event.peer.send(0, response_packet)
#                         host.flush()

#                         print(f"알 수 없는 메시지 타입: {message_type}")

#                     except UnicodeDecodeError as e:
#                         print(f"메시지 디코딩 오류: {e}, 수신한 데이터: {raw_data}")
#                     except Exception as e:
#                         print(f"오류 발생: {e}")
#                 elif event.type == enet.EVENT_TYPE_DISCONNECT:
#                     print(f"{event.peer.address}가 연결을 끊었습니다.")
#             except Exception as e:
#                 print(f"오류 발생: {e}")


# if __name__ == "__main__":
#     try:
#         start_server()
#     except KeyboardInterrupt:
#         print("서버가 종료되었습니다.")
#     except Exception as e:
#         print("오류 발생:", str(e))
