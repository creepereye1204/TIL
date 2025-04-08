class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("None")

    def delete_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next


def create_and_print_list():
    num_nodes = int(input("노드의 개수 : "))
    linked_list = LinkedList()

    for i in range(1, num_nodes + 1):
        data = int(input(f"노드 #{i} 데이터 : "))
        linked_list.append(data)

    print("생성된 연결 리스트: ", end="")
    linked_list.print_list()


def append_node():
    num_nodes = int(input("노드의 개수 : "))
    linked_list = LinkedList()

    for i in range(1, num_nodes + 1):
        data = int(input(f"노드 #{i} 데이터 : "))
        linked_list.append(data)

    new_data = int(input("끝에 추가할 데이터 : "))
    linked_list.append(new_data)

    print("생성된 연결 리스트: ", end="")
    linked_list.print_list()


def delete_first():
    num_nodes = int(input("노드의 개수 : "))
    linked_list = LinkedList()

    for i in range(1, num_nodes + 1):
        data = int(input(f"노드 #{i} 데이터 : "))
        linked_list.append(data)

    print("생성된 연결 리스트 : ", end="")
    linked_list.print_list()

    linked_list.delete_first_node()

    print("첫 번째 노드 삭제 후 연결 리스트 : ", end="")
    linked_list.print_list()



while True:
    print("\n메뉴:")
    print("1. 연결 리스트 생성 및 출력")
    print("2. 연결 리스트 끝에 노드 추가")
    print("3. 첫 번째 노드 삭제")
    print("4. 종료")

    choice = input("원하는 기능을 선택하세요 (1-4): ")

    if choice == '1':
        create_and_print_list()
    elif choice == '2':
        append_node()
    elif choice == '3':
        delete_first()
    elif choice == '4':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. 1-4 사이의 숫자를 입력하세요.")
