# import enet


# def main():
#     # ENet 초기화

#     # 서버 호스트 생성
#     server = enet.Host(enet.Address(b"0.0.0.0", 24872), 32, 2, 0, 0)

#     print("Server is running on port 24872.")

#     while True:
#         event = server.service(1000)
#         print(event.data)
#         # if event is not None:
#         #     if event.type == 0:
#         #         print("A new client connected!")

#         #     elif event.type == 2:
#         #         print("A client disconnected.")
#         #     else:
#         #         print(f"Received a packet: {event.packet.data.decode()}")
#         #         event.packet.destroy()


# if __name__ == "__main__":

#     main()
import enet


def start_server():
    host = enet.Host(enet.Address(b"0.0.0.0", 24872), 32, 2, 0, 0)
    print("Server is running...")

    while True:
        event = host.service(1000)
        try:

            if event.type == enet.EVENT_TYPE_CONNECT:
                print(f"Client connected: {event.peer.address}")
                event.peer.data = "Client".encode("utf-8")

            elif event.type == enet.EVENT_TYPE_RECEIVE:
                print(f"Received packet: {event.packet.data.decode()} from {event.peer.data}")
                # 클라이언트에게 응답
                response = "ACK: " + event.packet.data.decode()
                event.peer.send(0, enet.Packet(response.encode()))
                host.flush()

            elif event.type == enet.EVENT_TYPE_DISCONNECT:
                print(f"Client disconnected: {event.peer.data}")
            else:
                print(f"Event type: {event.type}")
        except:
            print("An error occurred:", str(event))


if __name__ == "__main__":
    start_server()
